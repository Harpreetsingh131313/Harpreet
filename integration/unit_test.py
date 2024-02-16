from sampletest import pass_value, fail_value

def test_pass():
    expected_value = pass_value
    actual_value = "success"
    if expected_value == actual_value:
        assert True
    else:
        assert False, "Test failed: Expected value does not match actual value"

def test_fail():
    expected_value = fail_value
    actual_value = "error"
    if expected_value == actual_value:
        assert True
    else:
        assert False, "Test failed: Expected value does not match actual value"