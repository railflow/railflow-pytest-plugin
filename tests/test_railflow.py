import pytest
import json


@pytest.fixture()
def sample_test(testdir):
    testdir.makepyfile("""
    import pytest 
    
    @pytest.mark.railflow(author='Bob',  description='Addition of two numbers',
                    jira_id=100231, test_path='test_calculation.py', 
                    case_fields='filedA1', result_fields='fieldB1',
                    id_mappings='map id1', case_type='test case', case_priority='important')
    def test_pass():
        assert 1==1
        
    @pytest.mark.railflow(testrail_user='Nulli', 
                    testrail_project= "Mathematics", 
                    case_fields='field',
                    result_fields='output',
                    test_path='manipulation.py',
                    case_type='Normal tests',
                    case_priority='Important',
                    assign=['user1@gmail.com', 'user2@gmail.com'])
    class TestClass:
    
        def test_fail(self):
            assert 4 == 5
        
    
    """)
    return testdir
    
@pytest.fixture()
def load_json(sample_test):
    result = sample_test.runpytest('--jsonfile=output.json')
    
    with open('output.json','r') as f:
        report = json.load(f)
    
    return report
    


def test_open_json(load_json):
    """
    Tests if json file created and output is dictionary type
    """
    if type(load_json[0]) == dict:
        assert True
        
        
@pytest.mark.parametrize("A,B",[("author",'Bob'),('description','Addition of two numbers'),
                        ("jira_id", 100231),('test_path','test_calculation.py'),('case_fields','filedA1'),
                        ('result_fields','fieldB1'),('id_mappings', 'map id1'),('case_type','test case'),
                        ('case_priority','important')])  
def test_json(load_json,A,B):
    """
    Tests if railflow_test_attributes are correctly printed in json report
    """
    test_attr = load_json[0]['railflow_test_attributes']
    assert test_attr[A] == B
    


@pytest.mark.parametrize("A,B",[('suite_name','test_json_test_report'), ('test_name','test_pass'), ('details', None), ('markers', ''),
                        ('result', 'PASSED'),('file_name', 'test_json_test_report.py')])    
def test_json_test_report(load_json,A, B):
    """
    Tests report paramters
    """

    report_dict = load_json[0]
    assert report_dict[A] == B
    
 

@pytest.mark.parametrize("A,B",[("testrail_user",'Nulli'),('testrail_project','Mathematics'),
                        ('test_path','manipulation.py'),('case_fields','field'),
                        ('result_fields','output'),('case_type','Normal tests'),
                        ('case_priority','Important'), ('assign', ['user1@gmail.com', 'user2@gmail.com'])])  
def test_json_class(load_json,A,B):
    """
    Tests railflow_test_attributes in class.
    """
    test_attr = load_json[1]['railflow_test_attributes']
    assert test_attr[A] == B
    



@pytest.mark.parametrize("A,B",[('suite_name','TestClass'), ('test_name','test_fail'), ('details', None),
                        ('result', 'FAILED'),('file_name', 'test_json_class_report.py')])    
def test_json_class_report(load_json,A, B):
    """
    Tests failed class report parameters
    """
    report_dict = load_json[1]
    assert report_dict[A] == B
  

