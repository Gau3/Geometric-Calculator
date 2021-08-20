l = float(input("Enter the length of the rectangle: "))
b = float(input("Enter the breadth of the rectangle: "))
def rectangle_area():
    a = l*b
    print("The area of rectangle is: ", a)
rectangle_area()
x = input("Enter P for calculating the perimeter: ")
if x == 'P':
    def rectangle_perimeter():
        P = l+b
        print("The perimeter of rectangle is: ", P)
    rectangle_perimeter()
elif x != 'P':
    print("Thank you")
    
    
