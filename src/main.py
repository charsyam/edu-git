from flask import Flask, render_template, request
from add import add
from minus import minus

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('calu.html', result=0)


@app.route('/add', methods=['POST'])
def add_endpoint():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])

    return render_template('calu.html', result=add(num1,num2))


@app.route('/minus', methods=['POST'])
def add_endpoint():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])

    return render_template('calu.html', result=minus(num1,num2))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
