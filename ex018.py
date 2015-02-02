def print_two(*args):
  arg1, arg2 = args
  print "arg1: %r, arg2: %r" % (arg1, arg2)
  return arg2, arg1

print "C = %s, D = %s" % (print_two("A", "B"))

