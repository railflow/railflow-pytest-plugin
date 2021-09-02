# pytest-railflow-testrail-reporter

[![PyPI](https://img.shields.io/pypi/v/pytest-railflow-testrail-reporter)](https://pypi.org/project/pytest-railflow-testrail-reporter/)
[![Build](https://github.com/railflow/railflow-pytest-plugin/actions/workflows/testing.yml/badge.svg)](https://github.com/railflow/railflow-pytest-plugin/actions/workflows/testing.yml)
[![Cov](https://codecov.io/gh/railflow/railflow-pytest-plugin/branch/main/graph/badge.svg?token=7SB1JK4HWO)](https://codecov.io/gh/railflow/railflow-pytest-plugin)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/pytest-railflow-testrail-reporter)](https://pypi.org/project/pytest-railflow-testrail-reporter/)

pytest-railflow-testrail-reporter is a pytest plugin generates json
outputs with predefined metadata as json attributes defined during the
tests.

It is designed for generating testrail outputs.

Requirements
============

In order to use pytest-railflow-testrail-reporter plugin, following
prerequsites should be met.

> -   Python 2.7, 3.4 or greater
> -   Pytest

Installation
============

Using Pip
---------

To install the pytest-railflow-testrail-reporter plugin using pip,run
the following command in terminal:

    pip install pytest-railflow-testrail-reporter

This will install the plugin to the system.

Usage
=====

Currently the plugin supports the metadata attributes given below. All
other undefined metadata attributes will be rejected with a warning.


  Function level Attributes | Class level Attributes
  --------------------------|-----------------------
  jira\_ids | case\_fields
  case\_fields | result\_fields
  result\_fields | case\_type
  testrail\_ids | case\_priority
  case\_type | smart\_assignment
  case\_priority | 

To run the test, enter the following command in the terminal from test
directory.

    pytest --jsonfile output.json

Examples
========

Please check
[examples](https://github.com/railflow/railflow_pytest_examples)
for more information and sample tests.

License
=======

This software is licensed under the [MIT license](https://lbesson.mit-license.org/)

See [License file](https://github.com/railflow/railflow-pytest-plugin/blob/main/LICENSE) for more information.
