#  if and nasted if 
age = 20
has_id = True

if age>=20 :
    if has_id == True:
        print ("You can enter ")
    else:
        print("You need an Id ")
else:
    print("You are too young ")


num= -3 
if num >0 :
   print("Positive")
elif num<0:
    print("Negative ")
else:
    print("Zero")

# loops 
for i in range (1,10):
 print(i)

for num in range(5,1):
 print(num)

# While
i=0
while i <5 :
    i+=1
    print(i)

# function:
def password_checher(password):
    if len(password)>=8:
        return "Strong"
    else:
        return "Weak"

print(password_checher("hsiahd8s"))

def discount(price):
    if price >=1000:
        return price -(price *0.2)
    elif price >= 500:
        return price-(price*0.1)
    else:
        return price

print(discount(100000))

def bigger(a,b):
    if a > b:
        return a
    elif a<b :
        return b 
    else :
        return "Equal "
print(bigger(9,0))


#lambda function :
maximum= lambda num1, num2: num1 if num1>num2 else  num2>num1 
print(maximum(6,3))

num= lambda x:"positive" if x>0 else "negative "
print(num(3))

add= lambda a,b,c: a+b+c
print(add(2,10,70))

grade= lambda mark:"A"if mark >=80 else "B"if mark >= 70 else "C"if mark >=60 else   "D" if  mark>= 50 else " F"
print(grade (49))

# recursion
def factorial(n):
    if n==1:
        return 1
    return n* factorial (n-1)
print(factorial(5))


# list 
names= ["Moahmed","omer","john"]
print(names[0])
print(names[1])
print(names[2])

names.remove("omer")
names.append("Ali")
names.reverse()
print(names)


# Tuble

tup= (1,4,8)
print(type(tup))
Tup=( 1, "hello",{"mhamed "},878,90,("ahmed"))
print(len(Tup))
print(len(tup))
print(tup[0],tup[2])
last_index=(len(tup))-1 # to know the last index
print(last_index)
print(tup[-2])
print(Tup[1:])
print(Tup[-1:])
print(Tup[0:])
print(Tup[:-1])
print(Tup[2:-1])
print(Tup[-3:-1])
fruits=("orange","banana","watermelon","apple",)
print(type(fruits))

tuple_to_list= list(fruits)
print(tuple_to_list)
print(type (tuple_to_list))
print("orange"in fruits) # True
Joining_tuple=Tup+tup+fruits
print(Joining_tuple)
empty_tuple=tuple()
brothers=("Mido",'hussan',"yousif")
sisters=('sara',"Maab","Ola")
siblings = brothers+sisters
print(siblings)

family_memebers=siblings+("John","Lissa")
print(family_memebers)

# sets 
a= {1,2,3,4}
b={3,4,5,6,8,4,2}
print(b)
print(a-b)
print(b-a)
# length of the set 

a= {1,2,3,4}
print(len(a))
print(len(b))
#checking whether an item is in the set using in memebership operator 
print(5 in a )
print(3 in b)
print(2 in a and 4 in a )
print(5 in b or 6 in b)
# adding items to a set 
#To add one item  we use add
a.add(5)
print(a)
b.add(9)
print(b)
# to add multiple items we use update 
a.update([5,6,7,8,9])
print(a)
b.update([11,12,13])
print(b)
# removing items in a set 
a.remove(2)
print(a)
b.discard(13)
print(b)
a.pop()
print(a)
set_3=a.union(b)
print(set_3)
a.update(b)
print(a)
# intersection 
x={1,2,3,4}
y={4,6,7,8}
print(x.intersection(y))
print(y.union(x))
print(x.difference(y))
print(y.difference(x))
print(x.issubset(y))
print(y.issubset(x))
print(x.issuperset(y))
print(y.issuperset(x))

print(y.symmetric_difference(x))
print(x.isdisjoint(y))
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'} 
A = {19, 22, 24, 20, 25, 26} 
B = {19, 22, 20, 25, 26, 24, 28, 27} 
age = [22, 19, 24, 25, 26, 24, 25, 24] 
print(len(it_companies))
it_companies.add("Twitter")
it_companies.update(['X','Tik tok', 'youtube'])
print(it_companies)
it_companies.remove("Facebook")
print(it_companies)
#When you use remove if the thing that you want to remove it is not in the set it would give you an error but when you use discard if the item is not exsit it won't give you an error 
it_companies.discard("mohamed ")
print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(B.union(A))
print(A.symmetric_difference(B))
del it_companies, A, B
age_set= set(age)
print(age_set)

#Dictionary 
person = {'first_name':'Mohmaed ','last_name':"Elsadig","Country": "Sudan ","age": 20}
print(person)
print(len(person))
print(person["first_name"])
print(person["Country"],person["age"])
print(person.get("Age"))
person["skills"]= "Python"
person["age"]= 21
print(person)
person.pop("first_name")
person.popitem()
print(person)
person_copy= person.copy()
print(person_copy)
keys=person_copy.keys()
print(keys)
values=person_copy.values()
print(values)
print(person_copy.clear())


dog=dict()
dog={"name":"volt","color":"brown","legs":4,"age":4,'breed':"german shipper"}
student= {"first_name":"Mohamed","last_name":"Elsadig","geneder":"male","age":20,"martial status":"single","skills":["python"],
"country":"Sudan","city":"Khartoum","address":"kampala"}
print(len(student))
print(type(student["skills"]))
student["skills"]= "coding ","football"
print(student)
keys= student.keys()
print(keys)
values=student.values()
print(values)
student.pop("age")
print(student)
del dog

#exeptions
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(result)
except ValueError:
    print("Please enter a number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")

try:
    with open("students.txt", "r") as file:
        data = file.read()
        print(data)

except FileNotFoundError:
    print("The file was not found.")
    
with open("students.txt", "w") as file:
    file.write("John")