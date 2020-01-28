import pytest


class OneDimensionLine:
    """ One dimension line which is parallel to x-axis """

    def __init__(self, start: int, end: int) -> None:
        assert type(start) == int, "first_argument must be of 'int', but '{}' was provided: {}".format(start.__class__.__name__, start)
        assert type(end) == int, "second_argument must be of 'int', but '{}' was provided: {}".format(end.__class__.__name__, end)
        assert start <= end, "first_argument: [{}] must be less than or equal to second_argument: [{}]".format(start, end)
        self.start = start
        self.end = end

    def __str__(self):
        return "({}, {})".format(self.start, self.end)

    def overlaps(self, line, end_points_included: bool) -> bool:
        """
            Check if the input line is overlapping
        """
        is_overlapping = True
        first_line_ended_before_second = ((self.end == line.start and not (end_points_included)) or self.end < line.start)
        second_line_ended_before_current = (line.end < self.start or (line.end == self.start and not (end_points_included)))
        if first_line_ended_before_second or second_line_ended_before_current:
            is_overlapping = False
        return is_overlapping


test_data = [
    ((1, 5), (2, 6), False, True),
    ((1, 5), (6, 8), False, False),
    ((1, 5), (5, 8), False, False),
    ((1, 5), (5, 8), True, True),
    ((8, 50), (5, 8), False, False),
    ((8, 50), (5, 8), True, True),
    ((8, 50), (5, 7), True, False),
    ((5, 0), (2, 6), False, AssertionError("first_argument: [5] must be less than or equal to second_argument: [0]")),
    (('5', 0), (2, 6), False, AssertionError("first_argument must be of 'int', but 'str' was provided: 5")),
    ((5, '10'), (2, 6), False, AssertionError("second_argument must be of 'int', but 'str' was provided: 10")),
]


@pytest.mark.parametrize("first_1d_line_coordinates, second_1d_line_coordinates, end_points_included, expected_output_or_error", test_data, ids=[ "Test-{}".format(i+1) for i in range(len(test_data))])
def test_overlapping_1d_lines(first_1d_line_coordinates, second_1d_line_coordinates, end_points_included, expected_output_or_error):
    try:
        assert OneDimensionLine(*first_1d_line_coordinates).overlaps(OneDimensionLine(*second_1d_line_coordinates), end_points_included) == expected_output_or_error
    except Exception as e:
        actual_error_message = str(e)
        expected_error_message = str(expected_output_or_error)
        expected_error_type = type(expected_output_or_error)
        actual_error_type = type(e)
        assert actual_error_type == expected_error_type, "DIFFERENT EXCEPTION TYPE FOUND:: \n\t  Actual(ERROR): '{}'\n\tExpected(ERROR): '{}'".format(actual_error_type, expected_error_type)
        assert actual_error_message.startswith(expected_error_message), "EXCEPTION MESSAGE IS DIFFERENT:: \n\t  Actual(ERROR): '{}'\n\tExpected(ERROR): '{}'".format(actual_error_message, expected_error_message)
