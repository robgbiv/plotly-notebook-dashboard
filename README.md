# plotly-notebook-dashboard
A way to pass Plotly charts from an IPython Notebook to dashboards.ly

In your Notebook, add something like this:

```py
import plotly.plotly as py      # Every function in this module will communicate with an external plotly server
foo = py.plot({                      # use `py.iplot` inside the ipython notebook
    "data": [{
        "x": [1, 2, 3, 4],
        "y": [4, 2, 5, 10]
    }],
    "layout": {
        "title": "a"
    }
}, filename='foo/01',      # name of the file as saved in your plotly account
   privacy='public')            # 'public' | 'private' | 'secret': Learn more: https://plot.ly/python/privacy
```

To send to dashboards.ly, call dashboard.create(plots, number of columns):
```py
import plotly_dashboard
plots = [foo, bar, baz]         # You can also pass in strings of URLs of plots instead of variables
plotly_dashboard.create(plots, 2) # 2 here is the number of columns per row on the dashboard
```

### Version
0.1.0

### Installation

- pip install plotly
- Copy the contents of this folder to your working directory

Then set your plotly credentials:
```py
python -c "import plotly; plotly.tools.set_credentials_file(username='foo', api_key='bar')"
```

- See the notebook in the repo for an example

### Todos

 - Set number of rows and columns
 - Lots

License
----

MIT
