"""
print('Hello , World!')

identify = '지구인'
number_of_legs = 4
print('안녕!',identify,'이야,','나는 다리가',number_of_legs,'개 있어');


my_name = 'python';
my_age = 29;

print (my_name,' 은 이제 ',my_age, '살');

my_next_age = 26
print ('내년에는 이제', my_next_age, '살');

multiply = 9 * 9 
divide = 30 / 5
power = 2 ** 10
reminder = 15 % 4

print(multiply, divide, power, reminder)

text = '2015' + '1991'
number = 2015 + 1991

print(text, number)
"""
# 함수

def print_sqrt():
	r1 = (-b + (b ** 2 - 4 * a * c ) ** 0.5) / (2 * a)
	r2 = (-b - (b ** 2 - 4 * a * c ) ** 0.5)/ (2 * a)
	
	print('해는 {} 또는 {}'.format(r1, r2))
	
a = 1
b = 2
c = -8

print_sqrt()

#함수2
def print_root(a, b, c):
	print(a,b,c)

x = 5
y = 4
z = 3
print_root(x, y, z)

def print_rounded(number):
	rounded = round(number)
	print(rounded)

print_rounded(4.6)
print_rounded(5.1)
print_rounded(2.9)

def add_10(value):
	result = value + 10
	return result

retVal = add_10(42)
print(retVal)
