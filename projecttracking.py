import pandas as pd

def project_tracking(file1, file2):
    df1 = pd.read_csv(file1, delimiter = ';')
    df2 = pd.read_csv(file2, delimiter = ';')

    merged_data = pd.merge(df1, df2, on = "project_id")

    # init all values to 0, fix later
    merged_data["blue_1_red_1"] = 0
    merged_data["blue_1_red_2"] = 0
    merged_data["blue_2_red_1"] = 0
    merged_data["blue_2_red_2"] = 0

    # Update the output columns based on the conditions
    merged_data.loc[merged_data['blue_1'] > 0, 'blue_1_red_1'] = merged_data['red_1']
    merged_data.loc[merged_data['blue_1'] > 0, 'blue_1_red_2'] = merged_data['red_2']
    merged_data.loc[merged_data['blue_2'] > 0, 'blue_2_red_1'] = merged_data['red_1']
    merged_data.loc[merged_data['blue_2'] > 0, 'blue_2_red_2'] = merged_data['red_2']

    # what happens if two projects from file1 are happening at the same time (not needed anymore(?))
    # merged_data.loc[(merged_data['blue_1'] > 0) & (merged_data['blue_2'] > 0), 
    #                 ['blue_1_red_1', 'blue_1_red_2', 'blue_2_red_1', 'blue_2_red_2']] = 0
    
    final_data = merged_data[["project_id", "blue_1_red_1", "blue_1_red_2", "blue_2_red_1", "blue_2_red_2"]]

    final_data.to_csv("output.txt", index = False, sep = ';', header = True)

    


project_tracking("file1.csv", "file2.csv")