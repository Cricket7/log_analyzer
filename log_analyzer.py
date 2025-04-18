import os
import re
from datetime import datetime

def parse_logs(directory, start_datetime, end_datetime):
    """
    Analyzes log files in the specified directory and extracts entries between start_datetime and end_datetime.
    
    Args:
        directory (str): Path to directory containing log files
        start_datetime (str): Start datetime in YYYY-MM-DD HH:MM:SS format
        end_datetime (str): End datetime in YYYY-MM-DD HH:MM:SS format
    """
    # Convert datetime strings to datetime objects
    datetime_format = "%Y-%m-%d %H:%M:%S"
    start_dt = datetime.strptime(start_datetime, datetime_format)
    end_dt = datetime.strptime(end_datetime, datetime_format)
    
    # Get all log files in directory
    log_files = [f for f in os.listdir(directory) if f.endswith('.log') or f.startswith('Log')]
    log_files.sort()  # Sort alphabetically (Log1, Log2, etc.)
    
    # Process each log file
    for log_file in log_files:
        log_path = os.path.join(directory, log_file)
        print(f"\n=== {log_file} ({start_datetime} to {end_datetime}) ===")
        
        with open(log_path, 'r') as f:
            for line in f:
                # Extract datetime from log line (adjust regex as needed)
                datetime_match = re.search(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})', line)
                if not datetime_match:
                    # Try alternative format without date (use date from previous line)
                    time_match = re.search(r'(\d{2}:\d{2}:\d{2})', line)
                    if time_match:
                        # Use date from start_datetime (fallback)
                        log_time_str = f"{start_dt.date()} {time_match.group(1)}"
                        datetime_match = re.search(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})', log_time_str)
                
                if datetime_match:
                    log_datetime_str = datetime_match.group(1)
                    try:
                        log_dt = datetime.strptime(log_datetime_str, datetime_format)
                        
                        # Check if datetime is within specified range
                        if start_dt <= log_dt <= end_dt:
                            print(line.strip())
                    except ValueError:
                        # Skip lines with invalid timestamps
                        continue

def validate_datetime(input_str):
    """Validate datetime format (YYYY-MM-DD HH:MM:SS)"""
    try:
        datetime.strptime(input_str, "%Y-%m-%d %H:%M:%S")
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    print("Log Analyzer - Extract entries by date and time range")
    print("----------------------------------------------------")
    
    # Get user input
    log_dir = input("Enter path to log files: ").strip()
    
    while True:
        start_input = input("Enter start datetime (YYYY-MM-DD HH:MM:SS): ").strip()
        if validate_datetime(start_input):
            break
        print("Invalid format. Please use YYYY-MM-DD HH:MM:SS")
    
    while True:
        end_input = input("Enter end datetime (YYYY-MM-DD HH:MM:SS): ").strip()
        if validate_datetime(end_input):
            break
        print("Invalid format. Please use YYYY-MM-DD HH:MM:SS")
    
    # Validate directory exists
    if not os.path.isdir(log_dir):
        print(f"Error: Directory not found: {log_dir}")
        exit(1)
    
    # Validate time range
    start_dt = datetime.strptime(start_input, "%Y-%m-%d %H:%M:%S")
    end_dt = datetime.strptime(end_input, "%Y-%m-%d %H:%M:%S")
    
    if start_dt > end_dt:
        print("Error: Start datetime must be before end datetime")
        exit(1)
    
    # Process logs
    parse_logs(log_dir, start_input, end_input)