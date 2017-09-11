"""
The main program should use functions from data and display modules
"""
import data
import display


def safe_get_positive_int(trait):
    num = 0
    while not num:
        try:
            num = int(input("\n Please provide student\'s %s: " % (trait)))
        except ValueError:
            print("%s has to be a positive numeral." % (trait.capitalize()))
        else:
            if num < 0:
                print("Year of birth cannot be negative.")
                num = 0  # make our loop ask again

    return num


def safe_get_student_from_input():
    # returns a list of tokens as below
    # data fmt: name,surname,year​ of​ birth,class,average​ grade,average​ presence
    name = ""
    while not name:
        name = input("\n Please provide student name: ")
    name = name.capitalize()

    surname = ""
    while not surname:
        surname = input("\n Please provide student surname: ")
    surname = surname.capitalize()

    birthyear = 0
    while not birthyear:
        birthyear = safe_get_positive_int("year of birth")

    class_id = ""
    while not class_id:
        class_id = input("\n Please provide student class: ")
    class_id = class_id.capitalize()

    avg_grade = 0
    while not avg_grade:
        avg_grade = safe_get_positive_int("average grade")

    avg_presence = 0
    while not avg_presence:
        avg_presence = safe_get_positive_int("average presence")

    # data fmt: name,surname,year​ of​ birth,class,average​ grade,average​ presence
    return [ name, surname, str(birthyear), class_id, str(avg_grade), str(avg_presence) ]


def add_new_student(students, new_student):
    """
    ADDITIONAL REQUIREMENT - BONUS

    Creates id for new student, adds it at the beginning of new student data,
    adds new student to students list and appends it to data file.

    :param list students: currently existing students
    :param list new_student: new student data without id. Format:
        name,surname,year of birth,class,average grade,average presence

    :returns: updated students list
    :rtype: list
    """
    # data fmt: id, name,surname,year​ of​ birth,class,average​ grade,average​ presence
    # grab ids
    current_ids = []
    for record in students:
        current_ids.append(record[0])

    # grab a brand new one
    try:
        new_uid = data.generate_id(current_ids)
    except ValueError:
        print("id pool has run out of unique possibilities")
        return

    student_added = new_student
    student_added.insert(0, new_uid)

    students.append(student_added)

    # note: export function expects a list of lists
    data.export_to_file([student_added])

    return students


def delete_student_by_id(students, uid):
    """
    Deletes student from list by given unique id and updates data file

    :param list students: currently existing students
    :param str uid: unique id of student to be deleted

    :returns: updated students list
    :rtype: list
    """
    uid_exists = False
    index = 0
    # data fmt: id,name,surname,year​ of​ birth,class,average​ grade,average​ presence
    for i in range(len(students)):
        if students[i][0] == uid:
            index = i
            uid_exists = True
            break # design implies that there is only one instance of uid

    if uid_exists:
        updated = students[:] # make a copy
        del updated[index]
        data.export_to_file(updated, "class_data.txt", "w")  #overwrite file
        return updated
    else:
        return students


def is_valid_uid(uid):
    if len(uid) != 4:
        return False

    uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    specials = "!@#$%^&*()_+"
    lowers = uppers.lower()

    return uid[0] in uppers and \
            uid[1] in digits and \
            uid[2] in specials and \
            uid[3] in lowers

# returns False if it was chosen to quit, else the student list
def handle_eligible_option(index, options):
    students = data.import_data_from_file()
    if options.index("Print all students") == index:
        display.print_students_list(students)

    elif options.index("Get student by id") == index:
        uid = ""
        while not is_valid_uid(uid):
            uid = input("\n Please provide a valid id: ")

        try:
            student = data.get_student_by_id(uid, students)
        except ValueError:
            print("Student with such id does not exist")
        else:
            display.print_student_info(student)

    elif options.index("Get youngest student") == index:
        youngest = data.get_youngest_student(students)
        display.print_student_info(youngest)

    elif options.index("Get oldest student") == index:
        oldest = data.get_oldest_student(students)
        display.print_student_info(oldest)

    elif options.index("Add new student") == index:
        new_student = safe_get_student_from_input()
        students = add_new_student(students, new_student)
        return students

    elif options.index("Delete student by id") == index:
        uid = ""
        while not is_valid_uid(uid):
            uid = input("\n Please provide a valid id: ")

        try:
            student = data.get_student_by_id(uid, students)
        except ValueError:
            print("Student with such id does not exist")
        else:
            students = delete_student_by_id(students, uid)
    elif options.index("x") == index:
        print("quitting...")
        return False

    return True

def main():
    """
    Calls all interaction between user and program, handles program menu
    and user inputs. It should have main loop of program that will end only
    when user choose an option from menu to close the program. It should repeat
    displaying menu and asking for input until that moment.

    You should create new functions and call them from main whenever it can
    make the code cleaner
    """
    options = ("Print all students", "Get student by id", \
                "Get youngest student", "Get oldest student", \
                "Add new student", "Delete student by id", "x")

    while True:
        display.print_program_menu(options)
        try:
            index = int(input("\n Please choose one of the options [%u...%u]" % (0, len(options) - 1)))
        except ValueError:
            print("Invalid input.")
        else:
            if index in range(len(options)):
                if handle_eligible_option(index, options) == False: # returns False on exit request
                    break
            else:
                print("Choice numeral out of range")

if __name__ == '__main__':
    main()
