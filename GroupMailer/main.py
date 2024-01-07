from packages import Gmail, File, DATA 

def showinterface() -> int :
    """
    Show cmd based interface of the app ask for the command number.

    Parameters
    None

    Returns
    command number: a int number indicating a particular command
    """
    # printing commands
    for key, value in DATA.command_list.items():
        print(f"{key}. {value}")
    
    # get input
    return int(input("Enter Command Number To Execute: "))

def main():
    a = "GroupMailer".center(50,"*")
    print(a)

    # show and get command number
    command = None
    while command != 'Exit':
        command_number = showinterface()
        command = DATA.command_list[command_number]
        if command == 'Exit':
            print("Thanks For Using GroupMailer.\nFeel free to contribute & give a star at https://github.com/mursalatul/mini-projects/tree/master/GroupMailer")
            break
        elif command == 'Help':
            print("Select 'Send mail' to send a package of mails.\nSelect 'Check Mail' to check if any email is in wrong state or not.")

if __name__ == '__main__':
    main()