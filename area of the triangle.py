a = float(input("Enter the length of first side: " ))
b = float(input("Enter the length of second side: " ))
c = float(input("Enter the length of third side: " ))

p = a + b + c
s = (a + b + c) * .5

area = (s * (s-a) * (s-b) * (s-c)) **.5

print("perimeter of triangle is", p)
print("semi perimeter of triangle is", s)
print("area of triangle is", area)