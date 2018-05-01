from flask import Flask, request
import json
import re


app = Flask(__name__)


@app.route('/calc', methods=['GET', 'POST']) # For å teste api, gå til http://127.0.0.1:5000/calc
def calculator():

    if request.method == 'GET':
        with open("calc_form.html") as file:
            return file.read()
    elif request.method == 'POST':

        # calculate result
        expression = request.form.get('expression')
        clean_expression = re.sub('[^0-9,+,-,*,/,(,),+-,-+,--]', '', expression)

        if clean_expression is None or clean_expression == "":
            body = {"Error message": "Expression entered on invalid form"}
            return json.dumps(body), 400

        result = {"result": eval(clean_expression)}
        return json.dumps(result)


if __name__ == '__main__':
    app.run(debug=True)
