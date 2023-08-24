'''def area_circle(r):
    area=3.14*r*r  
    return area'''

# Problem: Create a function that takes two numbers as argument and returns the greater of the two.

def compare(a,b):
    if a>b:
        return a
    else:
       return b
            
a = 10
b = 9
c = compare(a,b)
print(f"The greater number  is: {c}")

