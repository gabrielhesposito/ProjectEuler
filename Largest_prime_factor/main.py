#!/usr/bin/env python
#python 2.7
import argparse

def get_inputs ():
    arguments=argparse.ArgumentParser(description='Largest Prime to what level?.')
    arguments.add_argument("--lpf", dest="lpf", required=True, type=int, nargs='?')
    input= arguments.parse_args()
    return input.fibnumber


def calc_lpf():
    lbf = get_inputs()
    lbf_stack = array ( lbf  )
    for i in range(0, lbf ):
        if ( ( (i+1) % i )  > 0 ):
           #prime found - ^^ above needs to work
 
