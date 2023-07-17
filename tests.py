from hstest import CheckResult, StageTest, dynamic_test, TestedProgram

test_data = [
    [["miles_to_km 1.6", "The definition is correct!"]],
    [["km_to_meter 1000", "The definition is correct!"]],
    [["ounce_to_gram 28.35", "The definition is correct!"]],
    [["radian_to_degree 57.30", "The definition is correct!"]],
    [["feet_to_meter 0.31", "The definition is correct!"]],
    [["positive_to_negative -1", "The definition is correct!"]],
    [["apple_to_cherry 5", "The definition is correct!"]],
    [["milestokm 1.6", "The definition is incorrect!"]],
    [["miles_to_km 1.6 100", "The definition is incorrect!"]],
    [["miles_to_km onepointsix", "The definition is incorrect!"]],
    [["555 miles_to_km 1.6", "The definition is incorrect!"]],
    [["ten km_to_meter 1000", "The definition is incorrect!"]],
    [["ounce_to_gram", "The definition is incorrect!"]],
    [["ounce_too_gram 28.35", "The definition is incorrect!"]],
    [["ounce_2_gram 28.35", "The definition is incorrect!"]],
    [["1_to_5 5", "The definition is incorrect!"]],
    [["__to__ 10", "The definition is incorrect!"]],
    [["gold_t_o_silver 2", "The definition is incorrect!"]],
    [["?_to_gram 28.35", "The definition is incorrect!"]],
    [["kg_to_gram 5hundred", "The definition is incorrect!"]],
    [["kg_to_gram 10_", "The definition is incorrect!"]],
    [["miles_to_km 1.6 two", "The definition is incorrect!"]],
    [["miles_to_km 1.6 t_o", "The definition is incorrect!"]],
]


class ConverterTest(StageTest):

    @dynamic_test(time_limit=15000, data=test_data)
    def test1(self, arr):
        """
        With a predefined dictionary of definitions and results,
        Checks all of them one by one.
        """
        t = TestedProgram()
        output = t.start().strip()
        if output == "Enter a definition:":
            output = t.execute(arr[0]).strip()
        else:
            return CheckResult.wrong(
                f"Your program should output:\nEnter a definition:\ninstead of:\n{output}")

        if output == arr[1]:
            return CheckResult.correct()
        else:
            return CheckResult.wrong(
                f"Your program should output:\n{arr[1]}\ninstead of:\n{output}")


if __name__ == '__main__':
    ConverterTest().run_tests()
