import React from 'react';

import ExampleWorkSectionItem from './example-work-section-item';

export default class ExampleWorkSection extends React.Component {
  render() {
    const { exampleWorks } = this.props;

    return (
      <section className="section section--alignCentered section--description">
        {exampleWorks.map((exampleWork, idx) => (
          <ExampleWorkSectionItem key={idx} {...exampleWork} />
        ))}
      </section>
    )
  }
}
