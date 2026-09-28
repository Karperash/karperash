from PIL import Image
from pathlib import Path


RAMP = "@%#*+=-:. "


img = Image.open("data/avatar.jpg")

img = img.convert("L")


width = 80
ratio = img.height / img.width
height = int(width * ratio * 0.45)

img = img.resize((width, height))


pixels = list(img.getdata())


ascii_lines = []

line = ""

for i, pixel in enumerate(pixels):

    char = RAMP[pixel * (len(RAMP)-1)//255]

    line += char

    if (i+1) % width == 0:
        ascii_lines.append(line)
        line = ""


svg_text = ""

y = 40

for index, line in enumerate(ascii_lines):

    svg_text += f"""
<text x="20"
y="{y}"
font-family="monospace"
font-size="8"
fill="#58a6ff">

{line}

<animate
attributeName="opacity"
from="0"
to="1"
begin="{index*0.05}s"
dur="0.4s"
fill="freeze"/>

</text>
"""

    y += 8



svg = f"""
<svg width="500"
height="450"
xmlns="http://www.w3.org/2000/svg">


<rect width="100%"
height="100%"
fill="#0d1117"/>


<text x="20"
y="25"
font-family="monospace"
font-size="16"
fill="#8b949e">

loading Karperash identity...

</text>


{svg_text}


</svg>
"""


Path("assets/avatar.svg").write_text(svg)

print("Animated avatar generated")