import numpy as np
from bokeh.plotting import figure, output_file, show

N = 1000
x = np.random.random(size=N) * 100
y = np.random.random(size=N) * 100
radii = np.random.random(size=N) * 1.5

colors = [
    "#%02x%02x%02x" % (int(r), int(g), 150) for r, g in zip(50 + 2 * x, 30 + 2 * y)
]

output_file("scatter_with_cdn.html", title="scatter_with_cdn example", mode="cdn")

TOOLS = "crosshair, pan, wheel_zoom, box_zoom, reset, box_select, lasso_select, save"

p = figure(tools=TOOLS, x_range=(0, 100), y_range=(0, 100))

p.circle(x, y, radius=radii, fill_color=colors, fill_alpha=0.6, line_color=None)

show(p)