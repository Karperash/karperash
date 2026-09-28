import requests
import json
from pathlib import Path


USERNAME = "Karperash"


url = f"https://github.com/users/{USERNAME}/contributions"


html = requests.get(url).text


days = []

start = html.find("<svg")

svg = html[start:]


# ищем количество вкладов
import re

values = re.findall(
    r'data-count="(\d+)"',
    svg
)


for value in values:
    days.append(int(value))


# GitHub отдаёт примерно 365 значений
# превращаем их в недели

weeks = []

week = []

for i, value in enumerate(days):

    week.append(
        min(value, 4)
    )

    if len(week) == 7:
        weeks.append(week)
        week = []


Path(
"data/contributions.json"
).write_text(
    json.dumps(
        {
        "weeks": weeks
        },
        indent=2
    )
)


print(
"Contributions updated"
)