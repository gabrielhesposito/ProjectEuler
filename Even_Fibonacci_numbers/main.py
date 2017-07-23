#!/usr/bin/env python
#python 2.7
import argparse

arguments=argparse.ArgumentParser(description='Fib sequence to what level?.' )
arguments.add_argument("fibnumber",metavar='N', type=int, nargs='1',help="a fib number")

input= arguments.parse_args()
print input.accumulate(input.fibnumber)

#import argparse

#parser = argparse.ArgumentParser(description='Process some integers.')
#parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
#parser.add_argument('--sum', dest='accumulate', action='store_const',const=sum, default=max, help='sum the integers (default: find the max)')

#args = parser.parse_args()
#print args.accumulate(args.integers)

#global scope
fib_number=0
for i in range(0, 4000000):
    if ( (i % 2) > 0 ):
	fib_number=fib_number+i
print(fib_number)

