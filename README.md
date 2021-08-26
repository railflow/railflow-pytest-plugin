---
title: 'pytest-railflow-testrail-reporter'
---

[![Testing](https://github.com/railflow/railflow-pytest-plugin/actions/workflows/testing.yml/badge.svg)](https://github.com/railflow/railflow-pytest-plugin/actions/workflows/testing.yml)
[![Cov](https://codecov.io/gh/railflow/railflow-pytest-plugin/branch/main/graph/badge.svg?token=7SB1JK4HWO)](https://codecov.io/gh/railflow/railflow-pytest-plugin)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

Pytest-Railflow-Testrail-reporter is the Pytest plugin generates json
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

  -----------------------------------------------------------------------
  Function level Attributes                       Class level Attributes
  ----------------------------------------------- -----------------------
  testrail\_user                                  \> testrail\_user

  description                                     \> testrail\_project

  jira\_id                                        \> case\_fields

  test\_path                                      \> result\_fields

  case\_fields                                    \> test\_path

  result\_fields                                  \> case\_type

  test\_mappings                                  \> case\_priority

  case\_type                                      \> smart\_assign

  case\_priority                                  
  -----------------------------------------------------------------------

To run the test, enter the following command in the terminal from test
directory.

    pytest --jsonfile output.json

Please check
[examples](https://github.com/railflow/railflow-pytest-plugin/tree/main/examples)
for more information and sample tests.
