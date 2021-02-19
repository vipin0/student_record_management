#    Student Marks Management System
#    Written By VIPIN KUMAR YADAV
#    Sri Eshwar College Of Engineering 
#    Email: vipin6673@gmail.com
import sys
from time import sleep
from getpass import getpass

user1 = ('vipin', '1234', 'abcd')  #authourised usernams
pass1 = ('vipin', '1234', 'abcd')  #authourised passwords
userpass = dict(zip(user1, pass1))
# print(userpass)
reg = [] #registration number
name = [] #name
rollno = []# rollno
branch = [] #branch
t = ('Name', 'Roll No. ', 'Marks ')
sub = ('Physics', 'Chemisrty', 'Maths', 'EG', 'PSP', 'English')
marks = [] #Marks


def check_reg():
    x=input()
    if x not in reg:
        return x
    else:
        sleep(1)
        print("\n***** Registration No. Already Exist ******")
        print("Enter again:  ",end="")
        return check_reg()


def input_v():
    x = input()
    if x.isdigit() and 0 <= float(x) <= 100:
        temp = float(x)
        return temp
    else:
        print("\n***** Invalid Mark *****\nEnter Again:  ", end="")
        return input_v()

def grades(x):
    if 90<x<=100:
        return 'O'
    elif 80<x<=90:
        return 'A'
    elif 70<x<=80:
        return 'B'
    elif 60<x<=70:
        return 'C'
    elif 50<x<=60:
        return 'D'
    elif 40<x<=50:
        return 'E'
    else:
        return 'F'


def add_details():
    ch3=('y','Y','n','N')
    print("\n********* ADD NEW RECORD **********")
    ch2 = 'y'
    while ch2.upper() == 'Y':
        print("Enter the Reg. No.: ",end="")
        reg1 =check_reg()
        reg.append(reg1)
        name1 = input("Enter the Name: ")
        name.append(name1)
        rollno1 = input("Enter the Roll No.:  ")
        rollno.append(rollno1)
        m = []
        print("\n ***** ENTER MARK IN RANGE 0-100 ONLY *****")
        for i in range(0, len(sub)):
            print("Enter the marks of {} :  ".format(sub[i]), end="")
            # x=input_v()
            m.append(input_v())
        marks.append(m)
        ch2 = input("\nWant to add more: Enter (Y / N):  ")
        if ch2 in ch3:
            if ch2 in ('y','Y'):
                add_details()
            elif ch2.upper() == 'N':
                admin_menu()
                break
        else:
            print("\n****** Wrong Input ******")
            sleep(1)
            print("\n****** Returning To Admin Menu ******")
            admin_menu()
            break


def login():
    sleep(1)
    ch3=('Y','y','N','n')
    ch2 = 'y'
    tries = 3
    print("\n***** PLEASE ENTER YOUR LOGIN DETAILS ******")
    while ch2.upper() == 'Y' and tries != 0:
        user = input("Enter Your Username :  ")
        #print('Enter Your Password :   ', end="")
        #pass2 = input()
        pass2=getpass(prompt='Enter Your Password :  ')
        for i in userpass.keys():
            if i == user and userpass[i] == pass2:
                admin_menu()
                break
        else:
            sleep(1)
            print("\n********** Invalid Username or Password ********")
            tries -= 1
        if tries == 0:
            sleep(1)
            print("****** You have Reached the maximum attempts ******")
            main()
            break
        else:
            ch2 = input("Want to Login Again: Enter (Y / N):  ")
            if ch2 not in ch3:
                print("\n******OPPS!! Wrong Input *******\n")
                sleep(1)
                print("\n****** Returning To Main Menu ******")
                sleep(1)
                main()
                break
            if ch2.upper() == 'N':
                sleep(1)
                print("\n****** Returning To Main Menu ******")
                sleep(1)
                main()
                break


