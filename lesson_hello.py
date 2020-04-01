import math
# print("------------------------------------------------------")
# length = 10
# width = 20
# rectangle_square = length * width
# #print("Площадь прямоугольника:",rectangle_square)
# print("Площадь треугольника при ширине %d  см. и длине %d см. равна: %d кв. см."
#       % (width,length,rectangle_square))
# print("------------------------------------------------------")
# catheter1 = 6
# catheter2 = 4
# hypotenuse = math.sqrt(catheter1**2 + catheter2**2)
# print("Гипотенуза при первом катете %d см. и втором катете %d см.  равна: %.2f " % (catheter1,catheter2,hypotenuse))
# print("------------------------------------------------------")
# radius = 4
# area_of_a_circle = math.pi * (radius**2)
# print("Площадь круга при числе Пи %.2f и радиусе %d м. равна : %.3f" % (math.pi,radius,area_of_a_circle))
#First
a = 53
b = 23
c = 4
summ = a * b * ( c/2 )
print("Сумма при a = %d , b = %d , c = %d равна : %.3f" % (a,b,c,summ ) )
print("Second")
summ2 = (a**2 * b**2) % 2
print("Сумма при a = %d , b = %d  равна : %f" % (a,b,summ2 ) )
print("Third")
summ3 = (a + b) / 12 * c % 4 + b
print("Сумма при a = %d , b = %d , c = %d равна : %.3f" % (a,b,c,summ3 ) )
print("fourth")
summ4 = (a + b * c) / (a * b) % c
print("Сумма при a = %d , b = %d , c = %d равна : %.3f" % (a,b,c,summ4 ) )
print("fifth")
summ5 = abs(a * b) / (a - b)**3 - math.cos(c)
print("Сумма при a = %d , b = %d , c = %f равна : %.3f" % (a,b,math.cos(c),summ5 ) )
print("sixth")
a1 = 4
b1 = 7
c1 = 0.2
summ6 = (math.log(1 - c1) / - b1)**2 + abs(a1)
print("Сумма при a = %d , b = %d , c = %f равна : %.3f" % (a1,b1,c1,summ6 ) )



