#!/usr/bin/env python

import requests
import json

def create(graph_urls, columns):
    num_plots = len(graph_urls)
    rows = []
    for i in range(0, num_plots):
        if i % columns == 0:
            rows.append([{"plot_url": str(graph_urls[i])}])
        else:
            rows[len(rows) - 1].append({"plot_url": str(graph_urls[i])})
    dashboard_json = {
        "rows": rows,
        "banner": {
            "visible": True,
            "backgroundcolor": "#3d4a57",
            "textcolor": "white",
            "title": "Dashboard",
            "links": []
        },
        "requireauth": False,
        "auth": {
            "username": "foo",
            "passphrase": "bar"
        }
    }

    if dashboard_title != None:
        dashboard_json[0]["rows"]["banner"]["title"] = dashboard_title

    response = requests.post('http://dashboards.ly/publish',
                             data={'dashboard': json.dumps(dashboard_json)},
                             headers={'content-type': 'application/x-www-form-urlencoded'})

    response.raise_for_status()

    dashboard_url = response.json()['url']
    print('dashboard url: http://dashboards.ly{}'.format(dashboard_url))
