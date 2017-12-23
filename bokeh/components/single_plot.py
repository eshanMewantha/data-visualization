from bokeh.plotting import figure
from bokeh.embed import components

plot = figure()
plot.circle([1,2,3,4,5], [3,4,3,2,5])

script, div = components(plot)

print(script)
print('\n\n\n\n')
print(div)