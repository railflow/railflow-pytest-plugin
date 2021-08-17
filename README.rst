pytest-railflow-testrail-reporter
=================================

|Testing| |Cov|

The plugin is ready now and can be accessed from the directory itself.
The plugin now works for both python2 and python3.

Install Requirements first using:

::

   pip install -r requirements.txt

Install plugin to local pypi
----------------------------

To install the pytest-railflow-testrail-reporter plugin to local pypi,
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

Tasks for first deliverable
---------------------------

Finished tasks:

::

   - Creation of metadata marker
   - Creation of json test report
   - Integration of metadata into json test report is done.
   - Customize and sort json paramters according to each test
   - Customize metadata and add optional parameters.
   - tested compatibility with python2 and python3
   - Write tests for the plugin
   - Add tox.ini

To-do:

::

   - Add CI workflow -  Jenkins file
   - Write documentation for the plugin
   - Add to pypi

.. |Testing| image:: https://github.com/railflow/railflow-pytest-plugin/actions/workflows/testing.yml/badge.svg
   :target: https://github.com/railflow/railflow-pytest-plugin/actions/workflows/testing.yml
.. |Cov| image:: https://github.com/railflow/railflow-pytest-plugin/actions/workflows/coverage.yml/badge.svg
   :target: https://github.com/railflow/railflow-pytest-plugin/actions/workflows/coverage.yml
