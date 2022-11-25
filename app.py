#!/usr/bin/env python3

from flask import Flask

import core_operations

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hi'

@app.route('/<operation>/<record>')
def do_operation(operation, record):
    values = core_operations.convert(record)
    result = core_operations.operations[operation](values)
    return f"{operation}: {result}"

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
