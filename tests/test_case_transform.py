import pytest
import pyspark.sql.functions as F
from pyspark.sql import SparkSession, DataFrame
from collections import Counter
from transforms.case_transform import case_transform

COLUMN_NAME = 'name'

@pytest.fixture(scope='module')
def spark():
    spark = (
        SparkSession.builder
        .appName("test_case_transform")
        .getOrCreate()
    )
    yield spark
    spark.stop()

@pytest.fixture(scope='module')
def accounts(spark):
    df = spark.read.option('header','true').csv('tests/resources/accounts.csv')
    yield df
    spark.stop()

def test_transform_lowercase(accounts):
    df: DataFrame = accounts
    case = 'lowercase'
    expected_values = [
        "abc company",
        "xyz corporation",
        "random casing ltd",
        "def industries"
    ]

    df = case_transform.transform(df, COLUMN_NAME, case)
    names_col = df.select(F.col(COLUMN_NAME)).collect()
    actual_values = [str(row[0]) for row in names_col]

    assert Counter(expected_values) == Counter(actual_values)
    
def test_transform_uppercase(accounts):
    df: DataFrame = accounts
    case = 'uppercase'
    expected_values = [
        "ABC COMPANY",
        "XYZ CORPORATION",
        "RANDOM CASING LTD",
        "DEF INDUSTRIES"
    ]

    df = case_transform.transform(df, COLUMN_NAME, case)
    names_col = df.select(F.col(COLUMN_NAME)).collect()
    actual_values = [str(row[0]) for row in names_col]

    assert Counter(expected_values) == Counter(actual_values)

def test_transform_bad_case(accounts):
    df: DataFrame = accounts
    case = "Lowercase"

    with pytest.raises(ValueError) as e:
        df = case_transform.transform(df, COLUMN_NAME, case)
    
    assert str(e.value) == "Provided value 'Lowercase' for parameter 'case' is invalid. Valid options are: uppercase, lowercase."

def test_transform_missing_name(accounts):
    pass

def test_transform_not_string(accounts):
    pass

