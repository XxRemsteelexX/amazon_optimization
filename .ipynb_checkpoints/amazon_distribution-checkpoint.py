

"""
Amazon Distribution Network Optimization Solution

Author: Glenn Dalbey
Course: D605 Advanced Analytics - Task 3
Institution: Western Governors University

This script solves Amazon's multi-tier cargo distribution optimization problem
using Linear Programming (PuLP). Data cleaning, robust error handling, and
professional reporting are included. Data exploration and plotting are removed
for clarity and reproducibility.
"""

import pandas as pd
import pulp
import numpy as np
import os



def main():
    """
    Runs Amazon's distribution optimization. Reads input data, builds the model,
    solves for minimum cost, and reports results. Results are saved to output/optimization_results.txt.
    """
    # ---- 1. Load Data ----
    try:
        sites_df = pd.read_excel('amazon_sites_demand_capacity.xlsx')
        costs_df = pd.read_excel('amazon_distribution_costs_full.xlsx')
        print("Data loaded successfully.")
    except FileNotFoundError as e:
        print("ERROR: Required data file not found.", e)
        return


    
    # ---- 2. Data Structuring ----
    hubs = {}
    focus_cities = {}
    centers_demand = {}

    for _, row in sites_df.iterrows():
        site_type = row['Type']
        city = row['City'].replace(' ', '_').replace('/', '_').replace(',', '')
        demand_current = row['Demand/Current tons']
        capacity = row['Capacity']

        if site_type == 'Hub':
            if 'CVG' in city:
                hub_code = 'CVG'
            elif 'AFW' in city:
                hub_code = 'AFW'
            else:
                hub_code = city
            hubs[hub_code] = {'capacity': capacity}

        elif site_type == 'Focus City':
            clean_city = city.split('_')[0]
            focus_cities[clean_city] = {'capacity': capacity}

        elif site_type == 'Center':
            if pd.notna(demand_current):
                centers_demand[city] = demand_current

    print(f"Data summary: {len(hubs)} hubs, {len(focus_cities)} focus cities, {len(centers_demand)} centers")


    
    # ---- 3. Cost Matrix Creation ----
    costs = {}

    # Hub to Focus City costs 
    costs[('CVG', 'Leipzig')] = 1.5
    costs[('CVG', 'San')] = 0.5
    costs[('AFW', 'San')] = 0.5

    for _, row in costs_df.iterrows():
        center = row['Center'].replace(' ', '_').replace('/', '_')
        if pd.notna(row.get('CVG')):
            costs[('CVG', center)] = row['CVG']
        if pd.notna(row.get('AFW')):
            costs[('AFW', center)] = row['AFW']
        if pd.notna(row.get('Leipzig')):
            costs[('Leipzig', center)] = row['Leipzig']
        if pd.notna(row.get('Hyderabad')):
            costs[('Hyderabad', center)] = row['Hyderabad']
        if pd.notna(row.get('San Bernadino')):
            costs[('San', center)] = row['San Bernadino']

    print(f"Cost matrix created with {len(costs)} routes")