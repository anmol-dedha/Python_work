import math

equation=(input('enter the equation in the standard form of Ax^2+Bx+C equation: '))
a_=int(equation.find('x'))


if a_== 0:
    a=1
else:
    a=int(equation[0:a_])

b_=int(equation.find('x',a_+1))
b=int(equation[a_+3:b_])

c_=len(equation)
c=int(equation[b_+2:c_])
# print(b)
# print(c)
# print(a)

root1=float(-b+math.sqrt((b*b)-4*a*c))/(2*a)
root2=float(-b-math.sqrt((b*b)-4*a*c))/(2*a)

print(f'the zeroes of your equation are :{root1} and {root2}')

# print(equation.find[1:0])


