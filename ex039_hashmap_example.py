import ex039_hashmap as hashmap

states = hashmap.new(10)
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')

cities = hashmap.new(10)
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'FL', 'Jacksonville')
hashmap.set(cities, 'OR', 'Portland')

print '-' * 20
print "CA state has city: ", hashmap.get(cities, 'CA')

print '-' * 20
hashmap.list(cities)

print '-' * 20
hashmap.dump(cities)

print '-' * 20
st = hashmap.get(states, 'Texas')

if not st:
  print "No state for Texas"

ct = hashmap.get(cities, 'TX', 'Default city')
print "City for TX: ", ct

