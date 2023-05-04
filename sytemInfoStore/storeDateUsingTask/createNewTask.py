import os
import sys
import win32com.client
import datetime

# Get the path to the Python interpreter and the Python script to run
python_path = sys.executable # use the system's default Python interpreter
script_path = r"C:\Users\naikm\Downloads\Python Harry\sytemInfoStore\storeDateUsingTask\createNewTask.py" # replace with your Python script's path

# Get the current date and time
now = datetime.datetime.now()
today_date = now.date()
start_time = datetime.time(12, 0, 0) # set the task to run at 12:00:00 AM and PM

# Create a task scheduler object
scheduler = win32com.client.Dispatch('Schedule.Service')
scheduler.Connect()

# Create a new task
root_folder = scheduler.GetFolder('\\')
task_name = 'My Python Task'
task_identifier = f'{{{os.getlogin()}}}\{task_name}'
task_exists = False
try:
    task = root_folder.GetTask(task_identifier)
    task_exists = True
except:
    task = scheduler.NewTask(0)

# Set the task settings
task.RegistrationInfo.Description = 'My Python Task Description'
task.Settings.Enabled = True
task.Settings.Hidden = False
task.Settings.AllowDemandStart = True
task.Settings.StopIfGoingOnBatteries = False

# # Set the task trigger to run every day at 12:00:00 AM and PM
# trigger = task.Triggers.Create(TriggerType=3) # daily trigger
# trigger.StartBoundary = f'{today_date}T{start_time}'
# trigger.DaysInterval = 1 # run every 1 day
# trigger.ExecutionTimeLimit = 'PT1H' # limit the task to run for 1 hour
# trigger.Enabled = True

# trigger = task.Triggers.Create(Type=3)  # DailyTrigger
# trigger.StartBoundary = f'{today_date}T{start_time}'
# # trigger.DaysInterval = 1  # Run every 1 day
# trigger.Enabled = True

# # Set the task action to run the Python script
# action = task.Actions.Create(Type=0)
# action.Path = python_path
# action.Arguments = f'"{script_path}"'

# Save the task
if task_exists:
    root_folder.RegisterTaskDefinition(task_identifier, task, flags=6) # update the existing task
    print(f'Task "{task_name}" has been updated.')
else:
    root_folder.RegisterTaskDefinition(task_name, task) # create a new task
    print(f'Task "{task_name}" has been created.')
