import mysql.connector
from mysql.connector import errorcode
import maskpass

def art_objects_choice(input_choice):
    if input_choice == '1':
        instr="select * from ART_OBJECTS"
        cur.execute(instr)
        col_names=cur.column_names
        search_result=cur.fetchall()
        print("Search found ",len(search_result)," Entries:\n")
        header_size=len(col_names)
        for i in range(header_size):
            print("{:<15s}".format(col_names[i]),end='')
        print()
        print(15*header_size*'-')
        for row in search_result:
            for val in row:
                print("{:<15s}".format(str(val)),end='')
            print()
    elif input_choice == '2':
        instr="select * from ART_OBJECTS ORDER BY Id_no;"
        cur.execute(instr)
        col_names=cur.column_names
        search_result=cur.fetchall()
        print("Search found ",len(search_result)," Entries:\n")
        header_size=len(col_names)
        for i in range(header_size):
            print("{:<15s}".format(col_names[i]),end='')
        print()
        print(15*header_size*'-')
        for row in search_result:
            for val in row:
                print("{:<15s}".format(str(val)),end='')
            print()
    elif input_choice == '3':
        instr= "select DateBorn, Date_died from (ART_OBJECTS JOIN ARTIST on name_ = artist_name) Where Name_ = 'R W';"
        cur.execute(instr)
        col_names=cur.column_names
        search_result=cur.fetchall()
        print("Search found ",len(search_result)," Entries:\n")
        header_size=len(col_names)
        for i in range(header_size):
            print("{:<15s}".format(col_names[i]),end='')
        print()
        print(15*header_size*'-')
        for row in search_result:
            for val in row:
                print("{:<15s}".format(str(val)),end='')
            print()
    else:
        command_error_roles()

def end_users_check_and_print(selection_check):
    if selection_check == '1':
        while True:
            try:
                print("\n\nYou have the following options for Displaying Art Pieces\n\n\n1- Display Title and Year\n2- Order By ID Number\n3- Date Born and Died for Artists")
                input_art = input("\n\n\n\nPlease Choose (Press R to Return): ")
                while input_art != "R":
                    art_objects_choice(input_art)
                    print("\n\nYou have the following options for Art Pieces\n\n\n1- Display Title and Year\n2- Order By ID Number\n3- Date Born and Died for Artists")
                    input_art = input("\n\n\n\nPlease Choose (Press R to Return): ")
                break
            except EOFError:
                command_error_roles()
            except KeyboardInterrupt:
                command_error_roles()   

    elif selection_check == '2':
        instr="select * from PAINTING"
        cur.execute(instr)
        col_names=cur.column_names
        search_result=cur.fetchall()
        print("Search found ",len(search_result)," Entries:\n")
        header_size=len(col_names)
        for i in range(header_size):
            print("{:<15s}".format(col_names[i]),end='')
        print()
        print(15*header_size*'-')
        for row in search_result:
            for val in row:
                print("{:<15s}".format(str(val)),end='')
            print()

    elif selection_check == '3':
        instr="select * from SCULPTURE"
        cur.execute(instr)
        col_names=cur.column_names
        search_result=cur.fetchall()
        print("Search found ",len(search_result)," Entries:\n")
        header_size=len(col_names)
        for i in range(header_size):
            print("{:<15s}".format(col_names[i]),end='')
        print()
        print(15*header_size*'-')
        for row in search_result:
            for val in row:
                print("{:<15s}".format(str(val)),end='')
            print()


    elif selection_check == '4':
        instr="select * from OTHER"
        cur.execute(instr)
        col_names=cur.column_names
        search_result=cur.fetchall()
        print("Search found ",len(search_result)," Entries:\n")
        header_size=len(col_names)
        for i in range(header_size):
            print("{:<15s}".format(col_names[i]),end='')
        print()
        print(15*header_size*'-')
        for row in search_result:
            for val in row:
                print("{:<15s}".format(str(val)),end='')
            print()

    elif selection_check == '5':
        instr="select * from PERMANENT_COLLECTION"
        cur.execute(instr)
        col_names=cur.column_names
        search_result=cur.fetchall()
        print("Search found ",len(search_result)," Entries:\n")
        header_size=len(col_names)
        for i in range(header_size):
            print("{:<15s}".format(col_names[i]),end='')
        print()
        print(15*header_size*'-')
        for row in search_result:
            for val in row:
                print("{:<15s}".format(str(val)),end='')
            print()

    elif selection_check == '6':
        instr="select * from ARTIST"
        cur.execute(instr)
        col_names=cur.column_names
        search_result=cur.fetchall()
        print("Search found ",len(search_result)," Entries:\n")
        header_size=len(col_names)
        for i in range(header_size):
            print("{:<15s}".format(col_names[i]),end='')
        print()
        print(15*header_size*'-')
        for row in search_result:
            for val in row:
                print("{:<15s}".format(str(val)),end='')
            print()

    elif selection_check == '7':
        instr="select * from EXHIBITIONS"
        cur.execute(instr)
        col_names=cur.column_names
        search_result=cur.fetchall()
        print("Search found ",len(search_result)," Entries:\n")
        header_size=len(col_names)
        for i in range(header_size):
            print("{:<15s}".format(col_names[i]),end='')
        print()
        print(15*header_size*'-')
        for row in search_result:
            for val in row:
                print("{:<15s}".format(str(val)),end='')
            print()

    else:
        command_error_roles()

