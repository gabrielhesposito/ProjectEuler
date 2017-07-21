#!/usr/bin/env python
#python 2.7

#global scope
fib_number=0
for i in range(0, 4000000):
    if ( (i % 2) > 0 ):
	fib_number=fib_number+i
print(fib_number)

