class File:
    # True if file is readable or file initialization went wrong
    file_status = False
    def __init__(self, file_name : str):
        self.file = open(file_name.strip(), 'r')

        # checking if data imported or not
        self.file_status = self.file.readable()
    
    def getall(self) -> list:
        """
        Return a list of all the data of the file object
        
        Parameters
        None
        Returns

        list: all the file content
        """
        if not self.file_status:
            return ["FILE INITIALIZATION ERROR"]
        
        return self.file.readlines()
    
    def getaline(self) -> str:
        """
        yield line one by one
        Parameters
        None
        
        yield
        str: gmail address
        """
        if not self.file_status:
            return ["FILE INITIALIZATION ERROR"]
        
        return self.file.readline()
