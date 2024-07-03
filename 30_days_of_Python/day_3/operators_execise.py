age = 31
height = 5.11
complex_num = 1 + 1j

print('Find the area of the Triangle')

Enter_Base = float(input('Enter Base: '))
Enter_Height = float(input('Enter Height: '))
Area_of_the_Triangle = 0.5 * Enter_Base * Enter_Height

print('Area of Triangle', Area_of_the_Triangle)

print('Find the Perimeter of the Triangle')

Enter_Side_A = input('Enter Side A: ')
Enter_Side_B = input('Enter Side B: ')
Enter_Side_C = input('Enter Side C: ')
Perimeter_of_Triangle = Enter_Side_A + Enter_Side_B + Enter_Side_C

print('Perimeter of Triangle', Perimeter_of_Triangle)

print('Find the area and perimeter of the rectangle')

Length = float(input('Enter Length: '))
Width = float(input('Enter Height: '))
Area_of_Rectangle = Length * Width
Perimeter_of_Rectangle = 2 * (Length + Width)

print('Area of Rectangle', Area_of_Rectangle)
print('Perimeter of Rectangle', Perimeter_of_Rectangle)

print('Calculate the area and circumference of a circle')

Enter_Radius = float(input('Enter Radius: '))
pi = 3.14
area_of_circle = pi * Enter_Radius * Enter_Radius
circumference_of_circle = 2 * pi * Enter_Radius

print('Area of Circle', area_of_circle)
print('Circumference of Circle', circumference_of_circle)

print('Calculate the Slope')

def analyze_linear_equation(m, b):
    slope1 = m
    
    y_intercept = b
    
    x_intercept = -b / m if m != 0 else None
    
    return slope1, x_intercept, y_intercept


m = float(input('Enter Slope: '))
b = float(input('Enter y-intercept'))

slope1, x_intercept, y_intercept = analyze_linear_equation(m, b)

print(f"For the equation y = {m}x + {b}:")
print(f"Slope: {slope1}")
print(f"X-intercept: {x_intercept}")
print(f"Y-intercept: {y_intercept}")

print('Find the Slope and Euclidean Distance')

x1 = 2
y1 = 2
x2 = 6
y2 = 10


Slope2 = ((y2  - y1) / (x2  - x1))

euclidean_distance = ((x2 - x1)**2 + (y2 - y1)**2)

print('Slope2', Slope2)

print('euclidean_distance', euclidean_distance)

print('Comparing the slopes')

print(slope1 == Slope2)

print(len('python'))
print(len('dragon'))
print(len('python') > len('dragon'))


print('on' in 'python' or 'dragon')
print('jargon' in  'I hope this course is not full of jargon')

print('Find the length of python and convert the value to float and convert it to string')

length = len('python')
float_length = float(length)
string_length = str(float_length)

print(string_length)
print(type(string_length))

print('How do you check if a number is even or not using python')

number = float(input('enter number: '))

if number % 2 == 0:
    print(f"{number} is even")
else:
   print(f"{number} is odd")


floor_division = 7 // 3
int_conversion = int(2.7)
comparision_result = floor_division == int_conversion

print(floor_division)
print(int_conversion)
print('Are they equal', comparision_result)


first_num = 10
second_num = 10
result = first_num == second_num
print('Result of if 10 is equal to 10', result)

third_num = int(9.8)
second_result = first_num == third_num
print('Is int 9.8 equal to 10', second_result)

print('Calculate weekly pay')

Enter_Hours = float(input('Enter Hours: '))
Enter_Rate_Per_Hour = float(input('Enter Rate Per Hour: '))
Your_Weekly_Earning_is = Enter_Hours * Enter_Rate_Per_Hour

print('Your Weekly Earnings', Your_Weekly_Earning_is)


print('How many second can you live')
enter_number_of_years = float(input('Number of Years: '))
number_of_seconds = enter_number_of_years * 31556952

print('You have lived for', number_of_seconds, 'seconds.')

print([1,1,1,1,1])
print([2,1,2,4,8])
print([3,1,3,9,27])
print([4,1,4,16,64])
print([5,1,5,25,125])