import numpy as np
import pandas as pd
from itertools import compress
from typing import Sequence

def barssince(condition: Sequence[bool], default=np.inf) -> int:
    """
    Return the number of bars since `condition` sequence was last `True`,
    or if never, return `default`.
        >>> barssince(self.data.Close > self.data.Open)
        3
    """
    return next(compress(range(len(condition)), reversed(condition)), default)


def cross(series1: Sequence, series2: Sequence) -> bool:
    """
    Return `True` if `series1` and `series2` just crossed (either
    direction).
        >>> cross(self.data.Close, self.sma)
        True
    """
    return crossover(series1, series2) or crossover(series2, series1)


def crossover(series1: Sequence, series2: Sequence) -> bool:
    """
    Return `True` if `series1` just crossed over
    `series2`.
        >>> crossover(self.data.Close, self.sma)
        True
    """
    series1 = (
        series1.values if isinstance(series1, pd.Series) else
        (series1, series1) if isinstance(series1, Number) else
        series1)
    series2 = (
        series2.values if isinstance(series2, pd.Series) else
        (series2, series2) if isinstance(series2, Number) else
        series2)
    try:
        return series1[-2] < series2[-2] and series1[-1] > series2[-1]
    except IndexError:
        return False