"""
The main program should use functions from data and display modules
"""
import data
import display


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
        try:
            birthyear = int(input("\n Please provide student\'s year of birth: "))
        except ValueError:
            print("Year of birth has to be a positive numeral.")

        if birthyear < 0:
            print("Year of birth cannot be negative.")
            birthyear = 0  # make our loop ask again

    class_id = ""
    while not class_id:
        class_id = input("\n Please provide student class: ")
    class_id = class_id.capitalize()

    # data fmt: name,surname,year​ of​ birth,class,average​ grade,average​ presence
    return [ name, surname, str(birthyear), class_id, str(0), str(0) ]


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
        if student[i][0] == uid:
            index = i
            uid_exists = True
            break # design implies that there is only one instance of uid

    if uid_exists:
        updated = students[:] # make a copy
        del updated[index]
        return updated
    else:
        return students


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
            operation = int(input("\n Please choose one of the options [%u...%u]" % (0, len(options) - 1)))
        except ValueError:
            print("Invalid input.")
        else:
            if operation in range(len(operations)):
                if options.index("Print all students") == operation:
                    students = data.import_data_from_file()
                    display.print_students_list(students)

                elif options.index("Get student by id") == operation:
                    pass

            else:
                print("Choice numeral out of range")

if __name__ == '__main__':
    main()
