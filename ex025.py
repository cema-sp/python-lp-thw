# to use this file type `import ex025`
# for help type in console `help(ex025)` or\
# `help(ex025.break_words)`

def break_words(text):
  '''Splits sentence with space delimiter'''
  return text.split(' ')

def sort_words(words):
  '''Sorts list of words'''
  return sorted(words)

def print_first_word(words):
  '''Prints the first word in list'''
  print words.pop(0)

def print_last_word(words):
  '''Prints the last word in list'''
  print words.pop(-1)

