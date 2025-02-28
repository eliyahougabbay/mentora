# src/main.py
import time
from src.celery_app import app
from src.tasks import run_mentora


if __name__ == "__main__":
    while True:
        try:
            user_input = input("What subject would you like to learn? ").strip()
            if not user_input:
                print("No input provided. Please enter a subject.")
                continue
            print("Processing...")
            response = run_mentora.delay(user_input)
        except Exception as e:
            print("An error occurred:", e)
            # Optionally, pause briefly before continuing
            time.sleep(3)
