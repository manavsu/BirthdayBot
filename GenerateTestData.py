import random
from BirthdayBotAPI.BirthdayStore import BirthdayStore

days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
birthday_store = BirthdayStore()

for i in range(1000):
    name = f"Person{i + 1}"
    month = random.randint(1, 12)
    birthday_store.add_birthday(f"Person{i + 1}", month, random.randint(1, days_in_month[month]))
