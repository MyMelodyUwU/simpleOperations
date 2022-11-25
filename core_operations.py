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
    return record

def convert(record):
    values = []
    for value in record.split(","):
        values.append(int(value))
    return values

def write(result):
    file = open(output_file, "w")
    for item in result:
        file.write("%s\n" % item)

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

def operation_random(values):
    output_list_size = values[0]
    list = []
    for i in range(output_list_size):
        list.append(str(random.randint(0, output_list_size)))
    return list

def operation_sum_binary(values):
    return operation_binary(operation_sum(values))
# ^ Good design == easy + flexible code to change

operations = {
    "average": operation_average,
    "binary": operation_binary,
    "random": operation_random,
    "sum": operation_sum,
    "sum_binary": operation_sum_binary
}

def main():
    operation = parse_arguments()
    record = read()
    values = convert(record)
    if operation in operations:
        result = operations[operation](values)
        write(result)
    else:
        print(f"Invalid operation: {operation}")

if __name__ == "__main__":
    main()