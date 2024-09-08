
# This example is a Python script that calls Python code by importing code.
# In this case, all the python code in bmi_main.py is wrapped in a function.
# Note, bmi_main.py uses a user defined Python function library.

# importing sys
import sys
import jmp

# adding folder with python code to the system path
sys.path.insert(1, '/Python')
from bmi_main import bmimain

bmimain()