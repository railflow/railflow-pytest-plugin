import pytest


@pytest.mark.railflow(
    testrail_user="Nulli",
    testrail_project="Mathematics",
    case_fields="field",
    result_fields="output",
    test_path="manipulation.py",
    case_type="Normal tests",
    case_priority="Important",
    assign=["user1@gmail.com, user2@gmail.com"],
)
class TestClass:
    def test_add(self):
        a = 3
        b = 2
        c = a + b
        assert c == 5
    
    @pytest.mark.xfail
    def test_subtract(self):
        a = 3
        b = 2
        c = a - b
        assert c == 0

    @pytest.mark.railflow(
        author="Alice",
        description="Division of two numbers",
        jira_id=100334,
        test_path="test_manipulation.py",
        case_fields="fieldZ1",
        result_fields="fieldZ2",
        id_mappings="map id2",
        case_type="test case",
        case_priority="important",
    )
    @pytest.mark.parametrize("a,b,c", [(22, 11, 2), (64, 8, 8), (9, 3, 3)])
    def test_divide(self, a, b, c):
        assert a / b == c
