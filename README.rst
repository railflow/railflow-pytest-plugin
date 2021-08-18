pytest-railflow-testrail-reporter
=================================

|Testing| |Cov| |MIT license|

Pytest-Railflow-Testrail-reporter is the Pytest plugin generates json outputs with predefined metadata as json attributes defined during the tests.

It is designed for generating testrail outputs.

Requirements
------------

In order to use pytest-railflow-testrail-reporter plugin, following prerequsites should be met.

    - Python 2.7, 3.4 or greater   
    - Pytest

Installation
------------

Using Pip
~~~~~~~~~

To install the pytest-railflow-testrail-reporter plugin using pip,run the following command in terminal:

::

   pip install pytest-railflow-testrail-reporter

This will install the plugin to the system.

Usage
------

Currently the plugin supports the metadata attributes given below. All other undefined metadata attributes will be rejected with a warning.

=========================   ======================
Function level Attributes   Class level Attributes
=========================   ======================
author           			author
description      			case_fields
jira_id          			result-fields
test_path        			test_path
case_fields      			case-type
result-fields    			case-priority
id-mappings      
case-type        
case-priority    
=========================   ======================

To run the test, enter the following command in the terminal from test
directory.

::

   pytest --jsonfile output.json

Please check examples_ for more information and sample tests.




.. |Testing| image:: https://github.com/railflow/railflow-pytest-plugin/actions/workflows/testing.yml/badge.svg
   :target: https://github.com/railflow/railflow-pytest-plugin/actions/workflows/testing.yml
.. |Cov| image:: https://codecov.io/gh/railflow/railflow-pytest-plugin/branch/main/graph/badge.svg?token=7SB1JK4HWO
   :target: https://codecov.io/gh/railflow/railflow-pytest-plugin
.. |MIT license| image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://lbesson.mit-license.org/
.. _examples: https://github.com/railflow/railflow-pytest-plugin/tree/main/examples
