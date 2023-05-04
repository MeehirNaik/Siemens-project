import os
import win32com.client
import socket
import time
import hashlib

# Define the Python script that you want to schedule
python_script = "C:/Users/naikm/Downloads/Python Harry/sytemInfoStore/saveSerialNumber/bootTimeGetter.py"

# Define the interval time
interval_time = 43200  # 12 hours in seconds

# Define a unique identifier for the task
task_identifier = hashlib.sha256(python_script.encode()).hexdigest()

# Define the trigger conditions for the task
ip_changed = False
lan_changed = False
last_ip_address = ''
last_lan_address = ''
trigger = win32com.client.Dispatch('Schedule.Service').NewTrigger(task_identifier)

while True:
    # Get the current IP address
    current_ip_address = socket.gethostbyname(socket.gethostname())
    if current_ip_address != last_ip_address:
        ip_changed = True
        last_ip_address = current_ip_address

    # Get the current LAN address
    current_lan_address = str(os.system('ipconfig | findstr IPv4')).split(': ')[-1].strip()
    if current_lan_address != last_lan_address:
        lan_changed = True
        last_lan_address = current_lan_address

    # If the IP or LAN address has changed, or if the interval time has passed, schedule the task
    if ip_changed or lan_changed or trigger.Enabled == False:
        task_service = win32com.client.Dispatch('Schedule.Service')
        task_service.Connect()
        root_folder = task_service.GetFolder('\\')
        task_definition = task_service.NewTask(0)
        task_definition.RegistrationInfo.Description = 'My Python Script'

        # Create a trigger to run the task
        trigger.StartBoundary = time.strftime('%Y-%m-%dT%H:%M:%S')
        trigger.Enabled = True
        trigger.Repetition.Interval = f'PT{interval_time}S'
        trigger.Repetition.Duration = 'PT24H'
        task_definition.Triggers.Add(trigger)

        # Set the action to run the Python script
        task_action = task_definition.Actions.Create('C:\\Windows\\System32\\cmd.exe', f'/c python "{python_script}"')
        task_action.WorkingDirectory = os.path.dirname(python_script)

        # Register the task in the root folder
        registered_task = root_folder.RegisterTaskDefinition(
            task_identifier,  # Task identifier
            task_definition,  # Task definition
            6,                # Update the task if it already exists
            '',               # No user
            '',               # No password
            1,                # Run the task whether the user is logged in or not
        )

        # Reset the trigger conditions
        ip_changed = False
        lan_changed = False
        last_ip_address = current_ip_address
        last_lan_address = current_lan_address

    # Wait for the interval time to pass
    time.sleep(interval_time)
