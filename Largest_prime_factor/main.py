#!/usr/bin/env python
#python 2.7
import argparse

def get_inputs ():
    arguments=argparse.ArgumentParser(description='Largest Prime to what level?.')
    arguments.add_argument("--lpf", dest="lpf", required=True, type=int, nargs='?')
    input= arguments.parse_args()
    print input.lpf
    return input.lpf


def calc_lpf():
    lpf = get_inputs()
    lpforg = lpf
    lpf_stack = []
    topprime=""
    for i in range( lpf , 0 , -1 ):
      	 #base case should end here
       for prime in range ( i, 0 , -1 ):
         if ( prime == 1  ):
           --lpforg
           lpf = lpforg
           lpf_stack.append(i)
           break 
         if ( ( prime % (prime -1) ) ==  0 ):
           #not prime
           continue
    print lpf_stack



calc_lpf() 
