import json
import datetime
import threading

class BirthdayRegistry:
    BirthdayLocation = 'BirthdayReminder/BirthdayWebAPI/BirthdaysTestData.json'
    Lock = threading.Lock()

    def __init__(self):
        with self.Lock:
            with open(self.BirthdayLocation, "r") as birthday_file:
                birthdays = json.load(birthday_file)
                self.birthdays = {name: Birthday.from_json(birthdays[name]) for name in birthdays}

    def add_birthday(self, name, month, day):
        with self.Lock:
            self.birthdays[name] = Birthday(month, day)
            self.write_to_store()

    def get_birthdays_today(self):
        with self.Lock:
            return [name for name in self.birthdays if self.birthdays[name] == datetime.date.today()]
    
    def get_all_birthdays(self):
        with self.Lock:
            return self.birthdays
    
    def write_to_store(self):
        with self.Lock:
            with open(self.BirthdayLocation, "w") as birthday_file:
                json.dump({name:self.birthdays[name].to_json() for name in self.birthdays}, birthday_file, indent=4)

    def to_json(self):
        with self.Lock:
            return json.dumps({name:self.birthdays[name].to_json() for name in self.birthdays}, indent=4)

class Birthday:
    def from_json(json):
        return Birthday(json["month"], json["day"])
    
    def __init__(self, month, day):
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.day}/{self.month}"

    def to_json(self):
        return {"month": self.month, "day": self.day}

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Birthday):
            return self.month == __value.month and self.day == __value.day
        if isinstance(__value, datetime.date):
            return self.month == __value.month and self.day == __value.day
        return False