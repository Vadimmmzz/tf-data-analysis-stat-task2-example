import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 230865321

def solution(p: float, x: np.array) -> tuple:
    s=0
    for i in range (len(x)):
        s=s+(x[i]**2)
    l=s/np.quantile(x,1-p/2)
    r=s/np.quantile(x,p/2)
    return l,r
