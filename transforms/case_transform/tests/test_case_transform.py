import pytest
import pyspark.sql.functions as F
from pyspark.sql import SparkSession, DataFrame
from collections import Counter
from transforms.case_transform import transform

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
    return spark.read.csv('resources/accounts.csv')

def test_transform(accounts):
    df: DataFrame = accounts
    column_name = 'name'
    case = 'uppercase'

    df = transform(df, column_name, case)

    actual_values = [row[F.col(column_name)] for row in df.select(column_name)]
    expected_values = [
        "abc company",
        "xyz corporation",
        "random casing ltd",
        "def industries"
    ]


    assert Counter(expected_values) == Counter(actual_values)


    

