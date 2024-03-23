import datetime

# Get the current date and time
now = datetime.datetime.now()
print("Current date and time:", now)

# Create a specific date
date = datetime.date(2023, 6, 5)
print("Date:", date)

# Create a specific time
time = datetime.time(12, 30, 45)
print("Time:", time)

# Combine date and time into a datetime object
datetime_obj = datetime.datetime.combine(date, time)
print("Datetime object:", datetime_obj)

# Parse a date string
date_string = "2023-06-05"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
print("Parsed date:", parsed_date)

# Format a datetime object as a string
formatted_date = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date:", formatted_date)

# Calculate a duration of time using timedelta
duration = datetime.timedelta(days=5, hours=3)
print("Duration:", duration)
