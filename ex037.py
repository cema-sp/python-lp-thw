from os import name

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
    return "Greeting: %s" % self.hello_
  
  def greet_me(self):
    print "Enter your name: "
    name_raw = raw_input("> ")
    print "Greeting: %s, %s" % (self.hello_, name_raw)

  def unimplemented(self): pass

  def logic(self):
    if not self.f_ and not self.n_:
      print "%r is false, %r is false." % (self.f_, self.n_)
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
      sqr = lambda x: x**2
      area = pi_ * sqr(int(r_raw))
      print "Area is %g." % area
    except ValueError, e:
      print "%r is not a valid integer (%s)!" % (r_raw, e)
    finally:
      print "Finished correctly"

  def loop(self, n):
    assert n < 10, "FUUUUUU~~~~"
		
    if n < 0:
      raise ValueError("n should be positive")
    else: pass

    for i in range(n):
      if i is not 2:
        print "i = %d" % i
      else:
        i += 1
        continue
      exec 'print "Next iteration!"'
      if i is 7: break
      else: pass

  def call_loop(self):
    print "Loop n: "
    n_raw = raw_input("> ")
    n = int(n_raw)
    self.loop(n)

class Controlled:
  v_ = "value"

  def __enter__(self):
    print "calling __enter__"
    self.v_ += " 1"
  
  def __exit__(self, type, value, traceback):
    print "calling __exit__"

def yield_function():
  yield "HELLO"

def yield_generator():
	for i in range(3):
		yield i**i

# ----------- main ---------------

my_object = MyClass()
print my_object.greet()
my_object.greet_me()
my_object.unimplemented()
my_object.logic()
my_object.radius()
my_object.call_loop()

with Controlled() as contr:
  print "Value of \"v_\": %r" % "UNKNOWN"

print "OS name: %r" % name

yield_function().next()

for i in yield_generator():
	print "Generating: %d" % i

