import numpy as np
from multiset import *
"""
Implements the DP-Table required to solve the subset sum problem
"""
def DPTable(S : Multiset ,p : int):
    """
    This function takes a multiset S and a number p as input and returns a table T_p
    where T_p[i,j] is the number of subsets of the first i elements of S which sum to j mod p\\
    S is a multiset\\
    p is a positive integer
    """
    # define a table of size (n+1) x p
    T = np.zeros((len(S)+1,p))
    # set 0,0 entry to 1
    T[0,0] = 1
    # for the second row onwards, t_p[i,j] = t_p[i-1,j] + t_p[i-1,j-S[i] mod p]
    for i in range(1,len(S)+1):
        for j in range(p):
            T[i,j] = T[i-1,j] + T[i-1,(j-S[i-1])%p]
    return T
