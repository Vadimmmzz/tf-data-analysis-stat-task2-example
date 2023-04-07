import pandas as pd
import numpy as np
import math
from scipy.stats import norm
from scipy.stats import chi2

chat_id = 230865321

def solution(p: float, x: np.array) -> tuple:
    s = len(x)*(x*x).mean()
    a = 1 - p
    l = ((1/4)*s / chi2.ppf(1 - a/2, df = 2*len(x))) ** 0.5
    r = ((1/4)*s / chi2.ppf(a/2, df = 2*len(x))) ** 0.5
    return l, r
