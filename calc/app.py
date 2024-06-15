from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def addition():
    """Add a + b"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = add(a, b)
    return str(result)

@app.route('/sub')
def subtraction():
    """Subtract b from a"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = sub(a, b)
    return str(result)

@app.route('/mult')
def multiplication():
    """Multiply a * b"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = mult(a, b)
    return str(result)

@app.route('/div')
def division():
    """Divide a / b"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = div(a, b)
    return str(result)

#

operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args['a'])
    b = int(request.args['b'])
    result = operators[oper](a, b)
    return str(result)
