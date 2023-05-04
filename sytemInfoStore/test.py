import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse("computer_info.xml")
root = tree.getroot()

# Find all computer elements and extract their values
for computer in root.findall("computer"):
    name = computer.find("name").text
    ip = computer.find("ip").text
    mac = computer.find("mac").text
    boot_time = computer.find("boot_time").text
    
    # Print the extracted values
    print(f"Name: {name}")
    print(f"IP: {ip}")
    print(f"MAC: {mac}")
    print(f"Boot Time: {boot_time}\n")