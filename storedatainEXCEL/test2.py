# import os
# import openpyxl

# file_path = "C:\\Users\\naikm\\Downloads\\test1\\"

# new_dir_path = "C:\\Users\\naikm\\Downloads\\test1\\"

# # check if the directory exists, and create it if it doesn't
# if not os.path.exists(new_dir_path):
#     os.makedirs(new_dir_path)
# else:
#     wb = openpyxl.Workbook()
#     wb.save(file_path + "new_workbook.xlsx")

# # specify the path to the new file
# new_file_path = os.path.join(new_dir_path, 'new_workbook.xlsx')

# print(file_path + "new_workbook.xlsx")
# wb = openpyxl.load_workbook(file_path + "new_workbook.xlsx")
# ws = wb.active
# wb.save(file_path + "new_workbook.xlsx")

import xlsxwriter
file_path = "C:\\Users\\naikm\\Downloads\\test1\\"

print(file_path[-6:-2])

# Create new file and add data
# workbook = xlsxwriter.Workbook(file_path + "test.xlsx")
# worksheet = workbook.add_worksheet()
# workbook.close()
# print("Data saved successfully.")

