import pandas as pd
import numpy as np

def get_scenarios(path_to_data= 'data') -> dict:
    """
    returns a dictionary D with the data for each scenario
    keys are the scenario numbers and values are the dataframes
    example: D[1] is the dataframe for scenario 1
    
    There are 9 scenarios, from 1 to 9
    """
    # Read in the data
    data_1 = pd.read_csv(path_to_data+'/station_49.csv') # for station 49
    data_2 = pd.read_csv(path_to_data+'/station_80.csv') # for station 80
    data_3 = pd.read_csv(path_to_data+'/station_40.csv') # for station 40
    data_4 = pd.read_csv(path_to_data+'/station_63.csv') # for station 63

    # rename colums W_i to W_{station_id}_i
    data_1 = data_1.rename(columns=lambda x: x.replace('W_', 'W_1_'))
    data_2 = data_2.rename(columns=lambda x: x.replace('W_', 'W_2_'))
    data_3 = data_3.rename(columns=lambda x: x.replace('W_', 'W_3_'))
    data_4 = data_4.rename(columns=lambda x: x.replace('W_', 'W_4_'))

    # rename colums YIELD to YIELD_{station_id}
    data_1 = data_1.rename(columns={'YIELD': 'YIELD_1'})
    data_2 = data_2.rename(columns={'YIELD': 'YIELD_2'})
    data_3 = data_3.rename(columns={'YIELD': 'YIELD_3'})
    data_4 = data_4.rename(columns={'YIELD': 'YIELD_4'})

    # Merge the data on YEAR
    merged_1_2 = pd.merge(data_1, data_2, on='YEAR', how='inner')
    merged_3_4 = pd.merge(data_3, data_4, on='YEAR', how='inner')

    merged_df = pd.merge(merged_1_2, merged_3_4, on='YEAR', how='inner')

    # rearange the columns
    not_yields_columns = [col for col in merged_df.columns if 'YIELD' not in col]
    yields_columns = [col for col in merged_df.columns if 'YIELD' in col]

    merged_df = merged_df[not_yields_columns + yields_columns]
    # | Year | W_1_1 | ... | W_1_18 |... | W_4_1 | ... | W_4_18 | Yield_1 | ... | Yield_4 |

    # temperature columns
    temp_colums = [col for col in merged_df.columns if 'W' in col and int(col.split('_')[-1]) <= 9]
    rainfall_colums = [col for col in merged_df.columns if 'W' in col and col.split('_')[-1] in ['13', '14', '15'] ]

    # add T columns by summing the temp_colums columns
    merged_df['T'] = merged_df[temp_colums].sum(axis=1)/36

    # add R columns by summing the rainfall_colums columns
    merged_df['R'] = merged_df[rainfall_colums].sum(axis=1)/12

    # set T = 1 if T<=21.2, T = 2 if 21.2 < T <= 22, T = 3 if 22 < T
    merged_df['T'] = pd.cut(merged_df['T'], bins=[-np.inf, 21.2, 22, np.inf], labels=[1, 2, 3])

    # set R = 1 if R<=1.8, R = 2 if 1.8 < R <= 2.2, R = 3 if 2.2 < R
    merged_df['R'] = pd.cut(merged_df['R'], bins=[-np.inf, 1.8, 2.2, np.inf], labels=[1, 2, 3])

    # store each scenario data
    scenarios = dict()

    k = 1
    for i in range(1, 4):
        for j in range(1, 4):
            scenarios[k] = merged_df[(merged_df['R'] == i) & (merged_df['T'] == j)].drop(columns=['R', 'T'])
            k += 1

    return scenarios