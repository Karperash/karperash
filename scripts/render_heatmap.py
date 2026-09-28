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


svg += """

<text x="40"
y="25"
fill="#58a6ff"
font-family="monospace"
font-size="18">

Karperash activity

</text>

</svg>
"""


Path(
"assets/contribution.svg"
).write_text(svg)


print("Heatmap created")