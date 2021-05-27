# This function has a variable with
# name same as s.
def f():
    s = "local"
    print(s)
 
# Global scope
s = "global"
f()
print(s)