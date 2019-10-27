from botocore.client import Config
from io import BytesIO

import boto3
import mimetypes
import zipfile


def lambda_handler(event, context):
    sns = boto3.resource('sns')
    topic = sns.Topic(
        'arn:aws:sns:eu-central-1:809411616619:Deploy-Portfolio-Topic')

    location = {
        'bucketName': 'portfoliobuild.adeelnayyer.uk',
        'objectKey': 'portfolio-build.zip'
    }

    try:
        job = event.get('Codepipeline.job')

        if job:
            for artifact in job['data']['inputArtifacts']:
                if (artifact['name'] == 'BuildArtifact'):
                    location = artifact['location']['s3Location']

        print('Building portfolio from: ' + str(location))

        s3 = boto3.resource('s3')
        portfolio_bucket = s3.Bucket('portfolio.adeelnayyer.uk')
        build_bucket = s3.Bucket(location['bucketName'])

        portfolio_zip = BytesIO()
        build_bucket.download_fileobj(location['objectKey'], portfolio_zip)

        with zipfile.ZipFile(portfolio_zip) as portfolioZip:
            for name in portfolioZip.namelist():
                obj = portfolioZip.open(name)
                portfolio_bucket.upload_fileobj(
                    obj, name, ExtraArgs={'ContentType': mimetypes.guess_type(name)[0]})
                portfolio_bucket.Object(name).Acl().put(ACL='public-read')

        print('Deployment successful')

        topic.publish(Subject="Deployment Successful",
                      Message="Portfolio is deployed successfully.")

        if job:
            codepipeline = boto3.client('codepipeline')
            codepipeline.put_job_success_result(jobId=job['id'])
    except:
        print('Deployment Failed')

        topic.publish(Subject="Deployment Failed",
                      Message="Failed to deploy portfolio.")

        raise

    return 'Done!'
