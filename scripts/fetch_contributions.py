import requests
import re
import json


USERNAME = "Karperash"

url = f"https://github.com/users/{USERNAME}/contributions"

html = requests.get(url).text


values = re.findall(
    r'data-level="(\d+)"',
    html
)


weeks = []
week = []


for value in values:

    week.append(int(value))

    if len(week) == 7:
        weeks.append(week)
        week = []


with open(
    "data/contributions.json",
    "w"
) as f:

    json.dump(
        {
            "weeks": weeks
        },
        f,
        indent=2
    )


print("Contribution data updated")