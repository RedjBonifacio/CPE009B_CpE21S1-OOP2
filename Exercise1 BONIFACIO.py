#Numbers
varium = 123
pi = 3.14159

#Strings
varstring = "Hello World!"
varText = 'This is a String'

#Lists
varList = ["abc", 123]

#Tuples
varTuple = 'abc' , 123, "HELLO"

#Dictionaries
var = 3
varDict = {'first':1, '2':'2nd' , 3:var}

varDict = {}
varDict['first']= 1
varDict['2'] = '2nd'
varDict[3] = var

#Addition
a = 5 + 3
print (a)

#Subtraction
a = 5 - 3
print (a)

#Multiplication
a = 5 * 3
print (a)

#Exponent
a = 5 ** 3
print (a)

#Division
a = 5 / 3
print (a)

a = 5 % 3
print (a)

a = 5 // 3
print (a)

#Increment/Decrement
a = 5
print (a)

a += 1
print (a)

#Decrement
a = 5
print (a)

a -= 1
print (a)

#String Concatenation
a = 'Hello' + 'World'
print (a)

#Complex Expressions
a = 3 + 5 - 6 * 2 / 4
print (a)

#Boolean Conditions
x = True

if x:
    print("var x is True")
else:
    print("var x is false")
    
#String COnditions
x = "Hello world!"

if x == 'Hello World!':
    print("var x is Hello World!")
else:
    print("var x is not Hello World!")
    
#Numberical Conditions
x = 10

if x == '10':
    print("var x is a string")
elif x == 10:
    print("Var x is an integer")
else:
    print("var x is none of the above")
    
#For Loops
for var in range(0, 5, 2):
    print(var)
    
#While Loops
var = 0
while var < 5:
    print(var)
    var += 2
    
#Nested Loops
while x < 5:
    for y in range (0, x):
        print(y, end='')
    x += 1
    print()
    
#Cain contain a number of values comprised of different datatypes.
pi = 3.14159
varList = [1, 2, 'A', 'B', 'Hello', pi]
print(varList[0])

print(varList[4])

varList.append('World!')
print(varList[6])

len(varList)

print(varList[5])

varList.remove(pi)
print(varList[5])

##Dictionaries
var = "Hello World!"
varDict = {'first' : 123, 2 : 'abc', '3' : var, 4 : ['lista', 'listb']}
print(varDict['first'])

print(varDict[2])

print(varDict['3'])

print(varDict[4])

print(varDict[4][1])

len(varDict)

#Generators can be used to build list in the memory as objects

def gen_num_up_to(n):
    num = 0
    while num < n:
        yield num
        num += 1
        

varList = gen_num_up_to(5)
print([var for var in varList])

def gen_num_up_to(n):
    num = 0
    while num < n:
        yield num
        num += 2
        
varList = gen_num_up_to(5)
print([var for var in varList])

varList = range(0, 5, 2)
print([var for var in varList])

#Slicing

varList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(varList[:5])

print(varList[5:])

print(varList[:-2])

print(varList[-2:])

print(varList[2:-2])

print(varList[2:8:2])

#Python functions use the following notation:
def remainder(n, m):
    while True:
        if n - m < 0:
            return n
        else:
            n = n - m

print(remainder(10, 4))
