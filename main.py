if __name__ == '__main__':
    while True:
        # starting menu
        print("<====== WIUT ======>")
        print("1. Submit Coursework")
        print("2. Submit MC")
        print("3. View My MCs")
        print("4. Quit")
        print("")

        menu_item = int(input("======> "))

        if menu_item == 1:
            print("Submit Coursework")
        elif menu_item == 2:
            print("Submit MC")
        elif menu_item == 3:
            print("View My MCs")
        elif menu_item == 4:
            break
        else:
            print("Enter Numbers 1-4!")
