# DATA-PIPELINE-DEVELOPMENT
*COMPANY*: CODTECH IT SOLUTIONS
*NAME*: DEEPANSHI
*INTERN ID*:CTO6DF2918
*DOMAIN*:DATA SCIENCE
*DURATION*: 6 WEEKS
*MENTOR*:NEELA SANTOSH

I built a basic data pipeline using python that performs 3 tasks:
1.Extracts data from CSV file
2.Transforms the data by cleaning it(removing rows with missing values)
3.Loads the cleaned data by printing it to the screen
The main purpose of this task was to understand how to work with data in CSV format and clean it using python.
The pipeline reads raw data from CSV file,removes missing or empty values,and outputs the clean data.

WHAT I BUILT:
* A working python script named pipeline.py .
TOOLS AND TECHNOLOGIES USED:
* VS Code- for writing and running the code
* python 3.13- programming language used
* pandas-python library for data processing
* CSV file- used as the data source(raw data)
STEP BY STEP PROCESS:
* installed python and made sure its set up in the VS code terminal
* installed the pandas library using:
* pip install pandas
* created a file named data.csv with some sample values and missing data, like:
  id,name,sales
  1,Alice,100
  2,Bob,150
  3,,200
  4,Deepanshi,
 * wrote a python script that:
   . uses pandas.read_csv() to extract the data.
   . cleans the data using df.dropna() to remove incomplete rows.
   . prints the cleaned data using print(df)
   . (optional) saves the cleaned data to a new file cleaned_data.csv using df.to_csv()
   . ran the pipeline using the command:
      python pipeline.py.

   OUTPUT
   . the final output printed only the  rows with complete data(no missing value).
      sample
       cleaned data
         id   name    sales
       0  1    Alice   100.0
       1  2     Bob     150.0
   WHAT I LEARNED:
   . how to install and configure python and pandas in VS code
   . how to create and work with CSV files in python
   . how to write modular python code using funtions(extract_data,transform_data,load_data)
   . the concept of data cleaning and handling missing values using pandas
   . how to debug errors like
     IndentationError,FileNotFoundError, and EmptyDataError
   . basics of how real data pipelines are structured in the industry.
