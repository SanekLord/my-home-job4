# перемножение всех нечётных в диопозоне от 1 до 100
print("Hello, I am multiplying numbers in a range.")
print("For example in the range from 1 to 100. I have multiplied all odd numbers:")
memory = 1
for i in range(1, 100, 1):
    if i % 2 != 0:
        memory *= i
print(memory)
print("Now give me your numbers")
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
znak = input("If you need to multiply even then enter |even| if odd, then |odd| or all in a row |no|")
memory1 = 1
for i in range(num1, num2 + 1, 1):
    if znak == "even":
        if i % 2 == 0:
            memory1 *= i
    elif znak == "odd":
        if i % 2 != 0:
            memory1 *= i
    elif znak == "no":
        memory1 *= i
print("Your response:", memory1)

