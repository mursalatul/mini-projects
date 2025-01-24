from babyconda import BabyConda

def main() -> None:
    # starting point of the program
    bbconda = BabyConda()

    program_is_running = 'Y'
    while program_is_running == 'Y' or program_is_running == 'y':
        bbconda.main_operation()
        program_is_running = input('Do you want to continue? (Y/N) ')
    exit(0)

if __name__ == '__main__':
    main()