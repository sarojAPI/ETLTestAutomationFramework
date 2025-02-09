from pickle import FALSE

import pandas as pd

# Looking at the row & column of the data
def test_readRowAndColumn():
    target_df = pd.read_csv('/Users/sarojdahal/PycharmProjects/ETLTest/people-100.csv', sep=',')
    shape = target_df.shape
    print(shape)

# Looking at the column count
def test_readColumn():
    target_df = pd.read_csv('/Users/sarojdahal/PycharmProjects/ETLTest/people-100.csv', sep=',')
    Column_count = target_df.columns
    print(Column_count)

# Looking at the total count
def test_readTotalCount():
    target_df = pd.read_csv('/Users/sarojdahal/PycharmProjects/ETLTest/people-100.csv', sep=',')
    total_count = target_df.count()
    print(total_count)

# Looking the unique values
def test_readUniqueValues():
    target_df = pd.read_csv('/Users/sarojdahal/PycharmProjects/ETLTest/people-100.csv', sep=',')
    unique_value = target_df['Phone'].count()#unique()
    print(unique_value)

# Test the duplicate
def test_checkDuplicates():
    target_df = pd.read_csv('/Users/sarojdahal/PycharmProjects/ETLTest/people-100.csv', sep=',')
    count = target_df.duplicated().sum()
    assert count == 0 , "Duplicate rows found - Please verify the data"

# Test if target is not blank
def test_dataCompleteness():
    target_df = pd.read_csv('/Users/sarojdahal/PycharmProjects/ETLTest/people-100.csv', sep=',')
    assert not target_df.empty,"Target file is empty - Please verify ETL Process"

# Test if the column is mandatory
def test_nullValueCheck():
    target_df = pd.read_csv('/Users/sarojdahal/PycharmProjects/ETLTest/people-100.csv', sep=',')
    isFirstNameNull = target_df['First Name'].isnull().any()
    assert isFirstNameNull == False , "First Name is having a NULL value"


