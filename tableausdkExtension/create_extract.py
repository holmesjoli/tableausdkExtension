from tableausdk.HyperExtract import ExtractAPI, Extract, TableDefinition, Row
from tableausdk.Types import Collation

from tableausdkExtension.extract_helper import map_schema, map_cols

class create_extract(object):

    def __init__(self, filename, df, col_types):
        """
        :param filename: the filename (a hyper file)
        :type filename: string
        :param df: the data to turn into a hyper file
        :type df: pandas dataframe
        :param col_types: a mapping of column names to column types, e.g. {VAR1: INTEGER}
        :type col_types: dct
        """
        self.df = df
        self.filename = filename
        self.col_types = col_types

        self.setUp()
        self.createHyper()
        self.tearDown()

    def checkFileExt(self):
        """Checks that the file extension is .hyper"""
        if not self.filename.endswith(".hyper"):
            raise Exception("Filename must end with .hyper")

    def setUp(self):
        """Setup for the extract creation"""
        self.checkFileExt()
        ExtractAPI.initialize()
        self.extract = Extract(self.filename)
        self.extract_exists = self.extract.hasTable('Extract')

    def createSchema(self):
        """Creates the table schema"""
        schema = TableDefinition()
        schema.setDefaultCollation(Collation.EN_GB)

        for key in self.col_types:

            schema_type = map_schema().get_type(self.col_types[key])
            schema.addColumn(key, schema_type)

        self.extract.addTable('Extract', schema)

    def populateExtract(self):
        """Populates cells in the extract"""

        table = self.extract.openTable('Extract')
        schema = table.getTableDefinition()

        for idx, row in self.df.iterrows():

            extract_row = Row(schema)

            for jdx, key in enumerate(self.col_types):

                func = map_cols(extract_row).get_type(self.col_types[key])
                func(jdx, self.df.iloc[idx][key])

            table.insert(extract_row)

    def createHyper(self):
        """Creates the hyper file"""

        self.createSchema()
        self.populateExtract()

    def tearDown(self):
        """Tear down hyper file setup"""

        self.extract.close()
        ExtractAPI.cleanup()
