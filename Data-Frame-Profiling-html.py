from pandas_profiling import ProfileReport
profile = ProfileReport(df)
profile.to_file(output_file='RTU-Processed-Profile.html')