from bokeh.plotting import figure
from bokeh.models import Dropdown
from bokeh.layouts import column
from bokeh.io import curdoc

### Generate our simple stock trends

T = [t for t in range(0,100)]
S1 = [t for t in T]
S2 = [-t for t in T]

p = figure(x_range=(min(T), max(T)), y_range=(min(S2), max(S1)), title="Simple Stock Trends")

r = p.line(T, S1)

ds = r.data_source

def select_stock(event):
    if event.item == "S1":
        ds.data["y"] = S1
    elif event.item == "S2":
        ds.data["y"] = S2
    else:
        raise Exception("Unknown stock trend selected")
    ds.trigger('data', ds.data, ds.data)

### Create dropdown menu for selecting stock trend
menu = [("Stock 1", "S1"), ("Stock 2", "S2")]
dropdown = Dropdown(label="Select Stock Trend", menu=menu)
dropdown.on_event("menu_item_click", select_stock)

curdoc().add_root(column(p, dropdown))