def end_user():
    while True:
        try:
            print('\n') # creates a new line
            print('-' * 130) # prints 130 lines
            print("\n\nOptions to display the following tables\n\n\n1- Art Pieces\n2- Paintings\n3- Sculpture\n4- Other Art Pieces\n5- Artists\n6- Collections\n7- Exhibitions")            
            selection = input("\n\nSelect the following options mentioned above (R to Return Main Menu): ")
            while selection != "R":
                end_users_check_and_print(selection)
                print("\nOptions to display the following tables\n\n\n1- Art Pieces\n2- Paintings\n3- Sculpture\n4- Other Art Pieces\n5- Artists\n6- Collections\n7- Exhibitions")         
                selection = input("\n\nSelect the following options mentioned above (R to Return Main Menu): ")
            print("\n")
            print('-' * 130) # prints 130 lines  
            break
        except EOFError:
            command_error_roles()
        except KeyboardInterrupt:
            command_error_roles()     

def admin_check(input_admin_choice):
    if input_admin_choice == '1':
        while True:
            try:
                print('\n') # creates a new lineSS
                print('-' * 130) # prints 130 lines        
                admin_command = input("\n\nPlease input a SQL Command. (R to log out and return to main menu): ")
                while admin_command != "R":
                    try:
                        cur.execute(admin_command)
                        print("Command Successfully Executed")
                    except mysql.connector.Error:
                        sql_command_error()   
                    admin_command = input("\n\nPlease input a SQL Command. (R to log out and return to main menu): ")
                print("\n")
                print('-' * 130) # prints 130 lines  
                break
            except EOFError:
                sql_command_error()
            except KeyboardInterrupt:
                sql_command_error()
    elif input_admin_choice == '2':
        try:
            choice = input("Do You Want to Run the Script File on Queries or Database: ")
            if choice == 'Queries':
                cnx = mysql.connector.connect(
                    host = "127.0.0.1", 
                    port = 3306,        
                    user = username,
                    password = passcode,
                    database = "MUSEUM"
                )
                cursor_ad = cnx.cursor()
                try:
                    fd = open('MUSEUM_QUERIES.sql', 'r')
                except FileNotFoundError:
                    print("Cannot Open File")
                    return
                sqlFile = fd.read()
                fd.close()
                sqlCommands = sqlFile.split(';')
                for command in sqlCommands:
                    try:
                        if command.strip() != '':
                            cursor_ad.execute(command)
                    except (IOError, msg):
                        print("Command skipped ", msg)
            elif choice == 'Database':
                cnx = mysql.connector.connect(
                    host = "127.0.0.1", 
                    port = 3306,        
                    user = username,
                    password = passcode,
                    database = "MUSEUM"
                )
                cursor_ad = cnx.cursor()
                try:
                    fd = open('MUSEUM_DB.sql', 'r')
                except FileNotFoundError:
                    print("Cannot Open File")
                    return
                sqlFile = fd.read()
                fd.close()
                sqlCommands = sqlFile.split(';')
                for command in sqlCommands:
                    try:
                        if command.strip() != '':
                            cursor_ad.execute(command)
                    except (IOError, msg):
                        print("Command skipped ", msg)
            else:
                command_run_error()
        except EOFError:
            command_run_error()
        except KeyboardInterrupt:
            command_run_error()
                

  
def administrator():
    while True:
        try:
            print('\n') # creates a new line
            print('-' * 130) # prints 130 lines
            print("\n\nOptions for Administration\n\n\n1- Run SQL Command\n2- Run SQL Script")            
            selection_admin = input("\n\nSelect the following options mentioned above (R to log out and return to main menu): ")
            while selection_admin != "R":
                admin_check(selection_admin)
                print("\n\nOptions for Administration\n\n\n1- Run SQL Command\n2- Run SQL Script")      
                selection_admin = input("\n\nSelect the following options mentioned above (R to log out and return to main menu): ")
            print("\n")
            print('-' * 130) # prints 130 lines  
            break
        except EOFError:
            command_error_roles()
        except KeyboardInterrupt:
            command_error_roles()  

