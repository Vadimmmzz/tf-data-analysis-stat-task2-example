import pandas as pd
import numpy as np
import math
from scipy.stats import norm


chat_id = 230865321

def solution(p: float, x: np.array) -> tuple:
    s = 0
    a = 1 - p
    for i in range(len(x)):
        s = s + (x[i] ** 2)
    hil = np.quantile(x, 1-a/2)
    hir = np.quantile(x, a/2)
    s = math.sqrt(s)
    l = s/(2*hil)
    r = s /(2*hir)
    return l, r
