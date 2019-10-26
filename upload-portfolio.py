from botocore.client import Config
from io import BytesIO

import boto3
import mimetypes
import zipfile


def lambda_handler(event, context):
    s3 = boto3.resource('s3')

    portfolio_bucket = s3.Bucket('portfolio.adeelnayyer.uk')
    build_bucket = s3.Bucket('portfoliobuild.adeelnayyer.uk')

    portfolio_zip = BytesIO()
    build_bucket.download_fileobj('portfolio-build.zip', portfolio_zip)

    with zipfile.ZipFile(portfolio_zip) as portfolioZip:
        for name in portfolioZip.namelist():
            obj = portfolioZip.open(name)
            portfolio_bucket.upload_fileobj(
                obj, name, ExtraArgs={'ContentType': mimetypes.guess_type(name)[0]})
            portfolio_bucket.Object(name).Acl().put(ACL='public-read')

    return 'Portfolio is deployed successfully.'
