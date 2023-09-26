def calculate_power(value, power):
	ans = 1
	for i in range(power, 0, -1):
		ans *= value
	return ans

x = int(input("Enter value: "))
y = int(input("Enter the power: "))

print(calculate_power(x, y))

