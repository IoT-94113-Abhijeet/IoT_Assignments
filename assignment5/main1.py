from geometry import area_circle, area_rectangle

radius = float(input("Enter radius of the circle: "))
length = float(input("Enter length of the rectangle: "))
width = float(input("Enter width of the rectangle: "))

circle_area = area_circle(radius)
rectangle_area = area_rectangle(length, width)

print("Area of Circle:", circle_area)
print("Area of Rectangle:", rectangle_area)
