from flask import Flask
import exchange_rate_helper

app = Flask(__name__)
print("hello")
@app.route("/")
def hello():
    return {"message": "Hello World"}

@app.route("/currencies")
def getAllCurrencies():
    return {"currencies": exchange_rate_helper.getSupportedCurrencies()}
print('body_love_fofy')
@app.route("/rates")
def getAllRates():
    return {"rates": exchange_rate_helper.getAllExchangeRates()}
print('fares')
print('fares')
@app.route("/rate/<string:currency>")
def getRatesForCurrency(currency):
    try:
        return {"rates": exchange_rate_helper.getExchangeRatesForCurrency(currency)}
    except:
        return ({"error": "Unsupported currency provided"}, 400)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
