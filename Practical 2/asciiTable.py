lower = 10
upper = 100
print("Enter a number ({0}-{1}):".format(lower,upper))

for i in range(10, 120, 11):
    print("{:<3} {:>3}".format(i, chr(i)))