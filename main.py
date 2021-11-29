from datetime import datetime

#function to convert string to date type
import cw_submission
def parse_date(str):
    return datetime.strptime(str, '%d.%m.%Y')

#function for printing beautiful lines
def new_two_lines():
    print("____________________________")
    print("")
    print("____________________________")

cw_submissions = []
# dictionary that holds modules and deadlines
module_deadline = {
    'CSF': parse_date("01.12.2021"),
    'IMOB': parse_date("11.12.2021"),
    'WT': parse_date("14.12.2021"),
    'ISDS': parse_date("21.12.2021")
}

#main function
if __name__ == '__main__':

    while True:
        # starting menu
        print("<====== WIUT ======>")
        print("1. View Modules and Deadlines")
        print("2. Submit Coursework")
        print("3. Submit MC")
        print("4. View My MCs")
        print("5. Quit")
        new_two_lines()

        menu_item = int(input("======> "))

        if menu_item == 1:
            for module in module_deadline.keys():
                print(module+": "+str(module_deadline.get(module)))
            new_two_lines()
        elif menu_item == 2:
            if not cw_submission.submit():
                print("Wrong Input")
            else:
                print("Successfully submitted")
            new_two_lines()
        elif menu_item == 3:
            print("Submit MC")
            new_two_lines()
        elif menu_item == 4:
            print("View My MCs")
            new_two_lines()
        elif menu_item == 5:
            break
        else:
            print("Enter Numbers 1-5!")
            new_two_lines()
