l = float(input("Enter the length of the cuboid: "))
b = float(input("Enter the breadth of the cuboid: "))
h = float(input("Enter the height of the cuboid: "))
def cubiod_area():
    a = 2((l*b)+(b*h)+(h*l))
    print("The area of cubiod is: ", a)
cubiod_area()
x = input("Enter V for calculating the volume: ")
if x == 'V':
    def cubiod_volume():
        Volume = l*b*h
        print("The volume of cube is: ", Volume)
    cubiod_volume()
elif x != 'P':
    print("Please Enter with correct input and try again")
    