import unittest
import os
import pandas as pd

from tableausdkExtension.create_extract import create_extract

class CreateExtractTestClass(unittest.TestCase):
 
    def __init__(self, *args, **kwargs):
 
        super(CreateExtractTestClass, self).__init__(*args, **kwargs)

        self.filename = "test_file.hyper"
        self.df = pd.DataFrame({"col1": [1,2,3,4], 
                                "col2": ["a", "b", "c", "d"],
                                "col3": [1.0, 2.0, 3.0, 4.0]})

        self.col_types = {"col1": "INTEGER",
                          "col2": "CHAR_STRING",
                          "col3": "DOUBLE"}

        create_extract(self.filename, self.df, self.col_types)

    def test_create_extract(self):

        fls = [self.filename, "DataExtract.log", "hyper_db"]
        [self.assertTrue(fl in os.listdir()) for fl in fls]
        [os.remove(fl) for fl in fls]
