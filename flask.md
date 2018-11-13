```
from flask import request

name = request.args.get('name', name)

@app.route('/')
@app.route('/<name>')

def index(name='Sean'):
    return "Hello {}".format(name)


@app.route('/<int: num1>/<int:num2>')
@app.route('/<float: num1>/<float:num2>')
def add(num1,num2):
    return num1 + num2
```
