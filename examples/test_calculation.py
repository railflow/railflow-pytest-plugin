import pytest


@pytest.mark.railflow(
    author="Bob",
    description="Addition of two numbers",
    jira_id=100231,
    test_path="test_calculation.py",
    case_fields="filedA1",
    result_fields="fieldB1",
    id_mappings="map id1",
    case_type="test case",
    case_priority="important",
    email="test@mail.com",
)  # here email is a not defined parameter
def test_power():
    """
    Test details are given here.
    """
    a = 3
    b = 2
    c = a ** b
    assert c == 9


@pytest.mark.railflow(case_priority="normal")
@pytest.mark.railflow(case_type="test case")
@pytest.mark.railflow(id_mappings="map id2")
@pytest.mark.railflow(result_fields="fieldB2")
@pytest.mark.railflow(case_fields="filedA2")
@pytest.mark.railflow(test_path="test_calculation.py")
@pytest.mark.railflow(jira_id=100241)
@pytest.mark.railflow(description="modulus of two numbers")
@pytest.mark.railflow(author="Bob123")
def test_modulus():
    a = 3
    b = 2
    c = a % b
    assert c == 0
