# Amazon Distribution Optimization

**Author:** Glenn Dalbey  
**Course:** D605 Advanced Analytics - Task 3  
**Institution:** Western Governors University  

## Project Overview
Linear Programming solution to optimize Amazon's multi-tier cargo distribution network. The model minimizes transportation costs while satisfying hub capacity, focus city capacity, flow balance, and demand constraints.

## Problem Description
- **Network:** 2 hubs, 3 focus cities, 65 distribution centers
- **Objective:** Minimize total transportation costs
- **Method:** Linear Programming using PuLP and CBC solver
- **Result:** 25.4% cost reduction through Leipzig route optimization

## Files Required
- `amazon_distribution.py` - Main optimization script
- `amazon_sites_demand_capacity.xlsx` - Site capacity and demand data
- `amazon_distribution_costs_full.xlsx` - Transportation cost matrix

## Usage
```bash
# Install dependencies
pip install pandas pulp numpy openpyxl

# Run optimization
python amazon_distribution.py