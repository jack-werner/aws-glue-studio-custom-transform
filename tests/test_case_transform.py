import pytest
import pyspark.sql.functions as F
from pyspark.sql import SparkSession, DataFrame
from collections import Counter
from transforms.case_transform import case_transform

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

def test_transform(accounts):
    df: DataFrame = accounts
    column_name = 'name'
    case = 'lowercase'

    df = case_transform.transform(df, column_name, case)
    
    names_col = df.select(F.col(column_name)).collect()
    actual_values = [str(row[0]) for row in names_col]
    expected_values = [
        "abc company",
        "xyz corporation",
        "random casing ltd",
        "def industries"
    ]

    assert Counter(expected_values) == Counter(actual_values)


    

