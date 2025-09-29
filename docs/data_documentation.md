# Data Documentation

## Overview

This document describes the data sources, formats, and structure used in the Amazon Distribution Network Optimization project.

## Data Files

### 1. amazon_sites_demand_capacity.xlsx

**Description**: Contains information about all network nodes including hubs, focus cities, and distribution centers with their capacities and demand requirements.

**Location**: `data/amazon_sites_demand_capacity.xlsx`

**Structure**:
| Column | Type | Description | Example |
|--------|------|-------------|----------|
| Type | String | Node type in the network | Hub, Focus City, Center |
| City | String | Geographic location | Cincinnati/Northern Kentucky (CVG) |
| Country | String | Country code/name | USA, Germany, India |
| Demand/Current tons | Float | Demand for centers, current flow for hubs | 1250.5 |
| Capacity | Float | Maximum capacity in tons | 95650.0 |

**Data Quality**:
- **Completeness**: 100% for capacity data, demand only applies to centers
- **Accuracy**: Validated against operational data
- **Currency**: Based on 2024 operational parameters

**Network Nodes Summary**:
- **Hubs**: 2 locations (CVG, AFW)
- **Focus Cities**: 3 locations (Leipzig, Hyderabad, San Bernardino)
- **Distribution Centers**: 65+ locations globally

### 2. amazon_distribution_costs_full.xlsx

**Description**: Transportation cost matrix showing cost per ton between all connected node pairs in the network.

**Location**: `data/amazon_distribution_costs_full.xlsx`

**Structure**:
| Column | Type | Description | Example |
|--------|------|-------------|----------|
| Center | String | Destination distribution center | Paris, London, Tokyo |
| CVG | Float | Cost per ton from CVG hub | 1.6 |
| AFW | Float | Cost per ton from AFW hub | 1.8 |
| Leipzig | Float | Cost per ton from Leipzig focus city | 0.5 |
| Hyderabad | Float | Cost per ton from Hyderabad focus city | 1.1 |
| San Bernadino | Float | Cost per ton from San Bernardino focus city | 0.7 |

**Cost Structure**:
- **Units**: USD per ton
- **Basis**: Transportation costs including fuel, labor, and logistics
- **Currency**: All costs in US Dollars
- **Time Period**: Annual average rates

**Data Preprocessing**:
- Missing values (NaN) indicate no direct route available
- Leipzig costs reduced by 10% to reflect negotiated rates
- Costs validated for geographic and operational feasibility
