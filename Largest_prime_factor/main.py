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
    lpf_stack = [ lpf ]
    for i in range( lpf , 0 , -1 ):
       if ( ( i % i+1 )  > 0 ):
         print i
         continue
       else:
         continue



calc_lpf() 
