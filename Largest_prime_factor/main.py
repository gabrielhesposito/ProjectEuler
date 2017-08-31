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
    lpf_stack = []
    topprime=""
    for i in range( lpf , 0 , -1 ):
       #print i   
      	 #base case should end here
       for prime in range ( i, 0 , -1 ):
         #print prime
         if ( ( i % prime ) == 0 ):
           #not prime
           break
         if ( prime == 1 ):
           # find prime
           print i
           lpf_stack.append(i)
           break 
    print lpf_stack



calc_lpf() 
