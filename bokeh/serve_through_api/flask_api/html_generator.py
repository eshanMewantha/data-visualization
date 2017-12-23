import pandas as pd

from bokeh.plotting import figure
from bokeh.sampledata.stocks import AAPL


def get_template():
    df = pd.DataFrame(AAPL)
    df['date'] = pd.to_datetime(df['date'])

    import jinja2
    from bokeh.embed import components

    # IMPORTANT NOTE!! The version of BokehJS loaded in the template should match
    # the version of Bokeh installed locally.

    template = jinja2.Template("""
    <!DOCTYPE html>
    <html lang="en-US">
    
    
    <link
        href="http://cdn.pydata.org/bokeh/release/bokeh-0.12.11.min.css"
        rel="stylesheet" type="text/css">
    <link
        href="http://cdn.pydata.org/bokeh/release/bokeh-widgets-0.12.11.min.css"
        rel="stylesheet" type="text/css">
    <link
        href="http://cdn.pydata.org/bokeh/release/bokeh-tables-0.12.11.min.css"
        rel="stylesheet" type="text/css">
    
    <script src="http://cdn.pydata.org/bokeh/release/bokeh-0.12.11.min.js"></script>
    <script src="http://cdn.pydata.org/bokeh/release/bokeh-widgets-0.12.11.min.js"></script>
    <script src="http://cdn.pydata.org/bokeh/release/bokeh-tables-0.12.11.min.js"></script>
    
    
    <body>
    
        <h1>Hello Bokeh!</h1>
    
        <p> Below is a simple plot of stock closing prices </p>
    
        {{ script }}
    
        {{ div }}
    
    </body>
    
    </html>
    """)


    p = figure(plot_width=500, plot_height=250, x_axis_type="datetime")
    p.line(df['date'], df['close'], color='navy', alpha=0.5)
    p.toolbar.logo = None

    script, div = components(p)

    return template.render(script=script, div=div)

