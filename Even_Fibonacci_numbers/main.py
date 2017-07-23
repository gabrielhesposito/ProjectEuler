#!/usr/bin/env python
#python 2.7
import argparse

def get_inputs():
    arguments=argparse.ArgumentParser(description='Fib sequence to what level?.' )
    arguments.add_argument("fibnumber",type=int, nargs='?')
    input= arguments.parse_args()
    return input.fibnumber

def calc_fib():
    fib_number=get_inputs()
    calculate_fib=0
    for i in range(0, fib_number):
        if ( (i % 2) > 0 ):
	   calculate_fib=calculate_fib+i
    print(calculate_fib)

calc_fib()

