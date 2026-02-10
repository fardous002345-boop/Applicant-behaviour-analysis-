import pandas as pd

# Load Excel file
file_path = "applicant_behavior_analysis.xlsx"
df = pd.read_excel(file_path, sheet_name="User_Behavior")

# 1. Page-wise user count
page_visits = df["Page_Visited"].value_counts()

# 2. Exit analysis
exit_points = df[df["Exit_Page"] == "Yes"]["Page_Visited"].value_counts()

# 3. Average time spent per page
avg_time = df.groupby("Page_Visited")["Time_Spent_Seconds"].mean()

# Create analysis summary
analysis = pd.DataFrame({
    "Total_Visits": page_visits,
    "Exit_Count": exit_points,
    "Average_Time_Spent": avg_time
}).fillna(0)

# Save report to Excel
analysis.to_excel("applicant_behavior_report.xlsx")

print("Applicant Behavior Analysis completed successfully!")
print(analysis)