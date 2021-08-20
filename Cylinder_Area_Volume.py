pi=22/7
height = float(input("Enter the height of cylinder: "))
radian = float(input("Enter the radius of cylinder: "))
def cylinder_area():
    sur_area = ((2*pi*radian) * height) + ((pi*radian**2)*2)
    print("The area of cylinder is: ", sur_area)
cylinder_area()
x = input("Enter V for calculating the Volume: ")
if x == 'V':
    def cylinder_volume():
        volume = pi * radian * radian * height
        print("The volume of cylinder is: ", volume)
    cylinder_volume()
elif x != 'V':
    print("Please try with the correct input")
    
