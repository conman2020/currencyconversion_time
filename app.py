from forex_python.converter import CurrencyRates, CurrencyCodes
from flask import Flask, session, request, render_template, redirect, make_response, flash
import logging

app = Flask(__name__)
app.config["SECRET_KEY"] = "fdfgkjtjkkg45yfdb"
c= CurrencyRates()
s=CurrencyCodes()

@app.route("/", methods=["GET"])
def homepage():
    """Show converter."""
    return render_template ("initialscreen.html")
@app.route("/result")
def result():
    # Rate=c.get_rate()
    starting_currency=request.args['starting_currency']
    conversion_currency=request.args['conversion_currency']
    symbolNewCurrency= s.get_symbol(conversion_currency)
    symbolStarting= s.get_symbol(starting_currency)
    cname= s.get_currency_name(conversion_currency)
    amount=request.args['amount']
    if symbolNewCurrency == None:
        return render_template ("result.html", error=f"{conversion_currency} is invalid country type")
    elif symbolStarting == None :
        return render_template ("result.html", error=f"{starting_currency} is invalid country type")
    elif int(amount) <= 0: 
        return render_template ("result.html", error=f"{amount} is invalid need to enter value greater than 0, negative values not allowed. ")
    # if new_amount >= 0: 
    #      return render_template ("result.html", error=f"{amount} is not a number please use numbers to convert")
    rate=c.get_rate(starting_currency, conversion_currency)
    total=round(rate*float(amount),2)
    return render_template ("result.html",starting_currency=starting_currency, conversion_currency=conversion_currency, amount=amount, rate=rate, total=total,symbol=symbolNewCurrency,cname=cname)


# @app.route("/faultyvalueentered")
# def faulty():
#     return render_template ("base.html")