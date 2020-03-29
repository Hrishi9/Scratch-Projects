
'''
def draw(n="Hrishi"):
    print(n)
    if n == "Hrishi":
        print ("Name is Hrishi")
        var = n.strip(' ')
        var1 = []
        for i in var:
            var1.append(i)

        #print (var1)
        #var1 = [i for i in var]
        print (var1)


draw()

l = [] #list
dict = {1:'Hrishi'} #dict
str = 'string' #string
int = 0
bool # true or false
'''
'''
def star(a):

    #a = 4
    
    string = '*'
    c = ' '

    #for i in range(a,b):
    #string = string + '*'
    for i in range(0, a):
        print (string * a)



star(7)

'''
#just put a digit anjjj
'''
class Hrishi(object):
    def print(self, n):
        print(n)


x = Hrishi()
x.print('Hrishi')
'''
'''
def triangle(a):
    g=int(input("enter a number"))

    for i in range(1,3):
        print(a+a+a+a+a+a+a+a+a+a)
    for i in range(1,g):
        print("\t**")

triangle("*")
'''
'''
def tee():
    string = ' '
    string1 = ' '
    for i in range (1, 20):
        string = string + '*'
        if i == 19:
            for j in range (0, 2):
                print(string)


    for i in range (1, 10):
        string1 = string1 + '*'
        string2 = '      '
        #print (i, string1)
        if i == 5:
            for j in range(1, 10):
                print (string2 + string1)



tee()
'''
'''
def ice():
    string =' '
    string1 =' '
    string2 = ' '
    for i in range(1, 20):
        string = string + '/'
        if i==19:
          for j in range(0,2):
             print (string)

    for m in range(1,10):
        string1 = string1 + '*'
        if m==5:
            #for k in range(0,10):
            #while True:
            string1 = '       ' + string1
            for k in range(0, 10):
                print (string1)


    for i in range(1, 20):
        string2 = string2 + '*'
        if i==19:
          for j in range(0,2):
             print (string2)


ice()

'''

def Zed():
    string = ''
    string1 = ''
    string2 = '  '
    string3 = ''
    for i in range (0,14):
        string = string + '*'
        if i==13:
            for i in range(0,2):
                print(string)
    for i in range(0,5):
        string1 = string1 + '*'
        if i ==4:
            for i in range (0,8):
                string2= " "
                string1= string2 + string1
                print (string1)


    for i in range (0,14):
        string3 = string3 + '*'
        if i==13:
            for i in range(0,2):
                print(string3)


Zed()

all good? should I push the code to github?
#nice
push itok
how to change the directory to this python one current?
cd to thid dir ok
im on right branch right?