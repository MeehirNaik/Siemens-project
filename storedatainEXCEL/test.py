import wmi
import socket
import uuid
from datetime import datetime
import os
import re
import psutil
import xlsxwriter

# Get system boot time
boot_time_timestamp = psutil.boot_time()
boot_time = datetime.fromtimestamp(boot_time_timestamp).strftime("%Y-%m-%d %H:%M:%S")
print(f"System boot time: {boot_time}")

# Get system information
system = wmi.WMI()
serial_number = system.Win32_BIOS()[0].SerialNumber.strip()
host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)
print(ip_address)
mac_address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
print(mac_address)
mac_address1 = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1])
print(mac_address1)

# Get current date and time
now = datetime.now()

# Convert to string format
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

# Check if system_info.xlsx file exists
if os.path.exists("system_info.xlsx"):
    # Load the workbook
    workbook = xlsxwriter.Workbook("system_info.xlsx")
    worksheet = workbook.add_worksheet()

    # Check if temp.txt file exists and can be uploaded
    if os.path.exists("temp.txt"):
        with open("temp.txt", "r") as f:
            text = f.read()
            print(text)
            for line in text.split('\n'):
                try:
                    # Append data to existing file
                    row = line.strip().split(",")
                    worksheet.write_row(worksheet.dim_rowmax, 0, row)
                    print("Temp data uploaded successfully!")
                except:
                    print("Temp data cannot be uploaded at this moment.")

    # Append present data to existing file
    try:
        row = [serial_number, host_name, ip_address, mac_address, boot_time, timestamp]
        worksheet.write_row(worksheet.dim_rowmax, 0, row)
        workbook.close()
        print(f"Data saved successfully: {row}")

        # Delete the temp file
        try:
            os.remove("temp.txt")
        except:
            print("temp not present")
    except:
        # Create new temp file and add data to it
        print("im in EXEPT")

        with open("temp.txt", "a") as k:
            k.write(f"\n{serial_number},{host_name},{ip_address},{mac_address},{boot_time},{timestamp}")
        print("Data added to temp file for later upload.")
else:
    # Create new file and add data
    workbook = xlsxwriter.Workbook("system_info.xlsx")
    worksheet = workbook.add_worksheet()
    worksheet.write_row(0, 0, ['Serial Number', 'Host Name', 'IP Address', 'MAC Address', 'Boot Time','Time'])
    row = [serial_number, host_name, ip_address, mac_address, boot_time, timestamp]
    worksheet.write_row(1, 0, row)
    workbook.close()
    print("Data saved successfully.")

try:
    # Open the workbook and select the worksheet
    workbook = xlsxwriter.Workbook('system_info.xlsx')
    worksheet = workbook.add_worksheet()

    # Get the maximum number of rows in the worksheet
    max_row = worksheet.dim_rowmax

    # Iterate over the rows in the worksheet
    for row in range(max_row, -1, -1):
        # Check if all cells in the row are empty
        if not worksheet.row_values(row):
            # Delete the row
            worksheet.delete_row(row)

    # Save the workbook
    workbook.close()
    
except:
    print("can't remove spaces")
