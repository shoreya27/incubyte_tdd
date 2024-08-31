import unittest
from app.string_app import StringApp

class Test_String_App(unittest.TestCase):

    def setup(self):
        self.str_app = StringApp('1\n2;,\n3')
    