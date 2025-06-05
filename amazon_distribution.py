

"""
Amazon Distribution Network Optimization Solution

Author: Glenn P. Dalbey
Course: D605 Advanced Analytics - Task 3
Institution: Western Governors University

This script solves Amazon's multi-tier cargo distribution optimization problem
using Linear Programming (PuLP). Data cleaning, robust error handling, and
professional reporting are included. Data exploration and plotting are omitted
for clarity and reproducibility.
"""

import pandas as pd
import pulp
import numpy as np
import os