# log_analyzer
Script to make analyzing logs easier especially when there are many logs and many different events

The script takes start and end date/time and then extracts those portions from a set of logs and orders them sequentially by log name

Features

Directory Input: Specify the path where your log files are stored

Time Range Selection: Input start and end times in HH:MM:SS format

Sequential Output: Logs are processed and displayed in order (Log1, Log2, etc.)

Time Filtering: Only entries within the specified time range are shown


Customization Notes

Log Format: The script currently looks for timestamps in HH:MM:SS format. If your logs use a different format:

Modify the regex pattern in re.search(r'(\d{2}:\d{2}:\d{2})', line)

Update the datetime parsing format in datetime.strptime()

File Selection: The script looks for files ending with '.log' or starting with 'Log'. Adjust the file filtering as needed.


Date+Time Support:

Accepts input in YYYY-MM-DD HH:MM:SS format

Properly compares both date and time components


Flexible Log Parsing:

First tries to match full datetime stamps (2023-01-15 10:00:56)

Falls back to time-only format (using the input date as reference)


Run: python3 log_analyzer_datetime.py

Inputs:

Path to log files

Start datetime (e.g., 2023-06-15 10:00:56)

End datetime (e.g., 2023-06-15 10:14:13)
