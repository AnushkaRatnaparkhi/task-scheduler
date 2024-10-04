import schedule
import time
import logging

# Configure logging
logging.basicConfig(filename='task_scheduler.log', level=logging.INFO)

def send_email():
    # Simulated email sending function
    logging.info("Simulated email sent!")

def schedule_tasks():
    schedule.every().day.at("10:00").do(send_email)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    schedule_tasks()

