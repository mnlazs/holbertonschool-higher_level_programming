#!/usr/bin/python3
import random
Last digit of = random.randint(-10000, 10000)
if Last digit > 5:
    print("{:d} and is greater than 5".format(Last digit))
elif Last digit == 0:
    print("{:d} and is 0".format(Last digit))
else:
    print("{:d} and is less than 6 and not 0".format(Last digit))
