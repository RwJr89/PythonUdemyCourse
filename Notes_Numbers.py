Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 00:48:40) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2 + 3
5
>>> 100 - 20
80
>>> 2 * 2
4
>>> 2 / 4
0.5
>>> 10 / 5
2.0
>>> type(2)
<class 'int'>
>>> type(0.5)
<class 'float'>
>>> 5 % 3
2
>>> 10 % 2
0
>>> 7.5 % 5
2.5
>>> 2 * 5 - 1
9
>>> 2 * ( 5 - 1 )
8
>>> import random
>>> random.randint (10, 20)
19
>>> random.randint ( 10, 100)
62
>>> potion_health = random.randint (25, 50)
>>> 
==== RESTART: /Volumes/Coding/Python Codes/Python Bible/health_potion.py ====
79
>>> 
==== RESTART: /Volumes/Coding/Python Codes/Python Bible/health_potion.py ====
99.0
>>> 
==== RESTART: /Volumes/Coding/Python Codes/Python Bible/health_potion.py ====
96
>>> 
==== RESTART: /Volumes/Coding/Python Codes/Python Bible/health_potion.py ====
60
>>> round (2.1)
2
>>> round(1.5)
2
>>> import math
>>> round (1.5)
2
>>> math.floor (1.5)
1
>>> mat.ceil(2.1)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    mat.ceil(2.1)
NameError: name 'mat' is not defined
>>> math.ceil(2.1)
3
>>> math.pie
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    math.pie
AttributeError: module 'math' has no attribute 'pie'
>>> math.pi
3.141592653589793
>>> math.e
2.718281828459045
>>> math.sin( math.pi /2  )
1.0
>>> math.sin( math.pi / 2 )
1.0
>>> math.sin( math.pi)
1.2246467991473532e-16
>>> math.floor(math.sin(math.pi))
0
>>> math.cos( 0 )
1.0
>>> math.asin( 0 )
0.0
>>> math.acos( 0 )
1.5707963267948966
>>> math.hypot(3, 4)
5.0
>>> mat.pow(2,3)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    mat.pow(2,3)
NameError: name 'mat' is not defined
>>> math.pow(2,3)
8.0
>>> 2 ** 3
8
>>> math.pow(9,2)
81.0
>>> 9 ** 2
81
>>> math.exp(2)
7.38905609893065
>>> math.log(math.e)
1.0
>>> math.log10(1000)
3.0
>>> math.log2(8)
3.0
>>> import random

health = 50

difficulty = 3

potion_health = int (random.randint (25, 50) / difficulty)

health = health + potion_health

print(health)

