#!/usr/bin/env python3

# My aim is to:

# Take 2 forms of input
# Cut the console input 
# Operation -> Find a number between the min and max number
# Append it to console or output

import sys
import random

input_file = "/dev/stdin" #Console read
#input_file = "z_in" #Input file

output_file = "/dev/stdout" #Console output
#output_file = "z_out" #output file

def parse_arguments():
    operation = "random"
    arguments = sys.argv[1:]
    argument_count = len(arguments)
    if argument_count > 0:
        operation = arguments[0]
    return operation

def read():
    file = open(input_file, "r")
    record = file.read()[:-1]
    values = []
    for value in record.split():
        values.append(int(value))
    return values 

def operation_average(values):
    print(f"Average: {values}")
    sum = 0
    for i in values:
        sum += i
    return [sum/len(values)]

def operation_sum(values):
    print(f"Sum: {values}")
    sum = 0
    for i in values:
        sum += i
    return [sum]

def operation_binary(values):
    print(f"Binary: {values}")
    list_of_binary = []
    for i in values:
        list_of_binary.append(bin(i)[2:])
    return list_of_binary

def operation_random(output_list_size):
    list = []
    for i in range(output_list_size):
        list.append(str(random.randint(0, output_list_size)))
    return list

def write(result):
    file = open(output_file, "w")
    for item in result:
        file.write("%s\n" % item)

def main():
    operation = parse_arguments()
    values = read()
    result = [f"Invalid operation: {operation}"]
    if operation == "average":
        result = operation_average(values)
    if operation == "sum":
        result = operation_sum(values)
    if operation == "binary":
        result = operation_binary(values)
    if operation == "random":
        result = operation_random(values[0])
    write(result)


if __name__ == "__main__":
    main()
