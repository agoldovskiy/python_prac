"""
задачи на регулярки
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


import re

with open("test_data/emails.txt") as file:
    for row in file:
        if re.match(r"\w+@+\w+.+\w", row):
            print(row)

import re

data = [0, 0, 0]
users = []
with open("test_data/errors2.txt") as file:
    masks = [r"ERROR", r"WARNING", r"INFO"]
    mask2 = r"\s\d+\s"
    for row in file:
        for i in range(len(masks)):
            if re.search(masks[i], row):
                data[i] += 1
                if i == 0:
                    num = re.search(mask2, row)
                    users.append(int(num.group())) # type: ignore

print("INFO: ", data[2])
print("WARNING: ", data[1])
print("ERROR: ", data[0])
print(users)

nums = "+7 999 123-45-67 8 999 123-45-67 +7 (999) 123-45-67 8 (999) 123-45-67"
import re
mask = r"[+]*[78]\s[(]*\d+[)]*\s\d+-\d+-\d+"
print(re.findall(mask, nums))


import re
text = "Встречи состоятся 15.09.2026, 21.09.2026 и 03.10.2026. Следующая встреча запланирована на 1.11.2026."
mask = r"\d\d.\d\d.\d\d\d\d"
print(re.findall(mask, text))


import re

def is_valid_login(login:str):
    if 4 <= len(login) <= 16:
        if login[0].lower() in "qwertyuiopasdfghjklzxcvbnm":
            mask = r"([a-zA-Z0-9_]+)+"
            if re.search(mask, login).group() == login: # type: ignore
                return True
    return False

logins = ["user_123", "admin", "123user", "ab", "user-name", "very_long_username"]

for l in logins:
    print(is_valid_login(l))


text = "Полезные сайты: https://python.org, http://example.com/page, https://example.com/docs/index.html и ftp://files.example.com/data."

import re

mask = r"http[s]*://[a-z./]+"
print(re.findall(mask, text))


import re
text = "   Текст   с   пробелами   "
result = ""
mask = r"[ ]*[эйцукенгшщзфывапролджячсмитьбюЭЙЦУКЕНГШЩЗФЫВАПРОЛДЖЯЧСМИТЬБЮ.]+[ ]*"
for w in re.findall(mask, text):
    result += w.strip() + " "
print(result)
