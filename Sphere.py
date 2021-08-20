r = float(input("Enter the radius of the sphere: "))
x = input("Enter P for Perimeter, A for Area and V for volume: ")
if x == 'P':
    def sphere_perimeter():
        p = 4*3.14*r
        print("Perimeter of the sphere is: ", p)
    sphere_perimeter()
elif x == 'A':
    def sphere_area():
        a = (4*3.14*r*r)
        print("Area of sphere is: ", a)
    sphere_area()
elif x == 'V':
    def sphere_volume():
        v = (4*3.14*r*r*r)/3
        print("Volume of sphere is: ", v)
    sphere_volume()
else:
    print("You have entered the wrong choice, please try again")
