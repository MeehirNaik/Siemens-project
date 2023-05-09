####	 Data Retrieval and Storing Python Program   ####

This Python exe retrieves system information and also retrives data from a XML file named AUTOMAT.xml. Data is than stored in a specified destination in a EXCEL file.


####	 note:   ####

1. need to setup windows task sheduler with the steps provided below in TaskShedularSteps.
2. For searching through dat you can use GUI which can be accessed by running the PcInfoGUI.exe.


####	 TaskShedularSteps   ####

here are the steps to create a task scheduler task that triggers every day at 12am and 12pm or if a new IP address is assigned to pc or  PC is unlocked.

1. Open the Task Scheduler by searching for it in the Start Menu or pressing Windows+R and typing `taskschd.msc`.
2. In the Task Scheduler, click on "Create Task" in the "Actions" panel on the right-hand side.
3. Give the task a name and description in the "General" tab.
4. In the "Triggers" tab, click "New" to create a new trigger.
5. Set the trigger to "Daily" and set the "Start" time to 12:00 AM. Check the "Repeat task every" box and set it to 12 hours. Make sure "Enabled" is checked.
6. In the "Actions" tab, click "New" to create a new action.
7. Set the action to "Start a program" and in the "Program/script" field, enter the path to the Python executable (e.g. `C:\Python39\python.exe`). In the "Add arguments" field, enter the path to your Python script that retrieves the IP address and checks if the PC is unlocked or logged in when it's locked.
8. In the "Conditions" tab, check the "Start only if the following network connection is available" box and select the network connection you want to use.
9. Check the "Stop if the computer switches to battery power" box.
10. In the "Settings" tab, check the "Allow task to be run on demand" box.
11. Click "OK" to create the task.


#### 	 Usage:   ####

To run the program, simply run exe file:


####	 Output:   ####

The program will output the following files:

SystemInfo.xlsx: The retrieved data, in excel format (if destination is a file path).
temp.txt: temp file is used to store data if the data can't be stored or can't accessed in Systeminfo.xlsx.


####	 Acknowledgments:	 ####

This program was developed by Meehir Naik - Apprentice - MAY 2023.
