#!/usr/bin/env python3

from flask import Flask

import random

app = Flask(__name__)

@app.route('/')

def index():
	return 'Hi'

@app.route('/rand/<output_list_size>')

def operation_random(output_list_size):
    size = int(output_list_size)
    list = []
    for i in range(size):
        list.append(str(random.randint(0, size)))
    return list

@app.route('/sum/<values>')

def operation_sum(values):
    sum_list = []
    sum = 0
    
    for i in values.split(','):
        sum_list.append(int(i))

    for i in sum_list:
        sum += i
    
    content = "this is list of values " + str(sum_list) + "\n This is the sum " + str(sum)
    return content

@app.route('/avg/<values>')

def operation_avg(values):
    sum_list = []
    sum = 0

    for i in values.split(','):
        sum_list.append(int(i))

    for i in sum_list:
        sum += i

    content = "This is a list of values" + str(sum_list) + "\n This is the average" + str(sum / len(sum_list))

    return content

@app.route('/binary/<values>')

def operation_binary(values):
    list_of_binary = []

    for i in values.split(','):
        list_of_binary.append(bin(int(i))[2:])

    content = "This is a list of values" + str(list_of_binary)

    return content

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
