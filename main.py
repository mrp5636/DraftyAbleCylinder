# Author: Miranda Palmer mrp5636@psu.edu
def getGradePoint(letter):
  if letter == "A":
    point = 4.0
  elif letter == "A-":
    point = 3.67
  elif letter == "B+":
    point = 3.33
  elif letter == "B":
    point = 3.0
  elif letter == "B-":
    point = 2.67
  elif letter == "C+":
    point = 2.33
  elif letter == "C":
    point = 2.0
  elif letter == "D":
    point = 1.0
  else:
    point = 0.0
  return point

def run():
  creditsum = 0
  partsum = 0
  for x in range (1,4):
    letter = input(f"Enter your course {x} letter grade: ")
    credit = int(input(f"Enter your course {x} credit: "))
    print(f"Gradepoint for course {x} is: {getGradePoint(letter)}")
    part = getGradePoint(letter)*credit
    creditsum = credit + creditsum
    partsum = part + partsum
  GPA = partsum/creditsum
  print(f"Your GPA is: {GPA}")
    
  """
  Use either a while-loop or a for-loop to make your code for getting three separate
  courses' letter grade and credit info. And calculate the final GPA.
  YOU CAN NOT use any features/data structures we haven't learned in the class,
  including but not limited to list, dictionary, and tuples.
  """
  return

if __name__ == "__main__":
  run()
