#!/usr/bin/env python
#python 2.7
import argparse
import time

def get_inputs ():
    arguments=argparse.ArgumentParser(description='Largest Prime to what level?.')
    arguments.add_argument("--lpf", dest="lpf", required=True, type=int, nargs='?')
    input= arguments.parse_args()
    print input.lpf
    return input.lpf


def calc_lpf ():
    lpf = get_inputs()
    lpf_stack = []
    topprime=""
    for i in range( lpf , 1 , -1 ):
       print "This is the prime evaluated : " +  str(i)
       for prime in range ( i, 1, -1 ):
         print "This is the number evaluated : " + str(prime)
         if ( ( i % prime ) == 0 ) and ( (i / prime) > 1 ) :
           #not prime
           time.sleep (2)
           break
         else:
           print "prime found print i" + str(i)
           lpf_stack.append(i)
    print lpf_stack


calc_lpf() 
