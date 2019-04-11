#------------------------------------------------------------------------------
#   SECTION 1 - LIBRARIES
#------------------------------------------------------------------------------
    # HELPER LIBRARIES
import argparse
import sys
import textwrap
import pandas as pd

    # TABLEAU LIBRARIES; AKA EXTRACT API
from tableausdk import *
from tableausdk.HyperExtract import *


#------------------------------------------------------------------------------
#   SECTION 2 - CONNECT AND READ SOURCE DATA
#------------------------------------------------------------------------------
    # FILE HANDLER FOR CSV INPUT DATA
input_data_csv = './Dummy_PatientData.csv'

    # CREATE DATAFRAME FROM CSV INPUT DATE
df = pd.read_csv(input_data_csv)

    # # FILTER NUMBER OF ROWS FOR DEMO
# n = 500
# df = df.head(n)

    # FILTER COLUMNS
filter_columns = ['PAT_MRN','CSN','PATIENT_NAME','DEPARTMENT_NAME','ROUTE','NAME_ABBREVIATED','TAKEN_TIME','BIRTH_DATE','DOSE','TotalDose','BolusDose']
df = df[filter_columns]

    # CONVERT DATE/TIME FIELDS TO PANDAS DATE/TIME DATA TYPE

dt_columns = ['TAKEN_TIME','BIRTH_DATE']
for col_tmp in dt_columns:
    print(col_tmp)
    df[col_tmp] = pd.to_datetime(df[col_tmp], errors='coerce')

    # REPLACE NAN VALUES WITH ZEROS FOR ENTIRE DATAFRAME
df = df.fillna(0)


#------------------------------------------------------------------------------
#   SECTION 3 - PARSE ARGUMENTS (HELPER FUNCTION)
#------------------------------------------------------------------------------
def parseArguments():
    parser = argparse.ArgumentParser( description='A simple demonstration of the Tableau SDK.', formatter_class=argparse.RawTextHelpFormatter )
    # (NOTE: '-h' and '--help' are defined by default in ArgumentParser
    parser.add_argument( '-b', '--build', action='store_true', # default=False,
                         help=textwrap.dedent('''\
                            If an extract named FILENAME exists in the current directory,
                            extend it with sample data.
                            If no Tableau extract named FILENAME exists in the current directory,
                            create one and populate it with sample data.
                            (default=%(default)s)
                            ''' ) )
    parser.add_argument( '-s', '--spatial', action='store_true', # default=False,
                         help=textwrap.dedent('''\
                            Include spatial data when creating a new extract."
                            If an extract is being extended, this argument is ignored."
                            (default=%(default)s)
                            ''' ) )
    parser.add_argument( '-f', '--filename', action='store', metavar='FILENAME', default='order-py.hyper',
                         help=textwrap.dedent('''\
                            FILENAME of the extract to be created or extended.
                            (default='%(default)s')
                            ''' ) )
    return vars( parser.parse_args() )


#------------------------------------------------------------------------------
#   SECTION 4 - CREATING EXTRACT (DEFINE SCHEMA AND CREATE EMPTY EXTRACT)
#------------------------------------------------------------------------------
    # (NOTE: This function assumes that the Tableau SDK Extract API is initialized)

def createOrOpenExtract(
    filename,
    useSpatial
):
    try:

        # Create Extract Object
        # (NOTE: The Extract constructor opens an existing extract with the
        #  given filename if one exists or creates a new extract with the given
        #  filename if one does not)

        extract = Extract( filename )

        # Define Table Schema (If we are creating a new extract)
        # (NOTE: In Tableau Data Engine, all tables must be named 'Extract')

        if ( not extract.hasTable( 'Extract' ) ):
            schema = TableDefinition()

            schema.setDefaultCollation( Collation.EN_GB )
            schema.addColumn( 'TAKEN_TIME', Type.DATETIME )
            schema.addColumn( 'PATIENT_NAME', Type.CHAR_STRING )
            schema.addColumn( 'PAT_MRN', Type.CHAR_STRING )
            schema.addColumn( 'CSN', Type.CHAR_STRING )
            schema.addColumn( 'DEPARTMENT_NAME', Type.CHAR_STRING )
            schema.addColumn( 'ROUTE', Type.CHAR_STRING )
            schema.addColumn( 'NAME_ABBREVIATED', Type.CHAR_STRING )
            schema.addColumn( 'DOSE', Type.DOUBLE )
            schema.addColumn( 'TotalDose', Type.DOUBLE )
            schema.addColumn( 'BolusDose', Type.DOUBLE )

            if ( useSpatial ):
                schema.addColumn( 'Destination', Type.SPATIAL )
            table = extract.addTable( 'Extract', schema )

            if ( table == None ):
                print 'A fatal error occurred while creating the table:\nExiting now\n.'
                exit( -1 )

    except TableauException, e:
        print 'A fatal error occurred while creating the new extract:\n', e, '\nExiting now.'
        exit( -1 )

    return extract


