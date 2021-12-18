#!/usr/bin/env python
# coding: utf-8
1.What are the two values of the Boolean data type? How do you write them?
Ans:- 1 and 0 are two values of boolean data type. 1 as True and 0 as False2.What are the three different types of Boolean operators?
Ans:- AND, OR and NOT are three boolean operators3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean
values for the operator and what it evaluate ).
Ans:-

1--> True and 0--> False

For not operator (1 input):- 

    Input   Output
       1      0
       0      1
       
 For AND Operator (2 input):-
      
      Input1 Input2  Output(And Result)
          0   0         0
          0   1         0
          1   0         0
          1   1         1

 For OR Operator (2 input):-
      
      Input1 Input2  Output(OR Result)
          0   0         0
          0   1         1
          1   0         1
          1   1         14. What are the values of the following expressions?

(5>4) and (3 == 5)
Ans:- False

not (5>4)
Ans:- False

(5>4) or (3 == 5)
Ans:- True

not ((5>4) or (3 == 5))
Ans:- False

(True and True) and (True == False)
Ans:- False

(not False) or (not True)
Ans:- True5. What are the six comparison operators?
Ans:- Equal to ==
      Greater than >
      Less than <
      Greater than or equal to >=
      Less than or equal to <=
      Not equal to !=6. How do you tell the difference between the equal to and assignment operators? Describe a
condition and when you would use one.

Ans:- Equal is denoted by '==' and Assignment denoted by '='

Assignment operator is to assign value to the variable. eg:- x =5 (5 is stored in the variable x)

Equal to operator compares value. eg:- x==6 (5 is stored in x and will be compared with 6)

If we want to store variable we will use assignment operator and if we want to compare and evaluate values with stored variable we will use equal to operator7. Identify the three blocks in this code:
spam = 0
if spam == 10:
print('eggs')
if spam > 5:
print('bacon')
else:
print('ham')
print('spam')
print('spam')

Ans:- Indentation is missing for 2 if condition and 1 else condition. See below correct code. 


spam = 0
if spam == 10:
    print('eggs')
if spam > 5:
    print('bacon')
else:
    print('ham')
print('spam')
print('spam')8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
Greetings! if anything else is stored in spam.

Ans:-

spam = int(input("Enter the number:- "))

if spam ==1:
    print("Hello")
elif spam ==2:
    print("Howdy")
else:
    print("Greetings!")9.If your programme is stuck in an endless loop, what keys you’ll press?

Ans:- Ctrl+C10. How can you tell the difference between break and continue?

Ans:- If the loop is terminated immediately once the condition is True BREAK is used (Loop is breaked)
      If the loop is not met for a condition once then Continue is used (1 iteration is not executed)11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

Ans:- There is no difference between range(10),range(0, 10) and range(0, 10, 1) as python takes start as 0 and step_size as 1 as default. (If start and step_size are not defined)12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
program that prints the numbers 1 to 10 using a while loop.

Ans:-

For Loop:-

for i in range(1,11):
    print(i)
    
While Loop:-

i = 1
while (i <= 10):
    print(i)
    i=i+113. If you had a function named bacon() inside a module named spam, how would you call it after
importing spam?

Ans:- spam.bacon()