from SlackAPI.SlackMessageDispatcher import SlackMessageDispatcher
import requests

def get_birthdays_today(dispatcher):
    try:
        return requests.get("http://127.0.0.1:5000/birthdays/today").json()
    except Exception as e:
        print(f"Failed to get birthdays from API - {e}")
        send_message(f"An exception occurred while attempting to get birthdays.")
        return []

def send_message(dispatcher, message): 
    try:
        dispatcher.send_message(message)
    except Exception as e:
        print(f"Failed to send message - {e}")

def check_for_birthdays():
    slack_message_dispatcher = SlackMessageDispatcher()

    birthdays_today = get_birthdays_today(slack_message_dispatcher)
    
    for birthday in birthdays_today:
        send_message(slack_message_dispatcher, f"Happy Birthday {birthday}!")
            

check_for_birthdays()
# if __name__ == "__main__":
#     while True:
#         if datetime.datetime.now().hour == 9:
#             check_for_birthdays()