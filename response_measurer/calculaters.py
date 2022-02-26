def calculate_mean(values: list):
    return sum(values) / len(values)


# Ref: https://stackoverflow.com/a/7464107/14091937
def calculate_percentile(n: list, p: float):
    """
    Find the percentile of a list of values

    @parameter N - A list of values.  N must be sorted.
    @parameter P - A float value from 0.0 to 1.0

    @return - The percentile of the values.
    """
    k = int(round(p * len(n) + 0.5))
    return n[k - 1]
