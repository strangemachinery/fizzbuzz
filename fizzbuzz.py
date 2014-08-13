
my_input = int(raw_input("Enter a number:"))
print type(int(my_input))
for i in range(my_input, 101):
    if i % 3 == 0:
	print "fizz",
	continue
    elif i % 5 == 0:
	print "buzz",
    elif i % 3 == 0 and i % 5 == 0:
	print "fizz buzz",
    else: 
	print i, 
