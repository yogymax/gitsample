
def m1(): #function
    print('hi')

class Mobile:

    def __init__(self,id,nm,price,model): #with parameter
        self.mobileId= id
        self.mobileName=nm
        self.mobilePrice=price
        self.mobieModel=model

    def displayMobileInfo(self):  #without parameter method -- behivours
        print(self.mobileId)
        print(self.mobileName)
        print(self.mobilePrice)
        print(self.mobieModel)


M1= Mobile(1,"S7",28334.5,'AA')
m2= Mobile(2,"S8",48334.5,'BA')



m1.displayMobileInfo()
print('-----------------------')
m2.displayMobileInfo()


#indentifiers are nothging but -- lets take an example you have few lines of code..and you are identifing elements from it
# method classs variable constructor and function

# rules of identifiers.. -- Python
    #allowed chars are --- A-Z  a-z  _  0-9
    #should not start with digit
    # case sensitive
    #reserved keywords cannot be used as identifiers
#IT industry coding conventions..
    # variable name should start with small letter + camelcase     firstName="Yogesh"
    #class names -- class + should start with capital + camelcase
    #methodnames/function names -- def + shud start with small letters + camecase


#compiler interpretter
#pycharm and python installed -- configured on ur machine
#virtual env -- configure -- will repeated..
#pip

# class
#object
#method or function
#variable
# indefiers
# types of variables
# types of methods
# identifier rules
# module
# reserved keywords
    # for loops
    #datatypes in depth with method and practicals..

'''
https: // www.programiz.com / python - programming  # tutorial

file - - module

real
world
programming
world
structure / sacha


class
    states / properties
    variables


baviours
methods / functions
product
Object


class Mobile{
------
}


4
space - equal
to
indent


def -- is always


used
to
write
function or method in python
function or method - - is nothing
but
set
of
lines
of
code..
logically
code
bind
kar
k
rakha


def --- outside


the


class -- called as Function


def -- inside


the


class -- called as Method..


def m1method/


    functionname(num): num - - parameter
body - -
with indent

m1(10)  # 10-- arg


class Mobile:
    def m1():
        print('hello1')
        print('hello2')
        print('hello3')


print('hello4')
print('hello5')


class
    object


variable
methods
functions
parameters
args
module
import

file
package
directory
interpretter
compiler

10 <


class 'int'>


10.0 <


class 'float'>


10 + 2j <


class 'complex'>


'laptop' <


class 'str'>


"laptop2" <


class 'str'>


laptop3
<class 'str'>


True <


class 'bool'>


None <


class 'NoneType'>


complex
Datatypes - its
an
object
which
holds
objects as single
entity.
collections
of
elements as a
single
entity

[] <


class 'list'>


{10} <


class 'set'>


{} <


class 'dict'>


() <


class 'tuple'>


Datatypes

Number
int
float
complex
String
''
""
''' ''' - - multiline
string
List[]
Tuple()
Set
{"a"}
Dict
{}
Bool = True / False


'''