SyntaxError: multiple statements found while compiling a single statement
>>> 
===== RESTART: /Volumes/Coding/Python Codes/Python Bible/hello_world.py =====
Hello world
>>> 
>>> A = " part one"
>>> B = "part two"
>>> A + B
' part onepart two'
>>> A = "part one"
>>> B = "part two"
>>> A + B
'part onepart two'
>>> A * 3
'part onepart onepart one'
>>> "=" * 20
'===================='
>>> print("TITLE")
TITLE
>>> "=" * 20
'===================='
>>> A = "part"
>>> B = 1
>>> A + B
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    A + B
TypeError: can only concatenate str (not "int") to str
>>> A + str(B)
'part1'
>>> "{} - {}".format(A,B)
'part - 1'
>>> 
>>> "{1} - {0}".format(A,B)
'1 - part'
>>> 
====== RESTART: /Volumes/Coding/Python Codes/Python Bible/hello_you.py ======
What is your name?: Rawle Williams
How old are you?:30
What city do you live in?:Jacksonville
What do you love doing?:Gaming
Your name is  Rawle Williams and you are 30 years old. You live in Jacksonville and you love Gaming
>>> "hello".count(e)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    "hello".count(e)
NameError: name 'e' is not defined
>>> string.method()
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    string.method()
AttributeError: 'str' object has no attribute 'method'
>>> "hello".count("e")
1
>>> text = "happy birthday"
>>> text.count("a)
	       
SyntaxError: EOL while scanning string literal
>>> text.count("a")
	       
2
>>> text.count("day")
	       
1
>>> x = "Happy Birthday"
	       
>>> x.lower()
	       
'happy birthday'
>>> x.upper()
	       
'HAPPY BIRTHDAY'
>>> x
	       
'Happy Birthday'
>>> x = x.upper()
	       
>>> x
	       
'HAPPY BIRTHDAY'
>>> x.capitalize()
	       
'Happy birthday'
>>> 
	       
>>> 
	       
>>> 
	       
>>> 
	       
>>> x.title()
	       
'Happy Birthday'
>>> x = x.title()
	       
>>> x
	       
'Happy Birthday'
>>> x.islower()
	       
False
>>> x.isupper()
	       
False
>>> x.istitle()
	       
True
>>> x.isalpha()
	       
False
>>> "abcd".isalpha()
	       
True
>>> "123".isdigit()
	       
True
>>> y = "happybirthday!123"
	       
>>> y.isalnum()
	       
False
>>> y = "happybirthday123"
	       
>>> y.isalnum()
	       
True
>>> x = "happy birthday"
	       
>>> x.index("birthday")
	       
6
>>> x.index("jbfghveh")
	       
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    x.index("jbfghveh")
ValueError: substring not found
>>> x.find("birthday")
	       
6
>>> x.find("adjae")
	       
-1
>>> x.index("Birthday")
	       
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    x.index("Birthday")
ValueError: substring not found
>>> x.find("Birthday")
	       
-1
>>> y = "00000Bday0000"
	       
>>> y.strip("0")
	       
'Bday'
>>> y.lstrip("0")
	       
'Bday0000'
>>> y.rstrip("0")
	       
'00000Bday'
>>> name = input("What is your name?:")
	       
What is your name?:Zee
>>> print(name)
	       
Zee
>>> len(name)
	       
3
>>> name = input("What is your name?:").strip()
	       
What is your name?:Rawle     
>>> print(name)
	       
Rawle
>>> len(name)
	       
5
>>> word = "supercalifragilisticexpialidocious"
	       
>>> word[0]
	       
's'
>>> word
	       
'supercalifragilisticexpialidocious'
>>> word[2]
	       
'p'
>>> variable[start:end:step}
	       
SyntaxError: invalid syntax
>>> variable[start:end:step]
	       
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    variable[start:end:step]
NameError: name 'variable' is not defined
>>> word[0:5:1]
	       
'super'
>>> word[0:5:2]
	       
'spr'
>>> word[5:9:1]
	       
'cali'
>>> word[5:]
	       
'califragilisticexpialidocious'
>>> word[5::2]
	       
'clfaiitcxildcos'
>>> word[:7]
	       
'superca'
>>> word[:8]
	       
'supercal'
>>> word[;5]
	       
SyntaxError: invalid syntax
>>> word[:5]
	       
'super'
>>> word[::-1]
	       
'suoicodilaipxecitsiligarfilacrepus'
>>> 
======== RESTART: /Volumes/Coding/Python Codes/Python Bible/slices.py ========
>>> string = "happy_birthday"
	       
>>> string[:]
	       
'happy_birthday'
>>> string[:birthday]
	       
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    string[:birthday]
NameError: name 'birthday' is not defined
>>> string[: string.index("_")]
	       
'happy'
>>> string[0: string.index("birthday')]
			   
SyntaxError: EOL while scanning string literal
>>> string[0: string.index("birthday")]
			   
'happy_'
>>> # here is a very long word

word = "antidisestablishmentarianism"
word[7:19:1]
			   
SyntaxError: multiple statements found while compiling a single statement
>>> word
			   
'supercalifragilisticexpialidocious'
>>> word = "antidisestablishmentarianism"
			   
>>> word
			   
'antidisestablishmentarianism'
>>> word[7:19:1]
			   
'establishmen'
>>> word[7:20:1]
			   
'establishment'
>>> 
=== RESTART: /Volumes/Coding/Python Codes/Python Bible/slicer_exercise.py ===
>>> 
=== RESTART: /Volumes/Coding/Python Codes/Python Bible/slicer_exercise.py ===
>>> 
===== RESTART: /Volumes/Coding/Python Codes/Python Bible/email_slicer.py =====
What is your email address?:Rawlewjr@gmail.com
Your username is Rawlewjr and your domain name is gmail.com
>>> 
			   
>>> # Booleans and Comparison operators
			   
>>> B = True
			   
>>> C = False
			   
>>> type(B)
			   
<class 'bool'>
>>> 2 > 3
			   
False
>>> 2 < 3
			   
True
>>> 2 = 3
			   
SyntaxError: can't assign to literal
>>> type(2 < 3)
			   
<class 'bool'>
>>> 2 == 3
			   
False
>>> 3 == 3
			   
True
>>> 2 != 3
			   
True
>>> 4 >= 3
			   
True
>>> 3 >= 3
			   
True
>>> 2 >= 3
			   
False
>>> 4 <= 3
			   
False
>>> 2 <= 3
			   
True
>>> # > greater than,# < less than, == equal to, != not equal to
			   
>>> # > greater than,# < less than, == equal to, != not equal to
			   
>>> 2 > 3
			   
False
>>> 3 = 3
			   
SyntaxError: can't assign to literal
>>> 3 <= 3
			   
True
>>> 4 < 3
			   
False
>>> 5 != 3
			   
True
>>> 7 >= 9
			   
False
>>> 
==== RESTART: /Volumes/Coding/Python Codes/Python Bible/if _statement.py ====
num1 is bigger than num2
>>> 
==== RESTART: /Volumes/Coding/Python Codes/Python Bible/if _statement.py ====
Both numbers are equal
>>> 
===== RESTART: /Volumes/Coding/Python Codes/Python Bible/if_challenge.py =====
num2 is bigger than num1
>>> # Logical Operators
			   
>>> not True
			   
False
>>> not False
			   
True
>>> not 2 < 3
			   
False
>>> not 3 > 1
			   
False
>>> not 4 == 3
			   
True
>>> x = 10
			   
>>> y = 20
			   
>>> if not y < x:
	  print("it worked")

			   
it worked
>>> C = 10
			   
>>> D = 5
			   
>>> if C > 10 and D > 1:
	  print("it worked")

			   
>>> False and True
			   
False
>>> if C >= 10 and D > 1:
	  print("it worked")

			   
it worked
>>> if not (C > 10 and D > 1):
	   print("it worked")

			   
it worked
>>> C = 5
			   
>>> d = -1
			   
>>> if C > or D > 1:
			   
SyntaxError: invalid syntax
>>> if C > 1 or D > 1:
	   print("it worked")

			   
it worked
>>> True or False
			   
True
>>> D = 5
			   
>>> if C > 1 or D > 1:
	   print("it worked")

			   
it worked
>>> if C > 100 or D > 100:
	   print("it worked")

			   
>>> False or False
			   
False
>>> if not (C > 100 or D > 100):
	   print("it worked")

			   
it worked
>>> 
			   
>>> 
			   
>>> 
			   
>>> 
			   
>>> 
			   
>>> 
			   
>>>  C = 6
			   
SyntaxError: unexpected indent
>>> C = 6
			   
>>> D = 2
			   
>>> if (C > 5 and D > 5) or (C > 1 and D > 1):
			   print("it worked")

			   
it worked
>>> False or True
			   
True
>>> 
if not ((C > 5 and D > 5) or (C > 1 and D > 1)):
			   print("it worked")

			   
>>> True and False
			   
False
>>> False or True
			   
True
>>> True or True
			   
True
>>> (True or False) and (False or True)
			   
True
>>> (True and False) and (False or True)
			   
False
>>> # Data Structures
			   
>>> 
=== RESTART: /Volumes/Coding/Python Codes/Python Bible/Data_Structures.py ===
[27, 46, -5, 17, 99]
>>> print(our_list)
			   
[27, 46, -5, 17, 99]
>>> type(our_list)
			   
<class 'list'>
>>> 
=== RESTART: /Volumes/Coding/Python Codes/Python Bible/Data_Structures.py ===
[27, 46, -5, 17, 99]
Traceback (most recent call last):
  File "/Volumes/Coding/Python Codes/Python Bible/Data_Structures.py", line 10, in <module>
    jackson[start:end:step]
NameError: name 'start' is not defined
>>> jackson
			   
['A', 'B', 'C', 1, 2, 3, 'Do', 'Rey', 'Mi', True, False]
>>> our_list
			   
[27, 46, -5, 17, 99]
>>> # Data Structures Lists
			   
>>> our_list = [27, 46, -5, 17, 99]
print(our_list)
type(our_list)
jackson = ["A", "B", "C", 1,2,3, "Do", "Rey", "Mi", True, False]
jackson[4]
jackson[7]
jackson[-2]
x = jackson[6]
jackson[start:end:step]
jackson[0:3]
jackson
our_list = [1,2,[3,4,5], 6, 7, 8]
			   
SyntaxError: multiple statements found while compiling a single statement
>>> out_list
			   
Traceback (most recent call last):
  File "<pyshell#230>", line 1, in <module>
    out_list
NameError: name 'out_list' is not defined
>>> our_list = [27, 46, -5, 17, 99]
			   
>>> print(our_list)
			   
[27, 46, -5, 17, 99]
>>> type(our_list)
			   
<class 'list'>
>>> type(our_list)
			   
<class 'list'>
>>> jackson = ["A", "B", "C", 1,2,3, "Do", "Rey", "Mi", True, False]
			   
>>> jackson[4]
			   
2
>>> jackson[7]
			   
'Rey'
>>> jackson[-2]
			   
True
>>> x = jackson[6]
			   
>>> jackson[0:3]
			   
['A', 'B', 'C']
>>> jackson
			   
['A', 'B', 'C', 1, 2, 3, 'Do', 'Rey', 'Mi', True, False]
>>> our_list = [1,2,[3,4,5], 6, 7, 8]
			   
>>> our_list[2]
			   
[3, 4, 5]
>>> our_list[2][0]
			   
3
>>> our_list[2][1]
			   
4
>>> our_list[2][2]
			   
5
>>> our_list[2][1:]
			   
[4, 5]
>>> our_list[2][0::2]
			   
[3, 5]
>>> our_table = [[1,2,3],[4,5,6],[7,8,9]]
			   
>>> our_table[0]
			   
[1, 2, 3]
>>> our_table[1]
			   
[4, 5, 6]
>>> our_table[2]
			   
[7, 8, 9]
>>> our_table[0][1]
			   
2
>>> our_table[1][2]
			   
6
>>> our_table[2][1]
			   
8
>>> 
our_table[1][1:]
			   
[5, 6]
>>> 
=== RESTART: /Volumes/Coding/Python Codes/Python Bible/Travis_security.py ===
7
>>> print(len(known_users))
			   
7
>>> 
=== RESTART: /Volumes/Coding/Python Codes/Python Bible/Travis_security.py ===
8
>>> L = [1,5,2,6,2,9]
			   
>>> 
=== RESTART: /Volumes/Coding/Python Codes/Python Bible/Travis_security.py ===
8
Hi! My name is Travis
What is your name?:Alice
name recognised
Hi! My name is Travis
What is your name?:Rawle
name NOT recognised
Hi! My name is Travis
What is your name?:
name NOT recognised
Hi! My name is Travis
What is your name?:
Traceback (most recent call last):
  File "/Volumes/Coding/Python Codes/Python Bible/Travis_security.py", line 7, in <module>
    if name in known_users:
KeyboardInterrupt
>>> l
			   
Traceback (most recent call last):
  File "<pyshell#259>", line 1, in <module>
    l
NameError: name 'l' is not defined
>>> L
			   
Traceback (most recent call last):
  File "<pyshell#260>", line 1, in <module>
    L
NameError: name 'L' is not defined
>>> L = [1,2,3,4,5]
			   
>>> L
			   
[1, 2, 3, 4, 5]
>>> example = ["A","B","C","A","B",]
			   
>>> example.remove("A")
			   
>>> example
			   
['B', 'C', 'A', 'B']
>>> example = ["A","B","C","A","B",]
			   
>>> del example[3]
			   
>>> example
			   
['A', 'B', 'C', 'B']
>>> del example[0:2]
			   
>>> example
			   
['C', 'B']
>>> 
=== RESTART: /Volumes/Coding/Python Codes/Python Bible/Travis_security.py ===
Hi! My name is Travis
What is your name?:Rawle
Hmmm I don't think I have met you yet Rawle
Would you like to be added to the system (y/n)/: y
Hi! My name is Travis
What is your name?:Rawle
Hmmm I don't think I have met you yet Rawle
Would you like to be added to the system (y/n)/: y
Hi! My name is Travis
What is your name?:Rawle
Hmmm I don't think I have met you yet Rawle
Would you like to be added to the system (y/n)/: y
Hi! My name is Travis
What is your name?:
=== RESTART: /Volumes/Coding/Python Codes/Python Bible/Travis_security.py ===
Hi! My name is Travis
What is your name?:Rawle
Hmmm I don't think I have met you yet Rawle
Would you like to be added to the system (y/n)/: y
Hi! My name is Travis
What is your name?:rawle
Hmmm I don't think I have met you yet Rawle
Would you like to be added to the system (y/n)/: y
Hi! My name is Travis
What is your name?:
Traceback (most recent call last):
  File "/Volumes/Coding/Python Codes/Python Bible/Travis_security.py", line 5, in <module>
    name = input("What is your name?:").strip().capitalize()
KeyboardInterrupt
>>> known_users
			   
['Alice', 'Bob', 'Claire', 'Dan', 'Emma', 'Fred', 'Georgie', 'Harry']
>>> 
=== RESTART: /Volumes/Coding/Python Codes/Python Bible/Travis_security.py ===
Hi! My name is Travis
What is your name?:Rawle
Hmmm I don't think I have met you yet Rawle
Would you like to be added to the system (y/n): y
Hi! My name is Travis
What is your name?:Rawle
Hmmm I don't think I have met you yet Rawle
Would you like to be added to the system (y/n): n
Hi! My name is Travis
What is your name?:n
Hmmm I don't think I have met you yet N
Would you like to be added to the system (y/n): n
Hi! My name is Travis
What is your name?:n
Hmmm I don't think I have met you yet N
Would you like to be added to the system (y/n): n
Hi! My name is Travis
What is your name?:n
Hmmm I don't think I have met you yet 
Would you like to be added to the system (y/n): n
Hi! My name is Travis
nWhat is your name?:
Hmmm I don't think I have met you yet 
Would you like to be added to the system (y/n): n
Hi! My name is Travis
What is your name?:n
Hmmm I don't think I have met you yet N
Would you like to be added to the system (y/n): n
Hi! My name is Travis
nWhat is your name?:
Hmmm I don't think I have met you yet 
nWould you like to be added to the system (y/n): 
Hi! My name is Travis
nWhat is your name?:
Hmmm I don't think I have met you yet 
nWould you like to be added to the system (y/n): 
Hi! My name is Travis
nWhat is your name?:
Hmmm I don't think I have met you yet 
Would you like to be added to the system (y/n): n
Hi! My name is Travis
What is your name?:Z
Hmmm I don't think I have met you yet Z
Would you like to be added to the system (y/n): Z
Hi! My name is Travis
What is your name?:Z
Hmmm I don't think I have met you yet Z
Would you like to be added to the system (y/n): y
Hi! My name is Travis
What is your name?:Z
Hmmm I don't think I have met you yet Z
Would you like to be added to the system (y/n): 
Traceback (most recent call last):
  File "/Volumes/Coding/Python Codes/Python Bible/Travis_security.py", line 18, in <module>
    add_me = input("Would you like to be added to the system (y/n): ").strip().lower
KeyboardInterrupt
>>> known_users
			   
['Alice', 'Bob', 'Claire', 'Dan', 'Emma', 'Fred', 'Georgie', 'Harry']
>>> 
=== RESTART: /Volumes/Coding/Python Codes/Python Bible/Travis_security.py ===
Hi! My name is Travis
What is your name?:Rawle
Hmmm I don't think I have met you yet Rawle
Would you like to be added to the system (y/n): y
Hi! My name is Travis
What is your name?:Rawle
Hmmm I don't think I have met you yet Rawle
Would you like to be added to the system (y/n): n
Hi! My name is Travis
What is your name?:
=== RESTART: /Volumes/Coding/Python Codes/Python Bible/Travis_security.py ===
Hi! My name is Travis
What is your name?:Rawle
HelloRawle!
Would you like to be removed from the system (y/n)?: 
=== RESTART: /Volumes/Coding/Python Codes/Python Bible/Travis_security.py ===
Hi! My name is Travis
What is your name?:Rawle
Hello Rawle!
Would you like to be removed from the system (y/n)?: n
No problem, I didn't want you to leave anyway!
Hi! My name is Travis
What is your name?:Rawle
Hello Rawle!
Would you like to be removed from the system (y/n)?: y
Hi! My name is Travis
What is your name?:Rawle
Hmmm I don't think I have met you yet Rawle
Would you like to be added to the system (y/n): y
Hi! My name is Travis
What is your name?:Rawle
Hmmm I don't think I have met you yet Rawle
Would you like to be added to the system (y/n): y
Hi! My name is Travis
What is your name?:Rawle
Hmmm I don't think I have met you yet Rawle
Would you like to be added to the system (y/n): Y
Hi! My name is Travis
What is your name?:Rawle
Hmmm I don't think I have met you yet Rawle
Would you like to be added to the system (y/n): 
