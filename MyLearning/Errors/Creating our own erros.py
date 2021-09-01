class RunTimeErrorWithCode(TypeError):
    """
    docstring
    use for documenting some details about the class
    also can be used inside a method or so
    doc string must have \""" in the start and end
    Exception raised when a specific error code is  needed.
    """
    def __init__(self, message, code):
        super().__init__(f'Error code {code}: {message}')
        self.code = code

err = RunTimeErrorWithCode("An error happened.", 500)
#print(err.__doc__)  #this prints the documentation part which we have done above
print(err)