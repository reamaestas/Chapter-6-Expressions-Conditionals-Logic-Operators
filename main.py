# Run the code as-is first.
name = 'Cynthia'
other_name = 'Rose'

print(name, other_name, name == other_name)

name = other_name

print(name, other_name)

# Replace the assignment statement on line 7 with other_name = name.
other_name = 'Rea'
print(name, other_name)

# Does the output change?
#YEP

# Does name = other_name behave the same way as other_name = name?
#YES

# What happens when you try print(name = other_name)?
# Throws name = input('Please enter a username: ')
print('------ IF STATEMENTS ----------------')

num = 10
if num < 0:
	print("opps!", num, "is too small!")

	#print("Indention matters!")
	#this indention wont work
print("Indention matters!")
#this is the proper indention


print('-----ELSE ---------')
user_name = input("Enter Full Name:")
if len(user_name) >= 5 and len(user_name) < 10:
   print("Welcome, " + user_name + "!")
else:
   print("Invalid.")
print('--------')
book_title = 'Little Fires Everywhere'
book_status = 'overdue'

if book_status == 'overdue':
	print(book_title + ' is overdue!')

else:
	print('No overdue books!')

print('-----AND OPERATOR---------')

name = 'Caroline'

print(name)
print('Longer than 5 characters: ', len(name)>5)
print('Shorter than 10 characters: ', len(name)<10)
print('len(name) > 5 and len(name) < 10: ', len(name) >5 and len(name) <10)
print(len(name)>3 and "cat" == "cat")
print(len(name)>3 and "cat" == "dog")

print('------- OR OPERATOR-------------')
num = 5
print(num>0 or num<10)
print(7> num or num == 3)
print(num*5 >100 or 'dog' == 'cat')

print('-----logic NOT OPERATOR---------------')

print(not True)
print(not False)

number = 5

print( not(number<7) )
print( not('dog' == 'cat') )
print( not(number*5 > 100 or 'dog' == 'cat') )

print('--------------------')
num1 = 5
python = 'Awesome'

print(num1 > 0 and num1 < 10 and 'dog' == 'cat')
print(num1 >7 or num1 == 3 or 'dog' == 'cat' or python == 'Awesome' )

print(num1 == 5 or num1 == 6 or num1 == 7)

print('------ORDER OF OPTERATIONS--------------')
print('1: math calculations', '\n2: evaluates comparisons as T/F', '\n3: applies all not operators', '\n4: evaluates and/or operations')

print('\n-----OPERATOR ORDER---------------')
print('parentheses ( )\nexponent **\nmultiplication and division * / // %\naddition and subtraction + -\ncomparison == != <= >= > <\nlogic not\nlogic and\nlogic or')
print('------NESTED CONDITIONALS--------------')

entry = int(input("Enter a whole number:"))

if entry%2 == 0:
	print('EVEN')
if entry > 0:
	print('POSITIVE')

#each if statement is independent

entry1 = int(input("Enter a whole number:"))

if entry1 % 2 == 0:
	print('EVEN')
	if entry1 > 0:
		print('POSITIVE')

#indentions matter!!!!
print('-----------ELSE---------')
word = input("Enter Word:")

if len(word) == 4:
	print("What did your mom tell you about 4 letter words?")
else:
	if len(word) < 4:
		print("You can think of a longer word than that!")
	else:
		print("Execellent word!")

#the indention tells us exactly which else clause belongs to which if statemet
print('--------------------')
num2 = 7

if num2 % 2 == 0:
	if num2 % 2 == 1:
		print("odd")
print(" \nthis doesnt return anything because the first if statement is False.")
print("\n-- lets make the first if statement true--")

if num2 % 2 != 0:
	if num2 % 2 == 1:
		print("odd")

print('----- Check you Understanding---------')

answer_1 = 'yes'
answer_2 = 'no'


if answer_1 == 'yes':
   if answer_2 == 'yes':
      print("Both of you agree!")
   else:
      print("You two need to work this out.")
else:
   if answer_2 == 'yes':
      print("Stop arguing and work it out.")
   else:
      print("Clean your bathroom anyway!")

print('-------CHAINED CONDITIONALS-------------')
#if one check in the series evaluates T then the following are ignored

#elif

the_num = 10
other_num = 20

if the_num > other_num:
	print(the_num, "is greater than", other_num)
elif the_num < other_num:
	print(the_num, "is less than", other_num)

else: 
	print(the_num, "is equal to", other_num)
print('--------multiple elif statements-----')

character = 'P'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'

if character in lowercase:
   print(character, 'is a lowercase letter.')
elif character in uppercase:
   print(character, 'is an UPPERCASE letter.')
elif character in digits:
   print(character, 'is a number.')
else:
   print('&**%#!', character, 'is a punctuation mark or a space.')
print('-----NESTED VS CHAINED CONDITIONALS-----')
#NESTED
user_word = input('Please enter a word: ')

if len(user_word) == 4:
   print("What did your mom tell you about using 4-letter words?")
else:
   if len(user_word) < 4:
      print("You can think of a longer word than that!")
   else:
      print("Excellent word!")
#CHAINED
user_word1 = input('Please enter a word: ')

if len(user_word1) == 4:
   print("What did your mom tell you about using 4-letter words?")
elif len(user_word1) < 4:
   print("You can think of a longer word than that!")
else:
   print("Excellent word!")
print('-----nesting check within a check---------------')
'''
if condition_1:
   # code here

   if condition_2:
      # code here

      if condition_3:
         # code here
      else:
         # code here

   else:
      # code here

else:
   # code here
'''

print('--------------------')

print('--------------------')
print('--------------------')
print('--------------------')
