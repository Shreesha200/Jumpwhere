class StringHandler:
    def __init__(self):
        self.s = ""

    def get_string(self):
        self.s = input("Enter a string: ")

    def print_string(self):
        print(self.s[::-1])
