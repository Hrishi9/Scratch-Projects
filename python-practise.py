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
# just put a digit anjjj
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
'''

'''
## 9 Palindrome

s = str(x)
rs = "".join(list(reversed(s)))
if rs != s:
    return False
return True

'''
'''
#-1 solution

def palindrome(str):
    #str(x)
    str1=str[::-1]
    if str==str1:
        return True
    else:
        return False

palindrome(abcde)

'''

# 14 largest common prefix
'''
def largestcommon(n1,n2,n3):
    str=n1
    str2=n2
    str3=n3
    str4=''
    str5=''
    for i in range(0, len(n1)):

        for j in range(0, len(n2)):
            #print(n1[i],n2[j])
            print (i,j)
            if n1[i]==n2[j]:
                print(n1[i], n2[j])
                str4=n1[i]
                #print(str4)
                #i+=1


largestcommon("donut","dough","dog")
'''

'''
def lcp(n1,n2):
    str1=n1
    str2=n2
    str4 = ' '
    i = 0
    j = 0
    if len(n1)>len(n2):
      while True:
        if n1[i] == n2[j]:
            str4 = str4 + n1[i]
            print(str4)
        i+=1
        j+=1
    else:
        return False


lcp("doughnut","dog")

'''

# '''
# for i in range(1, len(str4)):
#     for j in range(1, len(n3)):
#         if n1[i]==n3[j]:
#             str5=n1[i]
#             return str5
#         else:
#             return False
#
# print("", str5)
# '''
'''
def Hek():
    str=""
    str1=""
    str2=""
    for i in range (1,5):
        str=str + "*"
    for i in range (1,19):
        str1=str1 + "*"
    for i in range (1,11):
        str2 = str2 + " "
    for i in range (1,11):

        if i in range (5,7):
            print(str1)
        else:
            print(str+str2+str)


Hek()
'''
'''
def H():
    str=""
    str1=""
    for i in range(1, 16):
        if i <= 5 or i >= 11:
            str = str + "*"
        else:
            str = str + " "

    for i in range (1,16):
        str1=str1+"*"
    for i in range (1, 11):
        if i <5 or i>6:
         print(str)
        else:
            print(str1)
H()
'''
'''
def H():
    str = ""
    str1 = ""
    for j in range(1, 20):

            str = str + '\n'
            for i in range(1, 16):
                if i <= 5 or i >= 11:
                    str = str + "*"
                elif j ==10 or j ==11 or j ==12:
                    str = str + '*'
                else:
                    str = str + " "

    print (str)

H()
'''
'''
def Huk():
    str = ""
    str1 = ""


    for j in range(1, 20):
        str = str + '\n'
        for i in range(1, 27):
            if i <= 5 or i in range (11,16) or i in range (20,25):
                str = str + "*"
            elif j == 10 and i < 15 or j == 11 and i < 15 or j == 12 and i < 15 or j in range (0,3) and i in range (18,27) or j in range (18,20) and i in range (18,27):
                str = str + '*'
            else:
                str = str + " "
    print(str)
Huk()

'''

'''

def Ef():
    str = ""
    for i in range (1,20):
        str = str + '\n'
        for j in range (1,43):
            if j<=5 or j in range (24,30):
               str = str + "*"
            elif i in range (1,3) and j <20 or i in range (9,11) and j<20 or i in range (18,20) and j<20:
                str = str + '*'
            elif i in range(1,3) and j>24 or i in range (9,11) and j>24:
                str = str + '*'
            else:
               str = str + " "
    print(str)
Ef()

'''

'''

def Efwhile():
    str = ""
    #str1 = ""
    i=0
    while i<10:
        i+=1

    #i==0
        str = str + '\n'
        j=0
        k=0
        j += 1

        while j<=5:

            str = str + "*"
            j += 1


        while i in range(1,3) and j<15 or i in range (5,7) and j<15 or i in range (9,11) and j<15:

            str = str + "*"
            j +=1

        #while k in range (0,10):
        #    str= str + "/"
        #k+=1
            #j+=1
        j+=1
        while i in range (0,11) and j<19:
            j+=1
            str = str + " "
        while i in range (0,11) and j in range (19,25):
            j+=1
            str= str+ "*"
        while i in range (0,3) and j<35 or i in range (5,7) and j<35:
            j+=1
            str= str + '*'

        #i+=1
    print(str)

        #if i==20:
         #   break
Efwhile()

'''

