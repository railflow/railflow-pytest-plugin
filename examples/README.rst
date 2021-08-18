Examples Using Pytest-Railflow-Testrail-Reporter
================================================

The plugin is ready now and can be accessed from the directory itself.
The plugin now works for both python 2.7 and python 3.6 or greater.

Installation
------------

You can install the plugin via pip using the following command.

::

   pip install pytest-railflow-testrail-reporter
   
Writing Tests 
-------------

The plugin supports following metadata attributes. All other undefined metadata attributes will be rejected with a warning.

=========================   =========================
Function level Attributes   Class level Attributes
=========================   =========================
author                      author
description                 case_fields
jira_id                     result-fields
test_path                   test_path
case_fields                 case-type
result-fields               case-priority
id-mappings      
case-type        
case-priority    
=========================   =========================

The attributes should be defined in the markers with marker name ``railflow``.

So a sample test case looks like:

::

	import pytest
	
	@pytest.mark.railflow(author="Bob")
	def test_sample():
	    """
            This is a sample test
            """
            assert 1 == 1
      
Run the Test
------------

      
Write the above test to a file with ``test_`` as prefix (eg: ``test_file.py``). Now run the test using the command:

::

	pytest --jsonfile test_output.json test_file.py
	
Here ``test_output.json`` is the name of output json file.

Other Examples
--------------

Function level
~~~~~~~~~~~~~~

1. All attributes can be defined inside a single railflow marker as shown below.

::

	import pytest

	@pytest.mark.railflow(author='Bob',  description='Addition of two numbers',
                    jira_id=100231, test_path='test_calculation.py', 
                    case_fields="filedA1", result_fields="fieldB1",
                    id_mappings="map id1", case_type="test case", case_priority="important",
                    email="test@mail.com") # here email is a not defined parameter
	def test_add():
	    """
	    Add two numbers
	    """
	    a = 2 + 7
	    assert a == 9

2. It is also possible to define the attributes in separate markers for a single test. But the metadata should be added in reverse order as shown below:

::

	import pytest

	@pytest.mark.railflow(case_priority="normal")
	@pytest.mark.railflow(case_type="test case")
	@pytest.mark.railflow(id_mappings="map id2")
	@pytest.mark.railflow(result_fields="fieldB2")
	@pytest.mark.railflow(case_fields="filedA2")
	@pytest.mark.railflow(test_path='test_calculation.py')
	@pytest.mark.railflow(jira_id=100241)
	@pytest.mark.railflow(description='modulus of two numbers')
	@pytest.mark.railflow(author='Bob123')
	def test_add():
	    """
	    Add two numbers
	    """
	    a = 2 + 7
	    assert a == 9
