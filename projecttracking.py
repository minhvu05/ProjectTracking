import pandas as pd

def project_tracking(file1, file2):
    df1 = pd.read_csv(file1, delimiter = ';')
    df2 = pd.read_csv(file2, delimiter = ';')

    merged_data = pd.merge(df1, df2, on = "project_id")

    # Allows to modify the new df directly, but gets removes the project_id indexing
    merged_data.set_index('project_id', inplace=True)

    # Data from Projects and Status respectively
    project_names = [col for col in df1.columns if 'total' not in col and col != 'project_id']
    statuses = [col for col in df2.columns if 'total' not in col and col != 'project_id']

    for project in project_names:
        for status in statuses:
            merged_name = f"{project}_{status}"
            
            merged_data[merged_name] = 0


    # Removes unneccsary rows (totals and unmerged names) 
    columns_to_remove = project_names + statuses + ['total_x', 'total_y'] 
    merged_data.drop(columns = columns_to_remove, inplace=True)
    
    # Restores the project_id indexing
    merged_data.reset_index(inplace=True)
  


    merged_data.to_csv("output.txt", index = False, sep = ';', header = True)



    # # Update the output columns based on the conditions
    # merged_data.loc[merged_data['blue_1'] > 0, 'blue_1_red_1'] = merged_data['red_1']
    # merged_data.loc[merged_data['blue_1'] > 0, 'blue_1_red_2'] = merged_data['red_2']
    # merged_data.loc[merged_data['blue_2'] > 0, 'blue_2_red_1'] = merged_data['red_1']
    # merged_data.loc[merged_data['blue_2'] > 0, 'blue_2_red_2'] = merged_data['red_2']

    # what happens if two projects from file1 are happening at the same time (not needed anymore(?))
    # merged_data.loc[(merged_data['blue_1'] > 0) & (merged_data['blue_2'] > 0), 
    #                 ['blue_1_red_1', 'blue_1_red_2', 'blue_2_red_1', 'blue_2_red_2']] = 0
    
    # final_data = merged_data[["project_id", "blue_1_red_1", "blue_1_red_2", "blue_2_red_1", "blue_2_red_2"]]

    # final_data.to_csv("output.txt", index = False, sep = ';', header = True)

    


project_tracking("file1.csv", "file2.csv")