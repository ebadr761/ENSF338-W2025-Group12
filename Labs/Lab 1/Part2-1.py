import sys                      # imports the sys library
import math                     # imports the math library
def do_stuff():                 # creates a function that tries to find the solution
                             #to a quadratic equation by checking if the discriminant
   a = float(sys.argv[1])      # is greater than 0, if so use the quadratic formula,
   b = float(sys.argv[2])      # or if the discriminant is 0, then solutions are 0, or
   c = float(sys.argv[3])      # if the discriminant is negative, if so no solutions
   d = b**2 - 4*a*c            
   if d > 0:                   
       root1 = (-b + math.sqrt(d)) / (2*a)
       root2 = (-b - math.sqrt(d)) / (2*a)
       print(f'The solutions are: {root1}, {root2}') #FIXED CODE: removed faulty apostrophe with correct '
   elif d == 0:                 
       root = -b / (2*a)
       print(f'The solution is: {root}')             #Closes the quotation correctly now
   else:
       print('There are no real solutions.')         #Here as well.

do_stuff()
