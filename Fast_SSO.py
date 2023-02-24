"""
An Algorithm which determines the i^th set in a bin T_p,k by using the DP table T_p
"""
import numpy as np

def Fast_SSO(T_p : np.array, k : int, i : int):
    """
    Calculates S_I : the i^th set in T_p,k\\
    T_p is a DP table\\
    k is a positive integer between 0 and p-1\\
    i is a positive integer between 0 and t_p,k 
    """
    j=k
    Z = []
    # n is number of rows in T_p
    n = len(T_p) - 1
    # p is number of columns in T_p
    p = len(T_p[0])
    x = n
    while x > 0:
        if i <= T_p[x-1,j]:
            continue
        else:
            i = i - T_p[x-1,j]
            j = (j - x)%p
            Z.append(x)
        
        x = x - 1
    return Z

