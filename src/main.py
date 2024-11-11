from flask import Flask, render_template, request
from calculator import add, subtract, multiply, divide

app = Flask(__name__)

def handle_calculation(operation_func):
    """계산 처리를 위한 헬퍼 함수"""
    try:
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = operation_func(num1, num2)
        return render_template('calculator.html', result=result)
    except ValueError as e:
        if str(e) == "0으로 나눌 수 없습니다":
            return render_template('calculator.html', result=str(e))
        return render_template('calculator.html', result="숫자를 올바르게 입력해주세요")
    except Exception as e:
        return render_template('calculator.html', result="오류가 발생했습니다")

@app.route('/')
def index():
    return render_template('calculator.html', result=0)

@app.route('/add', methods=['POST'])
def add_endpoint():
    return handle_calculation(add)

@app.route('/subtract', methods=['POST'])
def subtract_endpoint():
    return handle_calculation(subtract)

@app.route('/multiply', methods=['POST'])
def multiply_endpoint():
    return handle_calculation(multiply)

@app.route('/divide', methods=['POST'])
def divide_endpoint():
    return handle_calculation(divide)

if __name__ == '__main__':
    app.run(debug=True)