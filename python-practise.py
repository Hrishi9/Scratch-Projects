
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
'''
'''
def Ozed ():
    string= ''
    string1= ' '
    string2= ''
    string3= ''
    string4= ''
    i = 20

    while True:

        string = string + "*"
        i -=1
        if i == 15 :
            for i in range(1, 10):


                     string1= " "+ string1
                         while i<=9:
                            string3 = string1
                             i -=1





                            print(string +string1 + string + string3)
                            break





             break





        #if i==5:
            #while True:
                #print(string)
                #break:



Ozed ()
'''
'''
def Lith():
    string=''
    i=0
    j=0
    k=0
    while True:

     while i<5:
        string= string+ '*'
        i+=1
     while j<9:
        print(string)
        j+=1
     while k<2:
        print(string*5)
        k+=1

     break

Lith()
'''
###list reference
'''
class iterate(object):
    def function(self, num):
        num : list[int]
        num.append(6)
        num.pop()
        print (num)

x = iterate()
x.function([1,2,3,4,5])
'''
'''
class addition(object):
    def add(self, nums):
        nums : list[int]
        var = nums[0] + nums[1]
        print(nums)
        print(var)

x = addition()
x.add([1,2,3,4,5])
'''
'''
class solution():
    def twoSum(self, nums: list[int], target: int) -> int:
    #def twoSum(self, nums: List[int], target: int) -> List[int]:
    #nums: List[int]
    #target: int
    #List[int]

        h = {}
        for i, num in enumerate(nums):
            #n = target - num
            #if n not in h:
                #h[num] = i
            #else:
                #return [h[n], i]
            print (nums)

x = solution()
x.twoSum([1,2,3,4], 1)
'''

'''
Number 1
def twoSum(nums, target):
    seen = {}
    for i, v in enumerate(nums):

        remaining = target - v
        print("This is remaining", remaining)
        print("This is before seen", seen)
        if remaining in seen:
            return [seen[remaining], i]

        seen[v] = i
        print("This is after seen", seen, i)

   # return []
    print("This is after seen", seen, i)




twoSum([2, 7, 11, 15], 26)

'''

def Reverse(n):
    #list=[int]
    #list.append(n)
    m=0
    print("Integer is ", n)
    print("This is in list", (list))
    digits = [int(x) for x in str(n) ]
    digits = digits [::-1]
    str1 = " "
    #print(digits[0],digits[1], digits[2])
    #print(len(digits))
    for i in range(0,len(digits)):
        q=0

        #print (i)
        q = digits[i]
        #print (digits[])
        #q==digits
        #print (digits[i])

        #print(q)
        #print(q)
        str1 = str1 + str(q)
        #str1=str1+q
    print(str1)
    #print (q)


Reverse(123)

