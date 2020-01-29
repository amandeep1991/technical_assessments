import pytest

from string_utils import string_utils

test_data = [
    ("1.2", "1.1", None, 1),
    ("1.2", "1.2", None, 0),
    ("1.2", "1.02", None, 0),
    ("1.2", "1.o2", None, AssertionError("ERROR: Provided versions are incompatible << because '2' can't be compared with 'o2' >>")),
    ("1.2", "1.3", None, -1),
    ("1-2", "1-3", "-", -1),
    ("abc", "def", "-", -1),
    ("abc", "def", r"\.", -1),
    ("1.a.2", "1.b.2", None, -1),
    ("2.a", "2.a.2", None, -1),
]


@pytest.mark.parametrize("version_1, version_2, version_splitter, expected_output_or_error", test_data, ids=["Test-{}".format(i + 1) for i in range(len(test_data))])
def test_string_utils_library_for_compare_versions(version_1, version_2, version_splitter, expected_output_or_error):
    try:
        if version_splitter:
            assert string_utils.compare_versions(version_1, version_2, version_splitter) == expected_output_or_error
        else:
            assert string_utils.compare_versions(version_1, version_2) == expected_output_or_error
    except Exception as e:
        actual_error_message = str(e)
        expected_error_message = str(expected_output_or_error)
        expected_error_type = type(expected_output_or_error)
        actual_error_type = type(e)
        assert actual_error_type == expected_error_type, "DIFFERENT EXCEPTION TYPE FOUND:: \n\t  Actual(ERROR): '{}'\n\tExpected(ERROR): '{}'".format(actual_error_type,
                                                                                                                                                      expected_error_type)
        assert actual_error_message.startswith(expected_error_message), "EXCEPTION MESSAGE IS DIFFERENT:: \n\t  Actual(ERROR): '{}'\n\tExpected(ERROR): '{}'".format(
            actual_error_message, expected_error_message)
