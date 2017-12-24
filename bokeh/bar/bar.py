from bokeh.models import ColumnDataSource, ranges, LabelSet
from bokeh.palettes import PuBu
from bokeh.plotting import figure
from bokeh.plotting import show

source = ColumnDataSource(dict(x=['DC','Marval'],y=[100,98]))

x_label = ""
y_label = "Ratings"
title = "Comic Book Ratings"
p = figure(plot_width=500, plot_height=300, tools="reset, wheel_zoom, box_zoom, save",
           x_axis_label = x_label,
           y_axis_label = y_label,
           title=title,
           x_minor_ticks=2,
           x_range = source.data["x"],
           y_range= ranges.Range1d(start=0,end=120))


labels = LabelSet(x='x', y='y', text='y', level='glyph',
        x_offset=-13.5, y_offset=0, source=source, render_mode='canvas')

p.vbar(source=source, x='x', top='y', bottom=0, width=0.3, color=PuBu[7][2])

p.add_layout(labels)
show(p)