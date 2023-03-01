import math

# 求一元二次方程ax²+bx+c（a≠0）的根，由方程系数a，b，c确定，将a，b，c代入式子就得到方程的根

a = -1
b = 2
c = 3

print((-b + math.sqrt(b**2 - 4*a*c))/(2*a))
print((-b - math.sqrt(b**2 - 4*a*c))/(2*a))


