# code file for ex21 
# Functions can return sth 

def add(a,b):
    print "ADD %d + %d" %(a,b)
    return a+b

def subtract(a,b):
    print "SUBTRACTING %d - %d" % (a, b )
    return a-b

def multiply(a, b):
    print "MULTIPLYING %d * %d" %(a,b)
    return a*b

def divide(a,b):
    print "DIVIDING %d / %d" %(a,b)
    return a/b

print "Let's do some math through funtions"

age = add(30,5)
height = subtract(70,5)
weight = multiply(90,2)
iq = divide(100,2)

print "Age: %d, Height: %d; Weight: %d; IQ: %d" %(age, height, weight, iq)

# A puzzle for the extra credit, type is anyway
print "Here is a puzzle"

what = add(age, subtract(height, multiply(weight,divide(iq, 2))))

print "That becomes", what, "Can you do it by hand?"


