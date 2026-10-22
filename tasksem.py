"""filepath = "abc123.txt"
rows = 0
words = 0
symbols = 0
m_len = 0
min_n = None
max_n = 0
summ = 0
count = 0
with open(filepath, "r") as file:
    for r in file:
        try:
            n = int(r)
            min_n = n if min_n is None else min(n, min_n)
            max_n = max(n, max_n)
            summ += n
            count += 1
        except ValueError:
            pass

avg = summ/count
import csv
scores = []
groups = {}
best_student = ""
max_s = -1
with open("abc.csv") as file:
    r = csv.DictReader(file)
    for row in r:
        if row["score"] in groups:
            groups[row["group"]].append(int(row["score"]))
        else:
            groups[row["group"]] = [int(row["score"])]

        scores.append(int(row["score"]))

        if int(row["score"]) > max_s:
            max_s = int(row["score"])
            best_student = row["name"]


for value in groups.values():
    print(sum(value)/len(value))

print(sum(scores)/len(scores))
print(best_student)

"""
#задачи до 3, показывал на семинарах

"""
import csv
filepath = "abc.csv"
writepath = "abc2.csv"
data = []
with open(filepath) as file:
    r = csv.reader(file)
    data.append(next(r))
    for row in r:
        if int(row[2]) > 100:
            data.append(row)
with open(writepath, "w") as file:
    for row in data:
        file.write(row[0]+","+row[1]+","+row[2]+"\n")"""

""" 
writepath = "test_data/students2.json"
filepath = "test_data/students.json"
import json

with open(filepath) as file:
    data = json.load(file)

best_student = []
best_score = 0

for s in data:
    if s["score"] >= 60:
        s["passed"] = True
        if best_score < s["score"]:
            best_score = s["score"]
            best_student = s
    else:
        s["passed"] = False

with open(writepath, "w") as file:
    json.dump(data, file)
"""

"""
def parse_number(value):
    for i in range(len(value)):
        if i == 0:
            if value[i] not in "+-0123456789":
                raise ValueError
        else:
            if value[i] not in "0123456789":
                raise ValueError
    return int(value)

try:
    print(parse_number("+1982"))
    print(parse_number("728"))
    print(parse_number("-2198"))
    print(parse_number("892nb"))
except ValueError:
    print("not a number")"""

"""
class BankError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class InvalidAmountError(BankError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class InsufficientFundsError(BankError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class AccountBlockedError(BankError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

def withdraw(balance, amount):
    if amount <= 0:
        raise InvalidAmountError
    if balance - amount < 0:
        raise InsufficientFundsError
    return balance - amount
"""
"""
import re

with open("test_data/errors.txt") as file:
    data = file.readlines()

errs = []
ids = []
ids_err = []
mask = r"ERROR"
mask2 = r"[0-9]+"
for err in data:
    match = re.search(mask2, err)
    if match:
        result = match.group()
        ids.append(result)    
    if re.search(mask, err):
        errs.append(err)
        ids_err.append(result)

print(ids, errs, ids_err)
"""
"""
import re

with open("test_data/emails.txt") as file:
    for row in file:
        if re.match(r"\w+@+\w+.+\w", row):
            print(row)"""
"""
from datetime import datetime

class Timer():
    start = datetime.now()
    def __enter__(self):
        self.start = datetime.now()
        return self

    def __exit__(self, exc_type, exc, tb):
        print(datetime.now() - self.start)
        return False

def wait():
    for i in range(999999):
        pass

with Timer():
    wait()
"""
"""
from contextlib import contextmanager
from datetime import datetime

@contextmanager
def timer():
    start = datetime.now()
    try:
        yield None
    finally:
        print(datetime.now() - start)

with timer():
    for i in range(999999):
        pass"""

"""
import re

data = [0, 0, 0]
users = []
with open("test_data/errors2.txt") as file:
    masks = [r"ERROR", r"WARNING", r"INFO"]
    mask2 = r"\s\d+\s" # type: ignore
    for row in file:
        for i in range(len(masks)):
            if re.search(masks[i], row):
                data[i] += 1
                if i == 0:
                    num = re.search(mask2, row)
                    users.append(int(num.group()))

print("INFO: ", data[2])
print("WARNING: ", data[1])
print("ERROR: ", data[0])
print(users)
"""
"""

summ = 0
min_n = float("inf")
max_n = 0
count = 0
avg = 0

with open("test_data/dataset.txt") as file:
    for row in file:
        count += 1
        n = int(row)
        min_n = min(min_n, n)
        max_n = max(max_n, n)
        summ += n

avg = summ/count

print(summ,min_n,max_n,count,avg)"""

"""
import re

ip_mask = r"\s\d+.\d+.\d+.\d+" # type: ignore
http_mask = r"\s[A-Z]+\s" # type: ignore
url_mask = r"(^\/[a-zA-Z]+)+" # type: ignore
with open("test_data/access.log") as file:
    for row in file:
        ip = re.search(ip_mask, row).group()
        http = re.search(http_mask, row).group()
        url = re.search(url_mask, row).group()
        print(url)"""

"""
nums = "+7 999 123-45-67 8 999 123-45-67 +7 (999) 123-45-67 8 (999) 123-45-67"
import re
mask = r"[+]*[78]\s[(]*\d+[)]*\s\d+-\d+-\d+" # type: ignore
print(re.findall(mask, nums))"""

"""
import re
text = "Встречи состоятся 15.09.2026, 21.09.2026 и 03.10.2026. Следующая встреча запланирована на 1.11.2026."
mask = r"\d+.\d+.\d+" # type: ignore
print(re.findall(mask, text))"""

"""
import re

def is_valid_login(login:str):
    if 4 <= len(login) <= 16:
        if login[0].lower() in "qwertyuiopasdfghjklzxcvbnm":
            mask = r"([a-zA-Z0-9_]+)+"
            if re.search(mask, login).group() == login:
                return True
    return False

logins = ["user_123", "admin", "123user", "ab", "user-name", "very_long_username"]

for l in logins:
    print(is_valid_login(l))"""

"""
text = "Полезные сайты: https://python.org, http://example.com/page, https://example.com/docs/index.html и ftp://files.example.com/data."

import re

mask = r"http[s]*://[a-z./]+"
print(re.findall(mask, text))"""

"""
import re
text = "   Текст   с   пробелами   "
result = ""
mask = r"[ ]*[эйцукенгшщзфывапролджячсмитьбюЭЙЦУКЕНГШЩЗФЫВАПРОЛДЖЯЧСМИТЬБЮ.]+[ ]*"
for w in re.findall(mask, text):
    result += w.strip() + " "
print(result)"""
