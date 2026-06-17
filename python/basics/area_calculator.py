print("Choose shape:")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")
choice = int(input("Enter choice (1/2/3): "))
if choice == 1:
    radius = float(input("Enter radius: "))
    area = 3.14 * (radius ** 2)
    print("Area of Circle:", round(area, 2))
 
elif choice == 2:
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = length * width
    print("Area of Rectangle:", area)
 
elif choice == 3:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = 0.5 * base * height
    print("Area of Triangle:", area)
 
else:
    print("Invalid choice")
