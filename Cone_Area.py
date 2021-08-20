pi=22/7
height = float(input("Enter the height of cone: "))
radian = float(input("Enter the radius of cone: "))
x = input("Enter V for calculating the Volume: ")
if x == 'V':
    def cone_volume():
        volume = (pi * radian * radian * height)/3
        print("The volume of cone is: ", volume)
    cone_volume()
elif x != 'V':
    print("Please try with the correct input")
    