from tableausdk.Types import Type

class map_schema(object):

    def __init__(self):
        """
        A dictionary of schema types
        """
        self.type = {"CHAR_STRING": Type.CHAR_STRING,
                    "INTEGER": Type.INTEGER,
                    "DOUBLE": Type.DOUBLE,
                    "BOOLEAN": Type.BOOLEAN,
                    "DATETIME": Type.DATETIME,
                    "DATE": Type.DATE,
                    "SPATIAL": Type.SPATIAL}

    def get_type(self, key):
        """
        Returns the type based off the key
        """
        try:
            return self.type[key]
        except KeyError:
            e = "Please check col_types spelling/case. These are the excepted types:\n{}".format("\n".join(self.type.keys()))
            raise Exception(e)

class map_cols(object):

    def __init__(self, extract_row):
        """
        A dictionary of functions to create to populate the columns.
        """
        self.type = {"NULL": lambda col_idx, value: extract_row.setNull(col_idx, value),
                    "CHAR_STRING": lambda col_idx, value: extract_row.setCharString(col_idx, value),
                    "INTEGER": lambda col_idx, value: extract_row.setLongInteger(col_idx, value),
                    "DOUBLE": lambda col_idx, value: extract_row.setDouble(col_idx, value),
                    "BOOLEAN": lambda col_idx, value: extract_row.setBoolean(col_idx, value),
                    "DATETIME": lambda col_idx, value: extract_row.setDateTime(col_idx, value),
                    "DATE": lambda col_idx, value: extract_row.setDate(col_idx, value),
                    "SPATIAL": lambda col_idx, value: extract_row.setSpatial(col_idx, value),
                    "DURATION": lambda col_idx, value: extract_row.setDuration(col_idx, value)}

    def get_type(self, key):
        """
        Returns the type based off the key.
        """
        try:
            return self.type[key]
        except KeyError:
            e = "Please check col_types spelling/case. These are the excepted types:\n{}".format("\n".join(self.type.keys()))
            raise Exception(e)
