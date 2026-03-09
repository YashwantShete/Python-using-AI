#Water Drinking Reminder

import time
from plyer import notification

def water_reminder(interval_minutes):
    # Convert minutes to seconds
    interval_seconds = interval_minutes * 60

    print("Water Drinking Reminder Started!")
    print(f"You will get a notification every {interval_minutes} minutes.\n")

    # Infinite loop to keep the reminder running
    while True:
        # Wait for the specified interval
        time.sleep(interval_seconds)
        
        # Trigger the desktop notification
        notification.notify(
            title="Drink Water",
            message="Time to drink a glass of water and stay hydrated.",
            app_name="Hydration Reminder",
            timeout=10
        )

# Standard boilerplate to run the script
if __name__ == "__main__":
    # Start the reminder with a 30-minute interval
    water_reminder(30)