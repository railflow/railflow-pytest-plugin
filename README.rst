pytest-railflow-testrail-reporter
=================================

|Testing| |Cov|

Pytest-Railflow-Testrail-reporter is the Pytest plugin generates json outputs with predefined metadata as json attributes defined during the tests.

It is designed for generating testrail outputs.

Requirements
------------

In order to use pytest-railflow-testrail-reporter plugin, following prerequsites should be met.

    - Python 2.7, 3.4 or greater   
    - Pytest

Installation
------------

Install Requirements first using:

::

   pip install -r requirements.txt

Using Pip
~~~~~~~~~

To install the pytest-railflow-testrail-reporter plugin using pip
open the terminal in root folder where ``setup.py`` is located.

Run the following command in terminal:

::

   pip install .

This will install the plugin to python package library.

Run the Test
------------

To run the test, enter the following command in the terminal from test
directory.

::

   pytest --jsonfile output.json



.. |Testing| image:: https://github.com/railflow/railflow-pytest-plugin/actions/workflows/testing.yml/badge.svg
   :target: https://github.com/railflow/railflow-pytest-plugin/actions/workflows/testing.yml
.. |Cov| image:: https://github.com/railflow/railflow-pytest-plugin/actions/workflows/coverage.yml/badge.svg
   :target: https://github.com/railflow/railflow-pytest-plugin/actions/workflows/coverage.yml
