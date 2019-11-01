import React from 'react';

export default class ExampleWorkSectionItem extends React.Component {
  render() {
    const { title, img } = this.props;
    const { alt, src } = img;

    return (
      <div className="section__exampleWrapper">
        <div className="section__example">
          <img alt={alt}
            className="section__exampleImage"
            src={src} />
          <dl className="color--cloud">
            <dt className="section__exampleTitle section__text--centered">
              {title}
            </dt>
            <dd></dd>
          </dl>
        </div>
      </div>
    );
  }
}
