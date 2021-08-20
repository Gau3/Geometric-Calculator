l = float(input("Enter the length of the cube: "))
def cube_area():
    a = 6*l*l
    print("The area of cube is: ", a)
cube_area()
x = input("Enter V for calculating the volume: ")
if x == 'V':
    def cube_volume():
        Volume = l*l*l
        print("The volume of cube is: ", Volume)
    cube_volume()
elif x != 'P':
    print("Please Enter with correct input and try again")
    