def employee_tables(tuple_insert_table_print):
    instr="select * from {}".format(tuple_insert_table_print.upper().replace(" ", "_"))
    cur.execute(instr)
    col_names=cur.column_names
    search_result=cur.fetchall()
    print("Search found ",len(search_result)," Entries:\n")
    header_size=len(col_names)
    for i in range(header_size):
        print("{:<15s}".format(col_names[i]),end='')
    print()
    print(15*header_size*'-')
    for row in search_result:
        for val in row:
            print("{:<15s}".format(str(val)),end='')
        print()

def employee_check_inputs(employee_inputs):
    if employee_inputs == '1':
        tuple_insert_table = input("\n\nPlease Input A Table Name: ")
        employee_tables(tuple_insert_table)

        tuple_insert_attribute_values = input("\nPlease Input Data (Data Format Must Be The Following: 'data1','data2','data3',....): ")
        try:
            tuple_insert = "INSERT INTO {0} VALUES ({1});".format(tuple_insert_table.upper().replace(" ", "_"), tuple_insert_attribute_values)
            cur.execute(tuple_insert)
            print("Adding Info Successfull")
        except mysql.connector.Error:
            sql_error() 
    elif employee_inputs == '2':
        tuple_delete_table = input("\n\nPlease Input A Table Name: ")
        employee_tables(tuple_delete_table)
        tuple_delete_attribute = input("\nPlease Input Attribute Name: ")
        tuple_delete_attribute_value = input("\nPlease Input Data: ")
        try:
            tuple_delete = "DELETE FROM {0} WHERE {1} = '{2}';".format(tuple_delete_table.upper().replace(" ", "_"), tuple_delete_attribute, tuple_delete_attribute_value)
            cur.execute(tuple_delete)
            print("Deleting Info Successfull")
        except mysql.connector.Error:
            sql_error() 
    elif employee_inputs == '3':
        tuple_modify_table = input("\n\nPlease Input A Table Name: ")
        employee_tables(tuple_modify_table)
        tuple_modify_attributes = input("\nPlease Input A Attribute Name: ")
        tuple_modify_attribute_values = input("\nPlease Input Data: ")
        tuple_modify_primary = input("\nPlease Input Primary Key: ")
        tuple_modify_primary_value = input("\nPlease Input Primary Key Value: ")
        try:
            tuple_modify = "UPDATE {0}\n SET {1} = '{2}'\n WHERE {3} = {4};".format(tuple_modify_table.upper().replace(" ", "_"), tuple_modify_attributes.capitalize().replace(" ", "_"), tuple_modify_attribute_values, tuple_modify_primary.capitalize().replace(" ", "_"), tuple_modify_primary_value)
            cur.execute(tuple_modify)
            print("Update Info Successfull")
        except mysql.connector.Error as eer:
            print(eer)
            sql_error()


def employee():
    while True:
        try:
            print('\n') # creates a new line
            print('-' * 130) # prints 130 lines
            print("\n\nOptions for Employee\n\n\n1- Add Information\n2- Delete Information\n3- Modify Information")            
            selection_employee = input("\n\nSelect the following options mentioned above (R to log out and return to main menu): ")
            while selection_employee != "R":
                if selection_employee in ['1', '2', '3']:
                    employee_check_inputs(selection_employee)
                else:
                    command_error_roles() 
                print("\n\nOptions for Employee\n\n\n1- Add Information\n2- Delete Information\n3- Modify Information")    
                selection_employee = input("\n\nSelect the following options mentioned above (R to log out and return to main menu): ")
            print("\n")
            print('-' * 130) # prints 130 lines  
            break
        except EOFError:
            command_error_roles()
        except KeyboardInterrupt:
            command_error_roles()    

def menu_display():
    print('\n\n\n\n\n\n\n\n\n\n') # creates new line
    print('-' * 130) # prints 130 lines
    print('\n\n\n') # creates new line
    print('-' * 45, end='') # prints 45 lines
    print(' \033[1m\033[33mTHE MUSEUM APPLICATION\033[0m ', end='')  # prints the title in bold yellow
    print('-' * 45) # prints 45 lines
    menu_display_selections()

def menu_display_selections():
    print('\n') # creates new line
    title_main_menu = '----- Main Menu -----' # assigns a string for the title menu
    center_align_main_menu = title_main_menu.center(130) # aligns the string at center
    print('\033[36m' + center_align_main_menu)  # prints the title of the main menu
    print('\n\n\033[3m\033[1m\033[36mWELCOME TO THE MAIN MENU\033[0m') # prints a modified text in italic blue
    print('\nPlease input either A or a as Administrator, E or e as Employee, U or u as End User(press q or Q to quit)') # prints a text to the user that to input one of the following commands

