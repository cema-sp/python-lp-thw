pi_ = 3.1415

class MyClass:

  global pi_ 
  t_ = True
  f_ = False
  n_ = None

  hello_ = "\t\vHello!\a"
  enums_list_ = ["one", "two", "three"]
  enums_dict_ = {"four": 4, "five": 5, "six": 6}

  def greet(self):
    print "Greeting: %s" % self.hello_

  def unimplemented(self): pass

  def logic(self):
    if self.f_:
      print "%r is true." % self.f_
    elif self.n_:
      print "%r is true." % self.n_
    elif self.t_:
      print "%r is true." % self.t_
    else:
      raise ValueError("ERROR")

  def radius(self):
		print "Enter R: "
		r_raw = raw_input("> ")

		try:
			r = int(r_raw)
			area = pi_ * r**2
			print "Area is %g." % area
		except ValueError, e:
			print "%r is not a valid integer (%s)!" % (r_raw, e)

# ----------- main ---------------

my_object = MyClass()
my_object.greet()
my_object.unimplemented()
my_object.logic()
my_object.radius()

