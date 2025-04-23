import pandas as pd

def project_tracking(file1, file2):
    df1 = pd.read_csv(file1, delimiter=';')
    df2 = pd.read_csv(file2, delimiter=';')

    merged_data = pd.merge(df1, df2, on='project_id')
    merged_data.set_index('project_id', inplace=True)

    project_names = [col for col in df1.columns if 'total' not in col and col != 'project_id']
    statuses = [col for col in df2.columns if 'total' not in col and col != 'project_id']

    # Initialize new columns
    for project in project_names:
        for status in statuses:
            merged_data[f"{project}_{status}"] = 0

    for idx, row in merged_data.iterrows():
        # Check which project columns are non-zero
        non_zero_projects = [proj for proj in project_names if row[proj] > 0]

        if len(non_zero_projects) == 1:
            proj = non_zero_projects[0]
            for status in statuses:
                merged_data.at[idx, f"{proj}_{status}"] = row[status]
        # Else, leave all the new columns at 0 as initialized

    # Drop the original columns
    merged_data.drop(columns=project_names + statuses + ['total_x', 'total_y'], inplace=True)
    merged_data.reset_index(inplace=True)

    # Write the output
    merged_data.to_csv("output.txt", index=False, sep=';', header=True)

project_tracking("file4.csv", "construction_rehab.csv")