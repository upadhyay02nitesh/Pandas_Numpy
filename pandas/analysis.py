import pandas as pd
import numpy as np 

df_attendance=pd.read_csv('emp_data.csv')
# print(df_attendance.head())
print(df_attendance.to_json())
# Sum 'Hours Worked' by 'Name', including NaN as 0
# # Count rows for each Name, including NaN values in other columns
# name_count = df_attendance.groupby('Name').size().reset_index(name='Count')

# print(name_count)


# # print(df_attendance)
# # print(df_attendance.isna().sum())
# # df_attendance=df_attendance.ffill()
# # df_attendance=df_attendance.bfill()
# # df_attendance=df_attendance.dropna()

# # print(df_attendance['Punch In'].isna().sum())


# nan_count_by_name = df_attendance.groupby('Name')['Punch In'].apply(lambda x: x.isna().sum()).reset_index(name='NaN Count')

# print("Only Just Fill The TimeSheet\n",nan_count_by_name)
# # Remove rows with NaN in 'Punch In'
# df_attendance = df_attendance.dropna(subset=['Punch In']).reset_index(drop=True)

# print(df_attendance)
# # 

# df_attendance['Punch In'] = pd.to_datetime(df_attendance['Date'] + ' ' + df_attendance['Punch In'])
# df_attendance['Punch Out'] = pd.to_datetime(df_attendance['Date'] + ' ' + df_attendance['Punch Out'])

# print(df_attendance)
# # # Calculate total hours worked for each record
# df_attendance['Hours Worked'] = (df_attendance['Punch Out'] - df_attendance['Punch In']).dt.total_seconds() / 3600

# # print(df_attendance)
# # # Total hours worked by each employee
# # total_hours = df_attendance.groupby('Name')['Hours Worked'].sum().reset_index()
# # print(total_hours)
# # # # Average attendance (in hours) per day for each employee
# # avg_attendance = df_attendance.groupby('Name')['Hours Worked'].mean().reset_index()
# # print(avg_attendance)



# total_avg_hours = df_attendance.groupby('Name')['Hours Worked'].agg(
#     Total_Hours='sum',
#     Avg_Hours='mean',
#     Total_Day_In_Ofiice='count'
# ).reset_index()

# # total_avg_hours.to_csv('analysis_data.csv',index=False)

# name_total_days = name_count.set_index('Name')['Count']
# # print(name_total_days)
# total_avg_hours['Total Working Days']=total_avg_hours['Name'].map(name_total_days)

# # Calculate attendance percentage directly by mapping the total days
# total_avg_hours['Attendance_Percentage'] = (
#     total_avg_hours['Total_Day_In_Ofiice'] / total_avg_hours['Name'].map(name_total_days)
# ) * 100

# total_avg_hours['WFH'] = (
#     total_avg_hours['Name'].map(name_total_days)-total_avg_hours['Total_Day_In_Ofiice'] 
# ) 

# total_avg_hours.to_csv("wfh_report.csv",index=False)
# print(total_avg_hours)
# # print(total_avg_hours)
# # Filter rows where WFH is greater than 3
# wfh_df = total_avg_hours[total_avg_hours['WFH'] > 3][['Name', 'WFH']]

# # Save to CSV
# wfh_df.to_csv('wfh_employees.csv', index=False)

# print("Employees with more than 3 WFH days:")
# print(wfh_df)



