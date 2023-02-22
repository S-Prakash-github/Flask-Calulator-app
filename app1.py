## OBJECTIVE : addition substraction division and multiplication
## Create a Form to perform the specified actions
## A drop down to choose between the operations and the input will be of two numbers
## A button to give the result

from flask import Flask,request,jsonify,render_template

app = Flask(__name__)

## In get the query is seen in the url and for post it is comunicates with body
## both of them are used to get data

@app.route("/",methods = ['GET','POST'])

## invoking the website page
def home_page():
    return render_template('index.html')


@app.route("/math",methods = ['POST'])
def math_ops():
    ## all the data from the form is captured into the respective varibales
    if(request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if ops == 'add':
            r = num1+num2
            result = "The sum of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
        if ops == 'subtract':
            r = num1-num2
            result = "The Difference of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
        if ops == 'multiply':
            r = num1*num2
            result = "The Product of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
        if ops == 'divide':
            r = num1/num2
            result = "The divide of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
            
        return render_template('result.html' , result = result)

## OBJECTIVE : TO pass the data through POSTMAN(it is a tool for testing api)
@app.route('/postman_data',methods=['POST'])
def math_ops1():
    if(request.method == 'POST'):
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if ops == 'add':
            r = num1+num2
            result = "The sum of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
        if ops == 'subtract':
            r = num1-num2
            result = "The subtract of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
        if ops == 'multiply':
            r = num1*num2
            result = "The multiply of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
        if ops == 'divide':
            r = num1/num2
            result = "The divide of " + str(num1) + 'and ' + str(num2) + "is " + str(r)
            
        return jsonify(result)


if __name__=="__main__":
    app.run(host="0.0.0.0")
