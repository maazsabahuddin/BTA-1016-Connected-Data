# Python imports
import requests
import json
import flag

# Package imports
from flask import Flask, render_template, request
import pygal
import nasdaqdatalink

# Local imports


app = Flask('app')
jsonObject = open("./key.json")
config = json.load(jsonObject)


@app.route("/")
def base():
    """
    This end-point is the base api end-point
    :return:
    """
    pkr_value = json.loads(requests.get(
        f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd/pkr.json"
    ).text)
    usd_value = json.loads(requests.get(
        f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd/usd.json"
    ).text)
    cad_value = json.loads(requests.get(
        f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd/cad.json"
    ).text)
    gbp_value = json.loads(requests.get(
        f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd/gbp.json"
    ).text)

    nasdaqdatalink.ApiConfig.api_key = config["nasdaq_key"]
    nasdaq_pak = nasdaqdatalink.get(f'ECONOMIST/BIGMAC_{"PAK"}', start_date="2020-12-01", end_date="2022-11-19")
    nasdaq_usa = nasdaqdatalink.get(f'ECONOMIST/BIGMAC_{"USA"}', start_date="2020-12-01", end_date="2022-11-19",
                                    column_index=1)
    nasdaq_can = nasdaqdatalink.get(f'ECONOMIST/BIGMAC_{"CAN"}', start_date="2020-12-01", end_date="2022-11-19")
    nasdaq_gbp = nasdaqdatalink.get(f'ECONOMIST/BIGMAC_{"EUR"}', start_date="2020-12-01", end_date="2022-11-19")

    return render_template("index.html",
                           pkr=f"1 USD = {pkr_value['pkr']} PKR",
                           usd=f"1 USD = {usd_value['usd']} USD",
                           cad=f"1 USD = {cad_value['cad']} CAD",
                           gbp=f"1 USD = {gbp_value['gbp']} GBP",
                           nasdaq_pak=[nasdaq_pak.to_html(classes='data')],
                           nasdaq_usa=[nasdaq_usa.to_html(classes='data')],
                           nasdaq_can=[nasdaq_can.to_html(classes='data')],
                           nasdaq_gbp=[nasdaq_gbp.to_html(classes='data')],
                           nasdaq_pak_burger="🍔"*17,
                           nasdaq_usa_burger="🍔"*7,
                           nasdaq_can_burger="🍔"*10,
                           nasdaq_gbp_burger="🍔"*9,
                           domain="http://192.168.1.24:5000/")


@app.route('/line-graph', methods=['GET'])
def line_graph_data():
    """
    This function will create a linegraph chart against currency pairs
    :return:
    """
    currency = request.args.get("currency")
    dates = []
    usd_vs_x = []
    for i in range(10, 20):
        dd = str(i).zfill(2)
        _data = json.loads(requests.get(
            f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/2022-11-{dd}/currencies/usd/{currency}.json"
        ).text)
        usd_vs_x.append(_data[currency])
        dates.append(_data["date"])

    # Create a pygal visualization
    line_chart = pygal.Line()
    line_chart.title = f'Value of USD in {currency.upper()} for last 10 days'
    line_chart.x_labels = dates
    line_chart.add(currency.upper(), usd_vs_x)
    return line_chart.render()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
