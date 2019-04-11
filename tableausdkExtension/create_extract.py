import sys
import os
import pandas as pd

from tableausdk.Exceptions import TableauException
from tableausdk.HyperExtract import ExtractAPI, Extract, TableDefinition, Row
from tableausdk.Types import Type, Collation

from utils.config import read_yaml
from tab_tjjd.extract_helper import schema_types, col_types

class main(object):

    def __init__(self, filename, df, meta_data):
        """
        :param filename: the filename passed from the command line (a hyper file)
        :type filename: string
        :param df: the data to turn into a hyper file
        :type df: pandas dataframe
        :param meta_data: the meta data associated with the dataframe
        :type meta_data: dct
        """
        
        self.df = df
        self.meta_data = meta_data
        self.filename = filename
        self.cols = self.meta_data["COL_TYPES"]

        self.setUp()
        self.create_hyper()
        self.tearDown()

    def setUp(self):
        """Setup for the extract creation"""

        ExtractAPI.initialize()
        self.extract = Extract(self.filename)
        self.extract_exists = self.extract.hasTable('Extract')

    def createSchema(self):
        """Creates the table schema"""

        schema = TableDefinition()
        schema.setDefaultCollation(Collation.EN_GB)

        for key in self.cols:

            schema_type = schema_types().get_type(self.cols[key])
            schema.addColumn(key, schema_type)
            
        self.extract.addTable('Extract', schema)

    def populateExtract(self):
        """Populates cells in the extract"""

        table = self.extract.openTable('Extract')
        schema = table.getTableDefinition()
            
        for idx, row in self.df.iterrows():

            extract_row = Row(schema)

            for jdx, key in enumerate(self.cols):
                
                func = col_types(extract_row).get_type(self.cols[key])
                func(jdx, self.df.iloc[idx][key])

            table.insert(extract_row)

    def create_hyper(self):
        """Creates the hyper file"""

        self.createSchema()
        self.populateExtract()

    def tearDown(self):
        """Tear down hyper file setup"""
        
        self.extract.close()
        ExtractAPI.cleanup()