def print_s(x):
    sleep(1)
    pos=0
    if len(reg) != 0:
        if x in reg:
            print("\n\n*********** STUDENT DETAILS ************")
            i = 0
            for m in reg:
                if m == x:
                    pos = i
                    break
                i += 1
            print(repr("Reg No.").ljust(10),repr("Name").rjust(15),repr("Roll No.").rjust(15))
            print(repr(reg[pos]).ljust(10),repr(name[pos]).rjust(15),repr(rollno[pos]).rjust(15))
            print("\n**************** MARKS DETAILS *************")
            print(repr('Subject').ljust(18),repr('Mark').rjust(12),repr('Grade').rjust(10))
            print()      
            for j in range(len(sub)):
                print(repr(sub[j]).ljust(18),repr(marks[pos][j]).rjust(12),repr(grades(marks[pos][j])).rjust(10))
        else:
            print("\n******* Invalid Registration Number *******")
            main()
    else:
        print("\n***** Opps!! Something went Wrong !!!!! *****\n")
        sleep(1)
        print("***** Returning To Main Menu ******")
        sleep(1)
        main()


def print_t():
    if len(reg) != 0:
        sleep(1)
        print("\n\n********** ALL RECORDS **********\n")
        for i in range(0, len(reg)):
            print(repr("Reg No.").ljust(10),repr("Name").rjust(15),repr("Roll No.").rjust(15))
            print(repr(reg[i]).ljust(10),repr(name[i]).rjust(15),repr(rollno[i]).rjust(15))
            print("\n****************** MARKS DETAILS *************")
            print(repr('Subject').ljust(18),repr('Mark').rjust(12),repr('Grade').rjust(10))
            print()      
            for j in range(len(sub)):
                print(repr(sub[j]).ljust(18),repr(marks[i][j]).rjust(12),repr(grades(marks[i][j])).rjust(10))
            print('\n')
        sleep(2)
        admin_menu()

    else:
        sleep(1)
        print("\n***** No Record Found ****")
        print("***** Kindly ADD RECORD First ***** ")
        sleep(1)
        print("\n****** Returning To Admin Menu ******")
        admin_menu()


def modify():
    pos=0
    if len(reg) != 0:
        sleep(1)
        print("\n************ MODIFY RECORD ************")
        x = input("Enter the Reg. No. to Modify:   ")
        sleep(1)
        if x in reg:
            print_s(x)
            print()
            i = 0
            for m in reg:
                if m == x:
                    pos = i
                    break
                i += 1

            reg1 = input("Enter New Reg. No.: ")
            reg[pos] = reg1
            name1 = input("Enter New name: ")
            name[pos] = name1
            rollno1 = input("Enter New Roll. No.:  ")
            rollno[pos] = rollno1
            print("*** Enter the New Marks in Range 0-100 ***:")
            m = []
            for i in range(0, len(sub)):
                print("Enter the marks of {} :  ".format(sub[i]), end="")
                z = input_v()
                m.append(z)
            marks[pos] = m
            print("\n*********** RECORD UPDATED ************")
            admin_menu()
        else:
            print("\n****** Invalid Registration Number ******")
            admin_menu()
    else:
        sleep(1)
        print("\n***** No Record Found ****")
        print("***** Kindly ADD RECORD First ***** ")
        sleep(1)
        print("\n****** Returning To Admin Menu ******")
        admin_menu()


