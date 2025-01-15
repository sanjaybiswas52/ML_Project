#Dictionaries
# Like a map or hash table in other languages
captains = {}
captains["Pilibhit"] = "Sanjay"
captains["Dilip"] = "Kanpur"
captains["Neeraj"] = "Bhatiyala Kusalpur"
captains["Ashish"] = "Kanpur"

print(captains["Pilibhit"])
print(captains.get("Dilip"))
print(captains.get("Manoj"))

#Functions
def SquareIt(x):
    return x * x

print(SquareIt(2))

#You can pass functions around as parameters
def DoSomething(f,x):
    return(f(x))

print(DoSomething(SquareIt, 3))

#Lambda functions let you inline simple functions
print(DoSomething(lambda x: x*x*x,3))

#Boolean Expressions
