# tableausdkExtension

tableausdkExtension builds on the [Tableau SDK](https://onlinehelp.tableau.com/current/api/sdk/en-us/help.htm#SDK/tableau_sdk_using_python.htm%3FTocPath%3D_____4) python package. 

## About Tableau SDK

[Tableau SDK](https://onlinehelp.tableau.com/current/api/sdk/en-us/help.htm) is a set of packages maintained by Tableau. It gives users of different programming languages the ability to build Tableau data extracts which can then be loaded in Tableau.

### Why is this important?

Users may wonder why this is useful since Tableau already has many data connection capabilities (e.g. Excel, csv files, SQL Server, etc. ). For Data Analysts and Scientists, many of us still want to do data management and data validation in Python and then connect the cleaned data to Tableau. It's extremely useful for automatting pipelines, such that data validation, data management scripts, and extract builder steps can all be automatted and called using one Python script. The other important thing of note, is that building the extract requires the user to explicitly declare the types of each column in the dataset. Although, Tableau is very good at guessing column types, it still doesn't get it right 100% of the time, which then requires the user to manually change the column type in the Tableau UI. Again, for the sake of automation this is a pain point and could potentially cause errors if a user is utilizing a pre-build dashboard with new data. 

### What's in tableausdkExtension

What's in the extension? 
The tableausdkExtension package simply builds on the tableausdk package and automates some of the functionalities developed by Tableau.


## Getting Started

### tableausdk
1. Download [tableauSDK package](https://downloads.tableau.com/tssoftware/Tableau-SDK-Python-Win-64Bit-10-3-19.zip)
2. Move the downloaded package from the Downloads folder to the folder where you keep your Python repositories and rename the file to tableausdk^[This makes it easier to install the package later on and is consistent with how many Python packages are named].
3. Install the package. In Bash (Terminal/Command Line) navigate to the place where the package is stored. Navigate to the top folder, e.g. `cd tableausdk`. Then build and install the package using the following commands. 

```
python setup.py build
python setup.py install
```

### tableausdkExtension

The tableausdkExtension package functions were developed based on code presented at the Tableau 2018 conference. Code from the session can be found [here](https://www.dropbox.com/sh/lztdogubf20498e/AADJJpb_KO4g2m_CF1-SSc_Sa/TC18%20-%20Developer%20Track/Leveraging%20the%20Extract%20API%20to%20build%20sophisticated%20data%20models?dl=0&subfolder_nav_tracking=1). A video of the session can be found [here](https://www.youtube.com/watch?v=kk01bWEALXs&feature=youtu.be). A PDF of the powerpoint slides from the session can be found [here](https://tc18.tableau.com/sites/default/files/session/assets/18BI-081_Leveraging%20the%20Extract%20API%20to%20build%20sophisticated%20data%20models.pdf). 