from sys import argv

script, filename = argv

print "The file \"%s\" will be truncated!" % filename
raw_input("Are you sure (^C to quit)?")

target = open(filename, 'w')

target.truncate()

print "Now we will fill file with text."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

target.write(line1 + "\n")
target.write(line2 + "\n")
target.write(line3 + "\n")

target.close()

