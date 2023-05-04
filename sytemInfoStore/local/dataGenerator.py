import random
import string
import xml.etree.ElementTree as ET
import datetime
import os

def random_serial():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

def random_ip():
    return '.'.join(str(random.randint(0, 255)) for _ in range(4))

def random_mac():
    return ':'.join('{:02x}'.format(random.randint(0, 255)) for _ in range(6))

def random_hostname():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

def random_boot_time():
    return str(datetime.datetime.now())

if not os.path.exists("data"):
    os.makedirs("data")

for i in range(10):
    serial_number = random_serial()
    # serial_number = "A1WMQTKE72"
    ip_address = random_ip()
    mac_address = random_mac()
    hostname = random_hostname()
    boot_time = random_boot_time()
    read_time = str(datetime.datetime.now())  # add a read_time element

    filename = serial_number + ".xml"
    file_path = os.path.join("data", filename)

    root = ET.Element("Computer")
    sys_info = ET.SubElement(root, "SystemInfo")
    sys_info.set("SerialNumber", serial_number)

    serial = ET.SubElement(sys_info, "SerialNumber")
    serial.text = serial_number

    ip = ET.SubElement(sys_info, "IPAddress")
    ip.text = ip_address

    mac = ET.SubElement(sys_info, "MACAddress")
    mac.text = mac_address

    host = ET.SubElement(sys_info, "HostName")
    host.text = hostname

    boot = ET.SubElement(sys_info, "BootTime")
    boot.text = boot_time

    read = ET.SubElement(sys_info, "ReadTime")
    read.text = read_time  # set the read_time element to the current time

    if os.path.isfile(file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()

        sys_info = ET.SubElement(root, "SystemInfo")
        sys_info.set("SerialNumber", serial_number)

        serial = ET.SubElement(sys_info, "SerialNumber")
        serial.text = serial_number

        ip = ET.SubElement(sys_info, "IPAddress")
        ip.text = ip_address

        mac = ET.SubElement(sys_info, "MACAddress")
        mac.text = mac_address

        host = ET.SubElement(sys_info, "HostName")
        host.text = hostname

        boot = ET.SubElement(sys_info, "BootTime")
        boot.text = boot_time

        read = ET.SubElement(sys_info, "ReadTime")
        read.text = read_time  # set the read_time element to the current time

        tree.write(file_path)
    else:
        tree = ET.ElementTree(root)
        tree.write(file_path)
