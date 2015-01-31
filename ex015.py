from sys import argv

script, filename = argv

txt = open(filename)

print '*' * 20
print "Here is you file \"%s\"" % filename
print txt.read()
print '*' * 20

txt.close()

