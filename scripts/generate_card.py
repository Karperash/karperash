from pathlib import Path


name = "Karperash"
role = "AI Engineer"
skills = [
    "Python",
    "PHP",
    "Generative AI"
]


lines = []

lines.append("$ whoami")
lines.append("")
lines.append(name)
lines.append("")
lines.append("$ skills")
lines.append("")

for skill in skills:
    lines.append(skill)


text_elements = ""

y = 90

for line in lines:
    text_elements += f"""
<text x="40" y="{y}"
font-family="monospace"
font-size="20"
fill="#c9d1d9">
{line}
</text>
"""
    y += 35


svg = f"""
<svg width="700" height="350"
xmlns="http://www.w3.org/2000/svg">

<rect width="700" height="350"
rx="15"
fill="#0d1117"/>

{text_elements}

</svg>
"""


Path("assets/info-card.svg").write_text(svg)

print("Generated info-card.svg")