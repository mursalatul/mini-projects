import os

class Cleaner:
    windows_temp_path = 'C:\\Windows\\Temp'
    user_temp_path = 'C:\\Users\\mursa\\AppData\\Local\\Temp'
    windows_temp_path = 'D:\\Programming_related\\PROJECTS\\ALL_PROJECT\\mini-projects\\clean_windows_temp\\test'
    
    def __init__(self) -> None:
        pass

    def clean_w_temp(self) -> bool:
        """clean temporary files placed in C:\\Windows\\Temp
            Note: It can't remove some files as they are using by some running system.
        Returns:
            bool: [True] if successfully executed, else [False]
        """

        # setting the current working directory into windows_temp_path
        os.chdir(self.windows_temp_path)
        with os.scandir(os.getcwd()) as contents:
            for content in contents:  
                try:
                    if content.is_file():
                        os.remove(content.name)
                    else:
                        os.rmdir(content.name)
                except Exception as e:
                    print("%s" %e)
                        

    def clean_u_temp(self) -> bool:
        """clean temporary files placed in C:\\Users\\mursa\\AppData\\Local\\Temp
            Note: It can't remove some files as they are using by some running system.
        Returns:
            bool: [True] if successfully executed, else [False]
        """
        # setting the current working directory into windows_temp_path
        os.chdir(self.user_temp_path)
        with os.scandir(os.getcwd()) as contents:
            for content in contents:  
                try:
                    if content.is_file():
                        os.remove(content.name)
                    else:
                        os.rmdir(content.name)
                except Exception as e:
                    print("%s" %e)

    def clean_all(self) -> bool:
        """clean both windows and user temp

        Returns:
            bool: [True] if successfully executed, else [False]
        """
        self.clean_w_temp()
        self.clean_u_temp()

    # def remove_dir(self, dir_path):


def main():
    """the main function
    """
    clean = Cleaner()
    clean.clean_w_temp()
    clean.clean_u_temp()

if __name__ == '__main__':
    main()