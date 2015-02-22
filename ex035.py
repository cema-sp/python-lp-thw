from sys import exit

def gold_room():
  print "This room is full of gold. How much do you take?"
  choice = raw_input("> ")
  if "0" in choice or "1" in choice:
    how_much = int(choice)
  else:
    dead("Learn to type numbers!")

  if how_much < 50:
    print "Nice, you're not greedy, you win!"
    exit(0)
  else:
    dead("You greedy bastard!")

def dead(why):
  print why, "Good job!"
  exit(0)

def start():
  gold_room()

# -------------

start()

