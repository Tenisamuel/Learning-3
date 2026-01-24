import pandas as pd

# Load the first CSV file
file1 = 'CTI_NVD_2020.csv'
df1 = pd.read_csv(file1)

# Load the second CSV file
file2 = 'nvd_2020.csv'
df2 = pd.read_csv(file2)

# Create a list to store the results
results = []

# Iterate through each CVE_ID_2 in the second file and find the corresponding Status in the first file
for index, row in df2.iterrows():
    cve_id_2 = row['CVE_ID_2']
    matching_row = df1[df1['CVE_ID'] == cve_id_2]

    if not matching_row.empty:
        status = matching_row['Status'].values[0]
    else:
        status = 'New CVE'

    results.append({'CVE_ID_2': cve_id_2, 'Status': status})

# Convert the results list to a DataFrame
result_df = pd.DataFrame(results)

# Write the results to a new CSV file
output_file = 'NewCVEstatus.csv'
result_df.to_csv(output_file, index=False)

print(f"Comparison complete. Results saved to {output_file}")