'''

# Leetcode 27
def removeElement(nums, val):
    newnum = []
    for i in range (len(nums)):
      #  print(nums)
        if val!=nums[i]:
            #print(nums)
            newnum.append(nums[i])
    print(newnum)


removeElement([1,3,5,6,3,2,0,8], 3)

'''
'''
# Leetcode 26
def removeDuplicate(nums):
    newnum = []
    #val
    for i in range(len(nums)):

        #if nums[i]!=nums[i+1]:
            #print (nums[i], nums [i+1])

            try:
                if nums[i] != nums[i + 1]:
                    newnum.append(nums[i])
                    print(newnum)
                else:
                    pass
            except IndexError:
                newnum.append(nums[i])
                print(i)
                print(newnum)
                break


    


removeDuplicate([1,1,1,2,3,3,3,5,5,5,6])

'''
'''
def searchInsert(nums, target):
    for i in nums:
        if target==i:
            return (nums.index(i))
        elif target > nums[-1]:
            print("in condition")
            return (len(nums))
        elif target>i:
            print ("In continue statement")
            continue
        else:
            print ("In else statement")
            return (nums.index(i))



print(searchInsert([1,3,5,5,6],6))
'''
'''
def searchInsert(nums, target):
    if type(target) == int:
        for i in nums:
            if target - i > 0:
                pass
            else:
                return (nums.index(i))
        return (nums.index(i)+1)
    else:
        return ("Pass a variable in target")
        #print ("Pass a variable in target")


#print (searchInsert([1,2,4,5,6], 6))
def insert():
    index = searchInsert([1, 2, 4, 5, 6], 3)
    nums = [1, 2, 4, 5, 6]
    target = 3
    nums.insert(index, target)
    print(nums)

insert()
'''
'''
def searchInsertinArray(nums,target):
        val = []
        for i in nums:
            if target-i >0:
                print(i)
                val.append(i)
                #print(val)
                if i==nums.index[-1]:
                    val.append(target)
            elif target-i == 0:
                val.append(i)
                val.append(i)
            else:
                print ("Else condition")
                val.append(target)
                print(val)
        #print (nums.index(i)+1)
        #print(val)
        #find index
        #append to that index


print (searchInsertinArray([1,2,4,5,6],8))
'''
'''
def searchInsertinArray(nums,target):
    val = []
    for i in nums:
        print (i)
        if target-i > 0 or target-i>0 and target-i<0:
            val.append(i)
        elif target-i==0:
            val.append(i)
            val.append(i)
        elif target-i < 0 and (nums.index(i)==0):
            val.append(target)
            val.append(i)
        else:
            val.append(i)
    if target-i>0 and nums[::-1]:
        val.append(target)
    print(val)
searchInsertinArray([2,3,6,7],5)
'''
'''
def union():
    a = [1,2,3,4,5]
    b = [4,5,6,7,8,9]

    #A = set(a) | set(b)
    #B = set(a) & set(b)

    print('Union of the arrays:', set(a) | set(b))
    print('intersection of the arrays:', set(a) & set(b))
union()
'''

'''
# Python 3 program to find
# n'th term in look and
# say sequence

# Returns n'th term in
# look-and-say sequence
def countnndSay(n):
    # Base cases
    if (n == 1):
        return "1"
    if (n == 2):
        return "11"

    # Find n'th term by generating
    # all terms from 3 to n-1.
    # Every term is generated using
    # previous term

    # Initialize previous term
    s = "11"
    for i in range(3, n + 1):

        # In below for loop,
        # previous character is
        # processed in current
        # iteration. That is why
        # a dummy character is
        # added to make sure that
        # loop runs one extra iteration.
        s += '$'
        l = len(s)

        cnt = 1  # Initialize count
        # of matching chars
        tmp = ""  # Initialize i'th
        # term in series
        print ("i loop",i,s,cnt,tmp)
        # Process previous term to
        # find the next term
        for j in range(1, l):

            # If current character
            # does't match
            if (s[j] != s[j - 1]):

                # Append count of
                # str[j-1] to temp
                tmp += str(cnt + 0)

                # Append str[j-1]
                tmp += s[j - 1]

                # Reset count
                cnt = 1
                print("j loop",j, cnt, tmp)
            # If matches, then increment
            # count of matching characters
            else:
                cnt += 1

        # Update str
        s = tmp
    return s;

print(countnndSay(7))

#1 = 1    
#11 = 2  (one 1)
#21 = 3 (two 1s)
#1211 = 4 (one 2 one 1)
#111221 = 5 (one 1 one 2 two 1)
#312211 = 6 (three 1 two 2 one 1)
'''

