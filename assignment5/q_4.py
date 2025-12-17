# Import the datetime module
import datetime

# Get current date and time
current_datetime = datetime.datetime.now()

# Display current date and time
print("Current Date and Time:", current_datetime)

# Get the day of the week
# weekday() returns 0 for Monday, 1 for Tuesday, ..., 6 for Sunday
day_of_week = current_datetime.strftime("%A")  # Full day name 

print("Day of the Week:", day_of_week)
