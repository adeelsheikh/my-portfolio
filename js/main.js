import React from 'react';
import ReactDOM from 'react-dom';

import ExampleWorkSection from './example-work-section';

const exampleWorks = [{
  title: 'Work Example',
  img: {
    alt: 'example screenshot of a project involving code',
    src: 'images/example1.png'
  }
}, {
  title: 'Work Example',
  img: {
    alt: 'example screenshot of a project involving chemistry',
    src: 'images/example2.png'
  }
}, {
  title: 'Work Example',
  img: {
    alt: 'example screenshot of a project involving cats',
    src: 'images/example3.png'
  }
}];

ReactDOM.render(<ExampleWorkSection exampleWorks={exampleWorks} />, document.getElementById('example-work'))
