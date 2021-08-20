l = float(input("Enter the length of the square: "))
def square_perimeter():
    P = 4*l
    print("The length of square is: ", P)
square_perimeter()
x = input("Enter A for calculating the area: ")
if x == 'A':
    def square_area():
        A = l*l
        print("The volume of cube is: ", A)
    square_area()
elif x != 'P':
    print("Please Enter with correct input and try again")
    