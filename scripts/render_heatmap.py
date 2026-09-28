import json
from pathlib import Path


data = json.loads(
    Path("data/contributions.json").read_text()
)


colors = [
    "#161b22",
    "#0e4429",
    "#006d32",
    "#26a641",
    "#39d353"
]


svg = """
<svg width="900"
height="180"
xmlns="http://www.w3.org/2000/svg">

<rect width="900"
height="180"
fill="#0d1117"/>
"""


size = 14
gap = 5


for x, week in enumerate(data["weeks"]):

    for y, value in enumerate(week):

        svg += f"""
<rect
x="{40+x*(size+gap)}"
y="{40+y*(size+gap)}"
width="{size}"
height="{size}"
rx="3"
fill="{colors[min(value,4)]}"/>
"""


delay = (x * 7 + y) * 0.03

svg += f"""
<rect
x="{40 + x*(size+gap)}"
y="{50 + y*(size+gap)}"
width="{size}"
height="{size}"
rx="3"
fill="{colors[min(value,4)]}"
opacity="0">

<animate
attributeName="opacity"
from="0"
to="1"
begin="{delay}s"
dur="0.5s"
fill="freeze"/>

</rect>
"""


Path(
"assets/contribution.svg"
).write_text(svg)


print("Heatmap created")