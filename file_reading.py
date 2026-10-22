"""
задачи на чтение файлов
                        """
filepath = "test_data/abc123.txt"
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
"""
with open("test_data/abc.csv") as file:
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

import csv
filepath = "test_data/abc.csv"
writepath = "test_data/abc2.csv"
data = []
with open(filepath) as file:
    r = csv.reader(file)
    data.append(next(r))
    for row in r:
        if int(row[2]) > 100:
            data.append(row)
with open(writepath, "w") as file:
    for row in data:
        file.write(row[0]+","+row[1]+","+row[2]+"\n")

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

print(summ,min_n,max_n,count,avg)

import re
import json
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

ip_mask = r"\b\d{1,3}(?:\.\d{1,3}){3}\b"
http_mask = r"\b(GET|POST)\b"
url_mask = r"\b(GET|POST)\s+(/\S+)"
status_mask = r"\b\d{3}\b"
ip_count = {}
http_count = {}
url_count = {}
status_count = {}

with open("test_data/access.log", "r", encoding="utf-8") as file:
    for row in file:
        ip_match = re.search(ip_mask, row)
        http_match = re.search(http_mask, row)
        url_match = re.search(url_mask, row)
        status_match = re.search(status_mask, row)
        ip = ip_match.group() # type: ignore
        http = http_match.group() # type: ignore
        url = url_match.group(2) # type: ignore
        status = status_match.group() # type: ignore
        ip_count[ip] = ip_count.get(ip, 0) + 1
        http_count[http] = http_count.get(http, 0) + 1
        url_count[url] = url_count.get(url, 0) + 1
        status_count[status] = status_count.get(status, 0) + 1
        logging.info("обработан запрос: IP=%s, HTTP=%s, URL=%s, STATUS=%s", ip, http, url, status)

total_requests = sum(http_count.values())
total_errors = sum(count for status, count in status_count.items() if status.startswith("4"))
most_frequent_url = None
max_count = 0
for url, count in url_count.items():
    if count > max_count:
        max_count = count
        most_frequent_url = url

statistics = {
    "total_requests": total_requests,
    "requests_by_ip": ip_count,
    "requests_by_method": http_count,
    "requests_by_status": status_count,
    "requests_by_url": url_count,
    "total_4xx_errors": total_errors,
    "most_frequent_url": most_frequent_url
}

with open("test_data/statistics.json", "w", encoding="utf-8") as file:
    json.dump(statistics, file, ensure_ascii=False, indent=4)

logging.info("статистика сохранена в statistics.json")
