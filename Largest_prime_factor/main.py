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
    for isprime in range( lpf , 1 , -1 ):
       ########
       #  
       #######
       #print "This is the prime evaluated : " +  str(i)
       for prime in range ( isprime, 1 , -1 ):         
         #print "this is isprime: " + str(isprime)
         #print "this is prime: " + str(prime)

         ##no numbs greater than, no numbs equal too
         if (prime < isprime) :
           if (   isprime % prime  == 0  ):
           #######
	   #not prime number is divisible
           #######
           #time.sleep (2)
             print "break:  this is isprime: " + str(isprime) + "this is prime: " + str(prime)
             break
           
           print "postbreak: this is isprime: " + str(isprime) + "this is prime: " + str(prime)
           if (  (prime - 1)  == 1  ):
             print "prime found print " + str(prime)
             lpf_stack.append(isprime)

    for element in lpf_stack: 
         print element


calc_lpf() 
