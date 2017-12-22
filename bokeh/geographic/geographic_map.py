import numpy as np
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.tile_providers import WMTSTileSource

USA = x_range, y_range = ((-13884029, -7453304), (2698291, 6455972))

output_file("geographic_map.html", mode="inline")

p = figure(tools='pan, wheel_zoom, save, reset, box_zoom', x_range=x_range, y_range=y_range)
p.axis.visible = False

url = 'http://a.basemaps.cartocdn.com/light_all/{Z}/{X}/{Y}.png'
p.add_tile(WMTSTileSource(url=url))


def wgs84_to_web_mercator(df, lon="lon", lat="lat"):
    k = 6378137
    df["x"] = df[lon] * (k * np.pi / 180.0)
    df["y"] = np.log(np.tan((90 + df[lat]) * np.pi / 360.0)) * k
    return df


df = pd.DataFrame(dict(name=["Austin", "NYC"], lon=[-97.7431, -74.0059], lat=[30.2672, 40.7128]))
wgs84_to_web_mercator(df)

p.circle(x=df['x'], y=df['y'], fill_color='orange', size=10)

show(p)
