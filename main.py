#   Interactions Between Functions Practice #1
# Create a function (throw_dice) that "throws" two random dice and returns its results (the function MUST RETURN TWO VALUES AS A RESULT, both of which must be between 1 and 6, randomly).
# from random import randint
# def throw_dice():
#   die1 = randint(1,7)
  
#   die2 = randint(1,7)
#   return die1, die2

# die1, die2 = throw_dice()
# print(die1, die2)

# # Pass the result of these two dice to a function called roll_result (meaning that this second function MUST RECEIVE TWO ARGUMENTS) and return -without printing it- a certain message according to the what the sum of these values results:

# def rolled_dices(die1, die2):
#   sum_dice= die1+ die2
#   if sum_dice <=6:
#     print(f"The sum of your dice is {sum_dice}. Unfortunate")
#   elif sum_dice > 6 and sum_dice<10:
#     print(f"The sum of your dice is {sum_dice}. You have a good chance")
#   else:
#     print(f"The sum of your dice is {sum_dice}. It looks like a winning roll")
    
# rolled_dices(die1, die2)
#####################################################################################################
# return it as a list
# print out lowest to highest
# remove duplicates
# reomove higgest value

# Interactions Between Functions Practice #2
# Create a function called reduce_list() that takes a list (numbers) as an argument, and returns also a list, but removing duplicates (leaving only one of the numbers if there are duplicates) and removing the highest value. The order of the elements can be changed.
numbers_list=[1,3,4,16,3,14,5,6,3]
def reduce_list(numbers_list):
  print("numbers_list:", numbers_list)
  uniqueNumbers=set(numbers_list)
  print("Set of uniqueNumbers:",uniqueNumbers)
  return uniqueNumbers
print(set(numbers_list))

reduce = reduce_list(numbers_list)
print(f"the list is{reduce}")
reduce = list(reduce)
print(f"the list is{reduce}")
def kick_high(reduce):
  reduce.remove(max(reduce))
  print(f"the final list is {reduce}")
  # return y

kick_high(reduce)


  




  

  
  
  
# For example, if given the list [1,2,15,7,2] it should return [1,2,7].

# Create a function called average() that can receive as an argument the list returned by the previous function, and that calculates the average of its values. It should return the result (a float), without printing it.





#####################################################################################################
# Interactions Between Functions Practice #3
# You must create a list with values and call it secret_codes.

# Create a function called toss_coin that returns the result of a random coin toss. Such a function must be able to return the results "Heads" or "Tails", and must not receive any arguments to work.

# Create a second function called luck, that takes two arguments: the first must be the result of the coin toss. The second argument will be any list (the secret_codes variable that was created at the beginning).

# If the coin comes up "Tails", luck should print this message to the user: "List will self-destruct", and return said list as empty list = [ ].

# If the coin comes up "Heads", it should print to the screen: "List was saved" and return the list intact.

# Hint: Use the random library's choice method to choose an element at random from a sequence.