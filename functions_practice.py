#create function(no arguments, returns nothing)
def hello():
    print('Hello World')

#create function, 3 arguments, return single listwith 3 arguments
def pack(a,b,c):
    myList = [a,b,c]
    return myList

#create function, accepts a list, prints out a series of strings 
def eat_lunch(menu):
    if len(menu)<1:
        print('my lunchbox is empty')
    else:
        for i in range(len(menu)):
            if i==0:
                print("First I eat __"+menu[i])
            else:
                print("Next I eat ___"+menu[i])

hello()
appetizer="dip bread"
entree='wild salmon'
dessert='ice cream'
menu=pack(appetizer, entree, dessert)
print(menu)
eat_lunch(menu)