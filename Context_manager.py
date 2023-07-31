#with open("notes.text", "w") as file:
    #file.write("Some to do")

class ManageFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print("enter")
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self,exc_type,exc_value,exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print("Exception has been handled")
        print("exc:", exc_type, exc_value)
        print("exit")

with ManageFile("Notes.text") as file:
    print("do some stuff....")
    file.write("some to do")
    

from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
    f = open(filename, "w")
    try:
        yield f
    finally:
        f.close()

with open_managed_file("notes.text") as t:
    t.write("Ahmed Babatunde")