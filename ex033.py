# ------- functions ---------

def my_function(n, number):
  i = 0
  while i < n:
    print "At the top i is %d" % i
    numbers.append(i)

    i += 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

# ------- program ---------

numbers = []

my_function(6, numbers)

print "The numbers: "

for num in numbers:
  print num

