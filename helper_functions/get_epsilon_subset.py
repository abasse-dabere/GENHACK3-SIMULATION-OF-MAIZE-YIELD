import pandas as pd

def get_epsilon_subset(path_to_data= 'data') -> pd.DataFrame:
    """
    Returns the data includes in the epislon subset
    The data will be in this format | Year | W_1_1 | ... | W_1_18 |... | W_4_1 | ... | W_4_18 | Yield_1 | ... | Yield_4 |
    """

    # Read in the data
    data_1 = pd.read_csv(path_to_data+'/station_49.csv') # for station 49
    data_2 = pd.read_csv(path_to_data+'/station_80.csv') # for station 80
    data_3 = pd.read_csv(path_to_data+'/station_40.csv') # for station 40
    data_4 = pd.read_csv(path_to_data+'/station_63.csv') # for station 63

    # Filter the data to only keep the rows where W_13 + W_14 + W_15 <= Q
    Q1 = 3.3241
    Q2 = 5.1292
    Q3 = 6.4897
    Q4 = 7.1301

    data_1 = data_1[data_1['W_13'] + data_1['W_14'] + data_1['W_15'] <= Q1]
    data_2 = data_2[data_2['W_13'] + data_2['W_14'] + data_2['W_15'] <= Q2]
    data_3 = data_3[data_3['W_13'] + data_3['W_14'] + data_3['W_15'] <= Q3]
    data_4 = data_4[data_4['W_13'] + data_4['W_14'] + data_4['W_15'] <= Q4]

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

    final_merged_df = pd.merge(merged_1_2, merged_3_4, on='YEAR', how='inner')

    # rearange the columns
    not_yields_columns = [col for col in final_merged_df.columns if 'YIELD' not in col]
    yields_columns = [col for col in final_merged_df.columns if 'YIELD' in col]

    final_merged_df = final_merged_df[not_yields_columns + yields_columns]

    return final_merged_df

