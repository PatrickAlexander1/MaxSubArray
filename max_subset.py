#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 21:20:11 2021

@author: patrickwellins
"""

import math

def PatricksMaxSubset(arr):
    
    
    total = 0
    max_ = - math.inf
    max__ = 0
    current_low = + math.inf
    max_element = - math.inf
    
    for v in arr:
        total += v
        max_element = max(max_element, v)
        max_ = max(max_, total)
        max__ = max(max__, total - current_low)
        current_low = min(current_low, total)
        
        
    if max_element < 0:
        return max_element
    else:
        return max(max__, max_)