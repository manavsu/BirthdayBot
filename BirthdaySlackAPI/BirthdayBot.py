from BirthdayBotAPI.BirthdayStore import BirthdayStore
from SlackAPI.SlackMessageDispatcher import SlackMessageDispatcher
import datetime

birthday_store = BirthdayStore()
slack_message_dispatcher = SlackMessageDispatcher()

birthdays_today = birthday_store.get_birthdays_today()
print(f"Birthdays today: {birthdays_today}")

for birthday in birthdays_today:
    message = f"Happy Birthday {birthday}!"
    slack_message_dispatcher.send_message(message)
