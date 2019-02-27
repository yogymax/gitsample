items1 = {1:'One',2:'Two',3:'Three'} #dict with values -- 2 values -- key:value -- becomes one pair -- item
items2 = {1} # set -- single element,
items3 = {} # empty dict
items4 = set() # empty set




num=98299394937
print('num=10',type(num),num)

num=10.0
print('num=10.0',type(num))

num=102+2J
print('num=10+2j',type(num))

num='laptop1'
print('laptop',type(num))

num="laptop2"
print('laptop2',type(num))

num='''laptop3'''
print('laptop3',type(num))

num=True
print('num=True',type(num))


num=None
print('num=None',type(num))



'''
complex -- collection of elements/objects as single entity and those objects can be
homogenous or hetrogenous 

list -- properties -- []
    duplicates are allowed
    seq order is preserved
    nonetype is allowed -- many
    mutable -- it can be changed after creation..add/update/remove
set -- {}
    
items = set()  or items={10}
     set doesnt allows duplicates -- unique elements only
     set doesnt preserves seq order
    max One None is allowed
    mutable -- it can be changed after creation..add/update/remove
    
dict = {} or {key:value}
    duplicate keys are not allowed...values can be duplicate
    seq not maintained...
    max one None Key is allowed
    mutable -- it can be changed after creation..add/update/remove
    
items = () or (10)
    -- seq order maintained..
    -- duplicates are allowed..
    -- immutable
    -- 

'''



listitems = [10,20,10,"A",'A',30.4,23+3j]
print('[]',type(listitems))

setitems={"A","B","C",102,403,405}
print('{10}',type(setitems))

dictitems={1:'One',2:'Two'}
print('{}',type(dictitems))

tupleitems=(10,20,3,40,50,604,32,"A")
print('()',type(tupleitems))