def quit_display():
    print('\n') # creates a new line
    print('\n') # creates a new line        
    print('-' * 125) # prints 130 lines
    print('\n\n') # creates a new line
    print('-' * 41, end='') # prints 41 lines
    print(' \033[1m\033[33mQUITTING THE MUESEUM APPLICATION\033[0m ', end='') # prints the end title in bold yellow
    print('-' * 40) # prints 40 lines
    print('\n\n\n\n\n\n\n\n\n\n') # creates a new line

def sql_error():
    print('\n') # creates a new line
    print('-' * 130) # prints 130 lines
    print('\n\n\033[1m\033[31mInvalid Input. Please Type The Appropriate Input\033[0m') # the program will tell the user that to input the correct command to proceed
    print('\n') # creates new line 
    print('-' * 130) # prints 130 lines 

def command_error():
    print('\n') # creates a new line
    print('-' * 130) # prints 130 lines
    print('\n\n\033[1m\033[31mInvalid Command. You must type a specific command whether you want to log in as Administrator, Employee, or End User\033[0m') # the program will tell the user that to input the correct command to proceed
    print('\n') # creates new line 
    print('-' * 130) # prints 130 lines

def command_run_error():
    print('\n') # creates a new line
    print('-' * 130) # prints 130 lines
    print('\n\n\033[1m\033[31mInvalid Input. You must type whether you want to run a script for queries or database\033[0m') # the program will tell the user that to input the correct command to proceed
    print('\n') # creates new line 
    print('-' * 130) # prints 130 lines

def sql_command_error():
    print('\n') # creates a new line
    print('-' * 130) # prints 130 lines
    print('\n\n\033[1m\033[31mYou Have Inputed the Wrong SQL Command\033[0m') # the program will tell the user that to input the correct command to proceed
    print('\n') # creates new line 
    print('-' * 130) # prints 130 lines

def command_error_roles():
    print('\n') # creates a new line
    print('-' * 130) # prints 130 lines
    print('\n\n\033[1m\033[31mInvalid Command. You must type a specific command from the following options\033[0m') # the program will tell the user that to input the correct command to proceed
    print('\n') # creates new line 
    print('-' * 130) # prints 130 lines     

def username_and_password_error():
    print('\n') # creates a new line
    print('-' * 130) # prints 130 lines
    print('\n\n\033[1m\033[31mInvalid Username and Password\033[0m') # the program will tell the user that to input the correct command to proceed
    print('\n') # creates new line 
    print('-' * 130) # prints 130 lines   

def selection_checks(user_interface_check):

    print('\n') # creates a new line
    print('-' * 130) # prints 130 lines
    if user_interface_check in ['A', 'a' ,'E', 'e']:
        try:
            global username
            username = input("\n\nUsername (Press Ctrl+C To Return to Main Menu): ")
        except KeyboardInterrupt:
            print('\n\nReturning to Main Menu') # the program will tell the user that to input the correct command to proceed
            print('\n') # creates new line 
            print('-' * 130) # prints 130 lines  
            return
        except EOFError:
            ""
        try:
            global passcode
            passcode = maskpass.askpass(prompt="Password (Press Ctrl+C To Return to Main Menu): ", mask = "*")
        except KeyboardInterrupt:
            print('\n\nReturning to Main Menu') # the program will tell the user that to input the correct command to proceed
            print('\n') # creates new line 
            print('-' * 130) # prints 130 lines  
            return
        except EOFError:
            ""

    elif user_interface_check in ['U', 'u']:
        username = "guest"
        passcode = None
    try:
        cnx = mysql.connector.connect(
            host = "127.0.0.1", 
            port = 3306,        
            user = username,
            password = passcode,
        )
        global cur
        cur = cnx.cursor()
        cur.execute("use museum")
        if user_interface_check == 'A' or user_interface_check == 'a':
            administrator()
        elif user_interface_check == 'E' or user_interface_check == 'e':
            employee()
        elif user_interface_check == 'U' or user_interface_check == 'u':
            end_user()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            username_and_password_error()
            selection_checks(user_interface_check)
        else:
            print(err)
            selection_checks(user_interface_check)
    except UnboundLocalError:
        username_and_password_error()
        selection_checks(user_interface_check)
    else:
            cnx.close()

def main():
        menu_display()
        while True:
            try:
                user_interface = input('\n\033[1mPlease type a command: \033[0m') # request the user to input the commands text is in bold
                while user_interface != 'q' and user_interface != 'Q':
                    if user_interface in ['A', 'a' ,'E', 'e'] or user_interface in ['U', 'u']:
                        selection_checks(user_interface)
                    else:
                        command_error()
                    menu_display_selections()
                    user_interface = input('\n\033[1mPlease type a command: \033[0m') # request the user to input the commands text is in bold
                quit_display()
                break
            except EOFError:
                command_error()            
                menu_display_selections()
            except KeyboardInterrupt:
                command_error()            
                menu_display_selections()

if __name__ == '__main__': # assigns an if statement for the name and main program
    main() # calls and prints the main function