'''
class Solution(object):
    def maxSubArray(self, nums):
        def dp(nums):
            n = len(nums)
            f = [0 for _ in range(n)]
            print(f)
            f[0] = nums[0]
            print (f)
            for i in range(1, n):
                print(f[i -1] + nums[i])
                f[i] = max(f[i-1] + nums[i], nums[i])
                print("for loop f",f, f[i -1] + nums[i], f[i])
            return max(f)
        return dp(nums)
'''
'''
class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        curr = nums[0]
        ans = nums[0]
        for i in range(1, n):
            curr = max(curr + nums[i], nums[i])
            #(curr = 1 + 1, 1)
            print ("curr",curr)
            if curr > ans:
                ans = curr
                print ("ans", ans)

x = Solution()
print(x.maxSubArray([1,3,6,8,-5,86,7,43,5,8,9]))
 
'''
'''
def maxAddition(nums):
   curr = nums[0]
   prev = nums[0]
   for i in range(1, len(nums)):

       curr= max(curr + nums[i], nums[i])
       print ("This is current",curr,"This is previous",prev)
       if curr > prev:
           prev = curr
           print(curr, prev ,"If condition")

maxAddition([1,2,8,-60,5,6,-3])

'''
'''
def removedup(nums):
    a = []
    b = []
    prev = 0
    for i in nums:
        if i not in b:
            b.append(i)
            print(b)

removedup([1,1,2,3,4,1,5,6])

#a=[1,2,3,4,5,5] b=[]
## if b does not contain element of a, then append to b

'''

#def RemoveDupSortedLinklist(nums):


#RemoveDupSortedLinklist([])
'''
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList(object):
    def __init__(self):
        self.headval = None

# Print the linked list
def listprint(self):
    printval = self.headval
    while printval is not None:
        print (printval.dataval)
        printval = printval.nextval

x = SLinkedList
print(listprint())
'''

'''

class Node:

    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode


    def getData(self):
        return self.data

    def setData(self, val):
        self.data = val

    def getNextNode(self):
        return self.nextNode

    def setNextNode(self, val):
        self.nextNode = val

#[]->[]->[]
class LinkedList:


    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def getSize(self):
        return self.size

    #def addNode(self, data):
        #newNode = Node(data, self.head)
        #self.head = newNode
        #self.size += 1
        #return True

    def addNode(self, data):
        newNode = Node(data, self.head)
        self.head = newNode
        self.size +=1

    #def printNode(self):
        #curr = self.head

        #while curr:
            #print(curr.data)
            #curr = curr.getNextNode()

    def printNode(self):
        curr = self.head
        A= set()
        while curr:

            A.add(curr.data)
            curr = curr.getNextNode()
            print(sorted(A))
            b=sorted(A)
            print("this is B: ",b)
            for i in b:

                print(i)


myList = LinkedList()
print("Inserting")
print(myList.addNode(5))
print(myList.addNode(15))
print(myList.addNode(15))
print(myList.addNode(25))
print("Printing")
myList.printNode()
print("Size")
print(myList.getSize())

'''
'''

def mergearray(nums1,m,nums2,n):
    print (nums1[m:], nums2[:n])
    nums1[m:] = nums2[:n]
    nums1.sort()
    print (nums1)

mergearray([1,2,3,4,5],3,[2,3,7,8,9],3)
#1,2,2,3,3,7

'''
import collections

def SingleNumber(nums):
        b = collections.Counter(nums)
        print(b)
        c= b.items()
        print(c)
        for item in c:
            print (item)
            if item[1]==1:
                print("This is the item", item[0])


SingleNumber([2,2,7,9,7,3,3,4,4])