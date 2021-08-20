pi = 22/7
Radius = float(input("Enter the radius of circle: "))
def circle_circumference():
    a = 2*pi*Radius
    print("The circumference of circle is: ", a)
circle_circumference()
x = input("Enter A for calculating the area: ")
if x == 'A':
    def circle_area():
        a = pi*Radius*Radius
        print("The area of circle is: ", a)
    circle_area()
elif x != 'P':
    print("Please Enter with correct input and try again")