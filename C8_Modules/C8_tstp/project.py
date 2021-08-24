# Here i import the module hello.py (note that it is in the same directory. Else i should write the complete path)

import hello, module1

# Calling the function print_hello() from the imported module hello.py
hello.print_hello()

"""
When running this file, module1 outputs its output
even though a function has not been called.
When a module is imported, it is run.
The module hello, does not output anything automatically
since I have to calle the function inside it first.
"""

"""
Now, module1 has been reworked to:
if __name__ == "__main__":
    print("Hello!!!")

and it nolonger runs on import.
It can be run from inside module1 but not in this module.
"""
