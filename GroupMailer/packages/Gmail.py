class Gmail:
    """
    Provide methods for operating different types of operations on Gmail data
    """
    def isvalidgmail(self, gmail : str) -> bool:
        """
        Check if the given email address follows the format for Gmail addresses.

        Parameters:
        - gmail (str): The email address to be checked.

        Returns:
        bool: True if the email address is in the correct format for Gmail, False otherwise.
        """
        gmail = gmail.strip()
        # checking if the first letter is number or not
        if gmail[0:1].isdigit():
            return False
        # checking the letters
        for char in gmail:
            if char == " " or char in "`~!#$%^&*()_-=+[]\{\}\\|':;\">/?":
                return False
            elif char == '@' and gmail.count(char) > 1:
                return False
            elif char.isupper():
                return False
        
        # checking last part
        return gmail.endswith("@gmail.com")
    
    def isfixable(self, gmail : str) -> bool:
        """
        Check if a gmail can be fixed or not. A gmail can be fixed in and only if
        it contian white space or any error after @
        
        Parameters:
        - gmail (str): The email address to be checked.

        Returns:
        bool: True if the gmail can be fixed, else False
        """
        gmail = gmail.strip()

        # checking starting to @ of the gmail.
        # if it is in good shape after @ can be also fixed
        position_of_at_the_rate = gmail.find("@")
        if position_of_at_the_rate == -1:
            return False
        part_1 = gmail[:position_of_at_the_rate + 1]
        for char in part_1:
            if char in "`~!#$%^&*()_-=+[]\{\}\\|':;\">/?":
                return False
        return True