# Generate a Hailstone sequence
numString = raw_input("Enter a positive integer: ")
num = int(numString)
count = 0

print("Starting with number: %s" % num)
print("Sequence is: ")

while num > 1:
    if num % 2:
        num = num * 3 + 1
    else:
        num = num / 2
    print num
    count += 1

else:
    print
    print("Sequence is %s numbers long" % num)