def delete():
    pos=0
    if len(reg) != 0:
        sleep(1)
        print("\n************ DELETE RECORD ************")
        x = input("Enter the Reg. No. to Delete : ")
        sleep(1)
        if x in reg:
            print()
            print_s(x)
            i = 0
            for m in reg:
                if m == x:
                    pos = i
                    break
                i += 1
            ch = input("\n     Confirm Deletion ?? (Y/N):  ")
            if ch == 'Y' or ch == 'y':
                del reg[pos]
                del name[pos]
                del rollno[pos]
                del marks[pos]
                print("\n***** Record Deleted ******")
                admin_menu()
            elif ch == 'N' or ch == 'n':
                admin_menu()
            else:
                print("\n******* Wrong Input ******")
                sleep(1)
                print("\n****** Returning To Admin Menu ******")
                admin_menu()
        else:
            sleep(1)
            print("\n******* Invalid Registration Number *******")
            sleep(1)
            print("\n****** Returning To Admin Menu ******")
            admin_menu()

    else:
        sleep(1)
        print("\n***** No Record Found ****")
        print("***** Kindly ADD RECORD First ***** ")
        sleep(1)
        print("\n****** Returning To Admin Menu ******")
        admin_menu()

def student_menu():
    sleep(1)
    ch3=('y','Y','n','N')
    print("\n************** STUDENT MENU ***************\n")
    ch2 = "y"
    while ch2.upper() == 'Y':
        x = input("To view your Result enter your Reg. No.: ")
        print_s(x)
        sleep(1)
        ch2 = input("\nWant to Search More Result: Enter (Y / N)  ")
        if ch2 not in ch3:
            print("\n****** Wrong Input ******")
            sleep(1)
            print("\n****** Returning to Main Menu ******")
            sleep(1)
            main()
        elif ch2.upper() == 'N':
            sleep(1)
            main()
            break


def admin_menu():
    sleep(1)
    ch2 = 'y'
    ch3=('1','2','3','4','5')
    ch4=('y','Y','n','N')
    while ch2.upper() == 'Y':
        print("\n************ ADMIN MENU ************\n\t1.Add New Record \n\t2.Modify Record \n\t3.Delete Record\n\t4.Print All Records\n\t5.Main Menu")
        ch1 = input("Enter your choice: (1 / 2 / 3 / 4 / 5):   ")
        if ch1 in ch3:
            if ch1 =='1':
                sleep(1)
                add_details()
            elif ch1 =='2':
                modify()
            elif ch1 == '3':
                delete()
            elif ch1 =='4':
                print_t()
            elif ch1 =='5':
                sleep(1)
                main()
        elif ch1 not in ch3:
            print("******* Wrong input *******")
            ch2 = input("\nReturn to Admin Menu: Enter (Y / N):   ")
            if ch2 in ch4:
                if ch2 in ('y','Y'):
                    admin_menu()
                if ch2.upper() == 'N':
                    sleep(1)
                    print("****** Returning To Main Menu ******")
                    sleep(1)
                    main()
                    break
def pdetails():
    print("\n\n********* STUDENT RECORD MANAGEMENT SYSTEM **********\n")
    print(" " * 30, "Written BY : VIPIN KUMAR YADAV")
    print(" " * 45, "CSE 1st YEAR")
    print(" " * 31, "Guided BY : Mr. Karthik Sir")
    print(" " * 30, "Sri Eshwar College Of Engineering")
    sleep(1)
    main()


def main():
    print("\n**************** MAIN MENU ****************")
    ch2 = "Y"
    ch3=('1','2','3')
    while ch2.upper() == "Y":
        print("\t1.Admin Mode \n\t2.Student mode \n\t3.Exit")
        ch = input("Enter your Choice (1 / 2 / 3):   ")
        if ch in ch3:
            if ch =='1':
                login()
            elif ch =='2':
                student_menu()
            elif ch =='3':
                sleep(1)
                print("\n\n****** Thanks For Using The program ******")
                sleep(2)
                sys.exit(0)
        elif ch not in ch3:
            print("****** Wrong Input ******")
            print("\nReturn to Main Menu: Enter(Y / N):  ",end="")
            ch2 = input()
            if ch2 in ('y','Y'):
                sleep(1)
                main()
            elif ch2.upper == "N":
                sleep(1)
                print("****** Thanks For Using The program ******")
                sleep(2)
                sys.exit(0)
        elif ch2 not in ('y','Y','n','N'):
            print("***** Wrong Input *****")
            


pdetails()