#------------------------------------------------------------------------------
#   SECTION 5 - POPULATE EXTRACT (GET SCHEMA, INSERT DATA)
#------------------------------------------------------------------------------
    # (NOTE: This function assumes that the Tableau SDK Extract API is initialized)
def populateExtract(
    extract,
    useSpatial
):
    try:
        # Get Schema
        table = extract.openTable( 'Extract' )
        schema = table.getTableDefinition()



        for index, row in df.iterrows():
            # Insert Data
            extract_row = Row( schema )

            # Consider refactoring
            # https://erikrood.com/Python_References/iterate_rows_pandas.html

            tt_year = int(df.iloc[index]["TAKEN_TIME"].year)
            tt_month = int(df.iloc[index]["TAKEN_TIME"].month)
            tt_day = int(df.iloc[index]["TAKEN_TIME"].day)
            tt_hour = int(df.iloc[index]["TAKEN_TIME"].hour)
            tt_min = int(df.iloc[index]["TAKEN_TIME"].minute)
            tt_sec = int(df.iloc[index]["TAKEN_TIME"].second)


            # print(pur_year, pur_month, pur_day, pur_hour, pur_min, pur_sec)
            # print(type(pur_year), type(pur_month), type(pur_day), type(pur_hour), type(pur_min), type(pur_sec))

            extract_row.setDateTime(0, tt_year, tt_month, tt_day, tt_hour, tt_min, tt_sec, 0) # FIELD = 'TAKEN_TIME'
            print(tt_year, tt_month, tt_day, tt_hour, tt_min, tt_sec)

            extract_row.setCharString(1, df.iloc[index]["PATIENT_NAME"]) # FIELD = 'PATIENT_NAME'
            print(str(df.iloc[index]["PATIENT_NAME"]))

            extract_row.setCharString(2, df.iloc[index]["PAT_MRN"].astype(str)) # FIELD = 'PAT_MRN'
            print(str(df.iloc[index]["PAT_MRN"]))

            extract_row.setCharString(3, df.iloc[index]["CSN"].astype(str)) # FIELD = 'CSN'
            print(str(df.iloc[index]["CSN"]))

            extract_row.setCharString(4, df.iloc[index]["DEPARTMENT_NAME"]) # FIELD = 'DEPARTMENT_NAME'
            print(str(df.iloc[index]["DEPARTMENT_NAME"]))

            extract_row.setCharString(5, df.iloc[index]["ROUTE"]) # FIELD = 'ROUTE'
            print(str(df.iloc[index]["ROUTE"]))

            extract_row.setCharString(6, df.iloc[index]["NAME_ABBREVIATED"]) # FIELD = 'NAME_ABBREVIATED'
            print(str(df.iloc[index]["NAME_ABBREVIATED"]))

            extract_row.setDouble(7, df.iloc[index]["DOSE"]) # FIELD = 'DOSE'
            print(str(df.iloc[index]["DOSE"]))

            extract_row.setDouble(8, df.iloc[index]["TotalDose"]) # FIELD = 'TotalDose'
            print(str(df.iloc[index]["TotalDose"]))

            extract_row.setDouble(9, df.iloc[index]["BolusDose"]) # FIELD = 'BolusDose'
            print(str(df.iloc[index]["BolusDose"]))


            table.insert( extract_row )

    except TableauException, e:
        print 'A fatal error occurred while populating the extract:\n', e, '\nExiting now.'
        exit( -1 )


#------------------------------------------------------------------------------
#   Main
#------------------------------------------------------------------------------
def main():
    # Parse Arguments
    options = parseArguments()


    # Extract API Demo
    if ( options[ 'build' ] ):

        # STEP 1
        # Initialize the Tableau Extract API
        ExtractAPI.initialize()

        # STEP 2
        # Define Schema
        extract = createOrOpenExtract( options[ 'filename' ], options[ 'spatial' ] )

        # STEP 3
        # Populate Extract
        populateExtract( extract, options[ 'spatial' ] )

        # STEP 4
        # Flush the Extract to Disk
        extract.close()

        # STEP 5
        # Close the Tableau Extract API
        ExtractAPI.cleanup()

        # Print columns added to Extract
        print('Added the following columns to the Tableau Data Extract...'+'\n')
        for col_name in df.columns.values.tolist():
            print(col_name)

    return 0

if __name__ == "__main__":
    retval = main()
    sys.exit( retval )
