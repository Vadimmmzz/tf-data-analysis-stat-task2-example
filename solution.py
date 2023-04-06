import pandas as pd
import numpy as np
import math

from scipy.stats import norm


chat_id = 230865321

def solution(p: float, x: np.array) -> tuple:
    s=0
    for i in range (len(x)):
        s=s+(x[i]**2)
    l=math.sqrt(s/np.quantile(x,1-p/2))/2
    r=math.sqrt(s/np.quantile(x,p/2))/2
    return l,r
