# tableausdkExtension

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/978fb2b5516c443c9ec9e0c9cd86affb)](https://www.codacy.com/app/holmesjoli/tableausdkExtension?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=holmesjoli/tableausdkExtension&amp;utm_campaign=Badge_Grade)
[![Build status](https://travis-ci.org/holmesjoli/tableausdkExtension.svg?branch=master)](https://travis-ci.org/holmesjoli/tableausdkExtension)

tableausdkExtension builds on the [Tableau SDK](https://onlinehelp.tableau.com/current/api/sdk/en-us/help.htm#SDK/tableau_sdk_using_python.htm%3FTocPath%3D_____4) python package.

## About Tableau SDK

[Tableau SDK](https://onlinehelp.tableau.com/current/api/sdk/en-us/help.htm) is a set of packages maintained by Tableau. It gives programmers the ability to build Tableau data extracts which can then be loaded in Tableau.

### Use Cases

Users may wonder why this is useful since Tableau already has many data connection capabilities (e.g. Excel, csv files, SQL Server, etc.). Additionally, Tableau has the ability to do basic data cleaning capabilities such as splitting columns, changing column types, filtering data, etc.

#### Pipeline Automation

However, many people who touch data prefer to do management and data validation in tradition data analysis software and then connect the cleaned data to Tableau. Combining data validation, data management, and extract creation into one Python script is also very useful for automatting pipelines.

#### Best Practices

Automatting, multiple parts of an ETL into one script helps save time, but also allows users to continue practicing best practices such as version controlling code.

#### Explicit Type Declaration

Additionally, building a Tableau extract through code is important because the extract requires the user to explicitly declare the types of each column in the dataset. Although,Tableau is very good at guessing column types, it still doesn't get it right 100% of the time, which then requires the user to manually change the column type in the Tableau UI. This is an important step for quality control.

### What's in tableausdkExtension

What's in the extension? 
The tableausdkExtension package simply builds on the tableausdk package and automates some of the functionalities developed by Tableau.

## Getting Started

### Build Environment

It's recommended to build an environment, but not absolutely necessary. TableausdkExtension has been tested on the included environment however.

1.  Create the environment `conda create --name tableau --file requirements.txt`
2.  Activate the environment `source activate tableau`

Note: environment can be named whatever, it doesn't have to be called tableau

### tableausdk

1.  Download [tableauSDK package](https://downloads.tableau.com/tssoftware/Tableau-SDK-Python-Win-64Bit-10-3-19.zip)
2.  Move the downloaded package from `Downloads` to the folder where you keep your Python repositories and rename the file to tableausdk.
3.  Install the package. In Bash (Terminal/Command Line) navigate to the place where the package is stored. Navigate to the top folder, e.g. `cd tableausdk`. Then build and install the package using the following commands.

```python
    python setup.py build
    python setup.py install
```

### tableausdkExtension

1.  Clone the [repository](https://github.com/holmesjoli/tableausdkExtension)
2.  Install the package by navigating to the project folder and installing `pip install -e .`

The tableausdkExtension package functions were developed based on code presented at the Tableau 2018 conference(Named tc2018_sample.py in the tableausdkExtension folder).

-   Code from the session can be found [here](https://www.dropbox.com/sh/lztdogubf20498e/AADJJpb_KO4g2m_CF1-SSc_Sa/TC18%20-%20Developer%20Track/Leveraging%20the%20Extract%20API%20to%20build%20sophisticated%20data%20models?dl=0&subfolder_nav_tracking=1).
-   A video of the session can be found [here](https://www.youtube.com/watch?v=kk01bWEALXs&feature=youtu.be).
-   A PDF of the powerpoint slides from the session can be found [here](https://tc18.tableau.com/sites/default/files/session/assets/18BI-081_Leveraging%20the%20Extract%20API%20to%20build%20sophisticated%20data%20models.pdf).

#### Sample Code

```python
import pandas as pd

from create_extract import create_extract

filename = "test_file.hyper"
df = pd.DataFrame({"col1": [1,2,3,4], 
                    "col2": ["a", "b", "c", "d"],
                    "col3": [1.0, 2.0, 3.0, 4.0]})

col_types = {"col1": "INTEGER",
                "col2": "CHAR_STRING",
                "col3": "DOUBLE"}

create_extract(filename, df, col_types)
```

The class `create_extract` takes three inputs, filename, df, col_types

-   **filename** is the filename of the Tableau extract file, it must have the extension `.hyper`
-   **df** is the dataframe to convert to a hyper file
-   **col_types** is a mapping of column names to column types as a dictionary. The excepted column types are: INTEGER, CHAR_STRING, DOUBLE, BOOLEAN, DATETIME, DATE, SPATIAL.

Running create_extract generates three files in the directory which the code is run from:

-   filename.hyper
-   DataExtract.log
-   hyper_db
