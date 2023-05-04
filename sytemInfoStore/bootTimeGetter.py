import socket
import uuid
import xml.etree.ElementTree as ET
import subprocess

sNumber = 154

# Run the systeminfo command in the command prompt and capture the output asynchronously
process = subprocess.Popen(['systeminfo'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Wait for the command to complete and get the output
stdout, stderr = process.communicate()

# Decode the output to a string
output = stdout.decode()

# Extract the system boot time from the output using string manipulation
start_index = output.find('System Boot Time:') + len('System Boot Time:')
end_index = output.find('\n', start_index)
boot_time = output[start_index:end_index]

# Print the boot time to the terminal
print('System boot time:', boot_time)

# Get the hostname of the computer
hostname = socket.gethostname()

# Get the IP address of the computer
ip_address = socket.gethostbyname(hostname)

# Get the MAC address of the computer
mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1])

# Create a new computer element with sub-elements for the hostname, IP address, and MAC address
computer = ET.Element('computer')
serialNumber = ET.SubElement(computer, 'serialNumber')
serialNumber.text = str(sNumber)
name = ET.SubElement(computer, 'name')
name.text = hostname
ip = ET.SubElement(computer, 'ip')
ip.text = ip_address
mac = ET.SubElement(computer, 'mac')
mac.text = mac_address
boot_time_elem = ET.SubElement(computer, 'boot_time')
boot_time_elem.text = boot_time

# Check if the XML file already exists
try:
    tree = ET.parse('computer_info.xml')
    root = tree.getroot()
except:
    # If it doesn't, create a new root element and add the new computer element to it
    root = ET.Element('computers')
    tree = ET.ElementTree(root)
    raise
root.append(computer)

# Write the updated XML document to the file
tree.write('computer_info.xml', xml_declaration=True, encoding='utf-8', method="xml", short_empty_elements=False)