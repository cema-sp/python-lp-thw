states = {
  'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA'
}

cities = {
  'CA': 'San Francisco',
	'FL': 'Jacksonville'
}

cities['OR'] = 'Portland'

print '-' * 20
print 'Florida city: ', cities[states['Florida']]

print '-' * 20
for state, abbr in states.items():
	print "%s is abbriviated %s" % (state, abbr)

print '-' * 20
# safe get
st = states.get('Texas')
if st:
  print "Texas state: ", st
else:
  print "No state for Texas"

# get with default value
ct = cities.get("TX", "Default value")
print "City for TX: ", ct

