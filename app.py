from flask import Flask, render_template
from pycentral.base import ArubaCentralBase
from pprint import pprint
import json
from requests.models import Response
import creds as creds

central_info = creds.central_info


ssl_verify = True
central = ArubaCentralBase(central_info=central_info,
                           ssl_verify=ssl_verify)

apiPath = "/monitoring/v1/clients/wireless"
apiMethod = "GET"
apiParams = {}


app = Flask(__name__)

@app.route("/")
def index():
    wlan_total_up = central.command(apiMethod="GET",
                            apiPath="/monitoring/v2/clients?calculate_total=true&limit=1&timerange=3H&client_type=WIRELESS&client_status=CONNECTED")
    wlan_total_down = central.command(apiMethod="GET",
                            apiPath="/monitoring/v2/clients?calculate_total=true&limit=1&timerange=3H&client_type=WIRELESS&client_status=FAILED_TO_CONNECT")
    wired_total_up = central.command(apiMethod="GET",
                            apiPath="/monitoring/v2/clients?calculate_total=true&limit=1&timerange=3H&client_type=WIRED&client_status=CONNECTED")
    wired_total_down = central.command(apiMethod="GET",
                            apiPath="/monitoring/v2/clients?calculate_total=true&limit=1&timerange=3H&client_type=WIRED&client_status=FAILED_TO_CONNECT")
    ap_total_up = central.command(apiMethod="GET",
                            apiPath="/monitoring/v2/aps?status=Up&calculate_total=true")
    switch_total_up = central.command(apiMethod="GET",
                            apiPath="/monitoring/v1/switches?status=Up&calculate_total=true")
    apprf_top = central.command(apiMethod="GET",
                            apiPath="/apprf/datapoints/v2/topn_stats")
    audit_events = central.command(apiMethod="GET",
                            apiPath="/auditlogs/v1/events?limit=5")
#    print("apprf_top:", apprf_top)  # Debug output                         
#    print("apprf_top:", apprf_top)
    return render_template("index.html", wlan_total_up = wlan_total_up, wlan_total_down = wlan_total_down, wired_total_up = wired_total_up, wired_total_down = wired_total_down, ap_total_up = ap_total_up, switch_total_up = switch_total_up, apprf_top = apprf_top, audit_events = audit_events)

@app.route("/index.html")
def dashboard():
    wlan_total_up = central.command(apiMethod="GET",
                            apiPath="/monitoring/v2/clients?calculate_total=true&limit=1&timerange=3H&client_type=WIRELESS&client_status=CONNECTED")
    wlan_total_down = central.command(apiMethod="GET",
                            apiPath="/monitoring/v2/clients?calculate_total=true&limit=1&timerange=3H&client_type=WIRELESS&client_status=FAILED_TO_CONNECT")
    wired_total_up = central.command(apiMethod="GET",
                            apiPath="/monitoring/v2/clients?calculate_total=true&limit=1&timerange=3H&client_type=WIRED&client_status=CONNECTED")
    wired_total_down = central.command(apiMethod="GET",
                            apiPath="/monitoring/v2/clients?calculate_total=true&limit=1&timerange=3H&client_type=WIRED&client_status=FAILED_TO_CONNECT")
    ap_total_up = central.command(apiMethod="GET",
                            apiPath="/monitoring/v2/aps?status=Up&calculate_total=true")
    switch_total_up = central.command(apiMethod="GET",
                            apiPath="/monitoring/v1/switches?status=Up&calculate_total=true")
    apprf_top = central.command(apiMethod="GET",
                            apiPath="/apprf/datapoints/v2/topn_stats")
    audit_events = central.command(apiMethod="GET",
                            apiPath="/auditlogs/v1/events?limit=5")                         
    return render_template("index.html", wlan_total_up = wlan_total_up, wlan_total_down = wlan_total_down, wired_total_up = wired_total_up, wired_total_down = wired_total_down, ap_total_up = ap_total_up, switch_total_up = switch_total_up, apprf_top = apprf_top, audit_events = audit_events)
    
@app.route("/wlan_clients.html")
def wlan_client_info():
    clients = central.command(apiMethod="GET",
                            apiPath="/monitoring/v2/clients?timerange=3H&client_type=WIRELESS&client_status=CONNECTED")
    return render_template("wlan_clients.html", clients = clients)

@app.route("/wired_clients.html")
def wired_client_info():
    clients = central.command(apiMethod="GET",
                            apiPath="/monitoring/v2/clients?timerange=3H&client_type=WIRED&client_status=CONNECTED")
    return render_template("wired_clients.html", clients = clients)

@app.route("/devices.html")
def device_info():
    aps = central.command(apiMethod="GET",
                            apiPath="/monitoring/v2/aps")
    switches = central.command(apiMethod="GET",
                            apiPath="/monitoring/v1/switches")
    return render_template("devices.html", aps = aps, switches = switches)
