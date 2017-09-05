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


def test_lpf ():
    index=-1
    for element in lpf_stack:
        index=index-1
        if ( element * lpf_stack[index]  == lpf ):
           lpf_list.append(element, lpf_stack[index])
           ## one above element
           lpf_stack.pop(index)
           ## elements position
           lpf_stack.pop(index+1)
           #for element in lpf_list

        
    

def calc_lpf ():
    lpf = get_inputs()
    #place primes here
    lpf_stack = []

    #place two eles here
    lpf_list = []

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
         if ( prime < isprime ) :
           if ( isprime % prime  == 0 ):
             #######
	     #not prime number is divisible
             #######
             #time.sleep (2)
             print "break:  this is isprime: " + str(isprime) + "this is prime: " + str(prime)
             break
           
           print "postbreak: this is isprime: " + str(isprime) + "this is prime: " + str(prime)

           if (  ( prime - 1 )  == 1  ):
             print "prime found print " + str(prime)
             lpf_stack.append(isprime)

    for element in lpf_list: 
         print element




calc_lpf() 
