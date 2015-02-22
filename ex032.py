the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']

for number in the_count:
  print "This is count: %d" % number

elements = []
elements_r = range(0, 6)

for i in range(6, 12):
  print "Adding %d to the list." % i
  elements.append(i)

for i in elements_r:
  print "Element: %d" % i

