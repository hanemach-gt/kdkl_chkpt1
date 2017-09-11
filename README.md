# Krk-2017-2-checkpoint-1

## JERZYBOT ver. 01a

Jerzy feels overhelmed by all the duties in codecool. He asked you to write short program, that will help him cope with class management.

### Structure

JERZYBOT structure consist of three modules:

**data.py** - store functions regarding data management

**display.py** - store functions responsible for printing all the required data. In this module functions responsible for printing result are already implemented. First, try to understand how are they work and use them!

**main_program.py** - Heart of JERZYBOT. Contains main function and import data.py and display.py. **Also implements all functions for changing .txt file**

Module tests.py stores basic unit test for your project, based on test_class_data.txt Module bonus_tests.py stores tests for additional features --> **DO NOT MODIFY THOSE FILES!**

For your implementation operate only on class_data.txt REST OF TXT FILES ARE FOR TESTING PURPOSES ONLY - **DO NOT MODIFY THEM!**

Program have to import .txt file with values separated by commas as a primary source of data. Each line of file represents student data in given order:

`id,name,surname,year of birth,class,average grade,average presence`

Data exported to file should have the same format.

Basic functionality of program focus on filtering and changing data by user from source file, with certain level of persistence (program can also save and export data)

### General info about requirements

Passing tests is something you need to get 10 or 12 points. However, if during manual testing we find errors not found by tests from tests.py or bonus_tests.py, you will not get max points for requirements.

### Requirements

1. To get 10 points for requirements you must implement all functions without docstring note that they are bonus features.
2. To get 10 points for requirements your code must pass all basic tests (tests without BONUS in their name).
3. Every empty basic function should be implemented as it was described in it's docstrings. **PLEASE READ THEM CAREFULLY**
4. Built-in function **print() is forbidden in data.py module**
5. Your program's main menu offers at least 4 options for user (you can choose which one from data.py module for instance ----> 1. Print all students, 2. Get student by id,  3. Display youngest student, 4. display oldest student)
6. At least one function should be foolproof
7. At least one function should be able to handle potential exceptions (you can choose which one)
8. Create at least one additional function that wasn't defined in any of modules
9. Use functions from display monule to display data
10. If you read this last requirement, smile and keep your head up! You can do it! :)

You can add your own functions to any module if you feel they are needed to make your code cleaner.

### Additional Requirements

If your code pass all basic tests (tests without BONUS in their name, defined in tests.py), we will check bonus tests. To get 12 points for requirements your code have to pass all bonus tests (defined in bonus_tests.py).

1. Extend your program by new function altering file values. Remember about clean code basic principles!
2. Implement sort_by_age function from data
3. Implement get_all_by_gender from data
4. Implement generate_id from data
5. Implement add_new_student from main_program
6. Every empty bonus function should be implemented as it was described in it's docstrings. **PLEASE READ THEM CAREFULLY**
