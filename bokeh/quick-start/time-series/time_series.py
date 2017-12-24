import numpy as np

from bokeh.plotting import figure, output_file, show
from bokeh.sampledata.stocks import AAPL

aapl = np.array(AAPL['adj_close'])
aapl_dates = np.array(AAPL['date'], dtype=np.datetime64)
print(aapl_dates)

window_size = 30
window = np.ones(window_size) / float(window_size)
aapl_avg = np.convolve(aapl, window, 'same')

output_file("time_series.html", title='time series example', mode='inline')

p = figure(width=800, height=350, x_axis_type="datetime")

p.circle(aapl_dates, aapl, size=4, color="darkgrey", alpha=0.2, legend='close')
p.line(aapl_dates, aapl_avg, color="navy", legend="avg")

p.title.text = "AAPL One-Month Average"
p.legend.location = "top_left"
p.grid.grid_line_alpha = 0
p.xaxis.axis_label = "Date"
p.yaxis.axis_label = "Price"
p.ygrid.band_fill_color = "olive"
p.ygrid.band_fill_alpha = 0.1

show(p)
