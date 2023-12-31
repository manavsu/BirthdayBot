import requests
import json
import logging


class SlackMessageDispatcher:
    def __init__(self):
        WebHook_URL_Location = "config/WebHookURL.txt"
        with open(WebHook_URL_Location, "r") as webhook_url_file:
            self.Webhook_URL = webhook_url_file.read()

    def send_message(self, message):
        payload = {"text": message}
        headers = {"Content-Type": "application/json"}

        response = requests.post(
            self.Webhook_URL, data=json.dumps(payload), headers=headers
        )

        if response.status_code == 200:
            print(f"Message : {message} - Sent successfully")
        else:
            print(f"Failed to send Message : {message} - {response.status_code}")
