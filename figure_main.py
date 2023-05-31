import figure

myline = figure.line(10, 20)

width, height = myline.get_length()
# implement exception handler
rectangle = figure.area_rectangle(width, height)
print(rectangle)

myline.set_length(20, 30)
width, height = myline.get_length()
# implement exception handler
triangle = figure.area_right_triangle(width, height)
print(triangle)

myline.set_length(30, 40)
width, height = myline.get_length()
# implement exception handler
ellipse = figure.area_ellipse(width, height)
print(ellipse)
