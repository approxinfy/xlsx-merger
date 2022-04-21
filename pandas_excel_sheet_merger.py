import pandas as pd 
input_workbook_path = 'C:\\Users/kvrks/Documents/playground/Sales_dummy.xlsx'
output_workbook_path = 'C:\\Users/kvrks/Documents/playground/output.xlsx'
# Merging all sheets from input_workbook to a dataframe
data_frame = pd.concat(pd.read_excel(input_workbook_path, sheet_name=None), ignore_index=True)
# Writing created dataframe to putput_workbook
data_frame.to_excel(output_workbook_path)