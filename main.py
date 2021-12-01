from datetime import datetime

#function to convert string to date type
import cw_submission
import mc_submit


def parse_date(str):
    return datetime.strptime(str, '%d.%m.%Y')

#function for printing beautiful lines
def new_two_lines():
    print("____________________________")
    print("")
    print("____________________________")

#holds all cw submissions
cw_submissions = []

#holds all mc submissions
mc_submissions = []

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
            while True:
                new_submission = cw_submission.submit()
                if new_submission is None:
                    print("Wrong Input")
                else:
                    print("Successfully submitted")
                    new_two_lines()
                    cw_submissions.append(new_submission)
                    cw_submission.check(new_submission)
                    break
            new_two_lines()
        elif menu_item == 3:
            mc_submit.submit(None)
            new_two_lines()
        elif menu_item == 4:
            print("View My MCs")
            new_two_lines()
        elif menu_item == 5:
            break
        else:
            print("Enter Numbers 1-5!")
            new_two_lines()
