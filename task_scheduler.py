import schedule
import time
import logging
import sys

# Configure logging to include timestamp
logging.basicConfig(filename='task_scheduler.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def send_email():
    """Simulated email sending function with detailed logging."""
    try:
        # Simulate sending an email
        logging.info("Attempting to send email...")
        # Replace with real email sending logic if needed
        logging.info("Simulated email sent successfully!")
    except Exception as e:
        logging.error(f"Error occurred while sending email: {e}")

def schedule_tasks(run_time="10:00"):
    """Schedule tasks at the specified time."""
    try:
        logging.info(f"Scheduling email task to run daily at {run_time}.")
        schedule.every().day.at(run_time).do(send_email)

        while True:
            schedule.run_pending()
            time.sleep(1)
    except schedule.ScheduleValueError as e:
        logging.error(f"Invalid time format for scheduling: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    try:
        # Allow user to pass a custom schedule time via command-line or default to 10:00
        run_time = sys.argv[1] if len(sys.argv) > 1 else "10:00"
        logging.info(f"Starting the task scheduler. Scheduled time: {run_time}")
        schedule_tasks(run_time)
    except KeyboardInterrupt:
        logging.info("Scheduler stopped by user (KeyboardInterrupt).")
        sys.exit(0)


