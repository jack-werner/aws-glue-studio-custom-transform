# pylint: disable=W0621

"test_case_transform contains the unit tests for the transforms.case_transform module"
from collections import Counter
import pytest
import pyspark.sql.functions as F
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import StructType, StringType, StructField, DateType, IntegerType
from pyspark.sql.utils import AnalysisException
from transforms.case_transform import case_transform

COLUMN_NAME = "name"
CASE = "lowercase"


@pytest.fixture(scope="module")
def spark_session():
    "Test fixture that returns a shared SparkSession"
    spark = SparkSession.builder.appName("test_case_transform").getOrCreate()
    yield spark
    spark.stop()


@pytest.fixture(scope="module")
def accounts(spark_session):
    "Test fixture that returns a Spark DataFrame"
    spark = spark_session
    schema = StructType(
        [
            StructField("id", IntegerType(), False),
            StructField("name", StringType(), False),
            StructField("created_date", DateType(), False),
            StructField("state", StringType(), False),
            StructField("sector", StringType(), False),
        ]
    )

    df = (
        spark.read.option("header", "true")
        .schema(schema)
        .csv("tests/resources/accounts.csv")
    )
    yield df
    spark.stop()


def test_transform_lowercase(accounts):
    "Tests lowercase transform works properly"
    df: DataFrame = accounts
    expected_values = [
        "abc company",
        "xyz corporation",
        "random casing ltd",
        "def industries",
    ]

    df = case_transform.transform(df, COLUMN_NAME, CASE)
    names_col = df.select(F.col(COLUMN_NAME)).collect()
    actual_values = [str(row[0]) for row in names_col]

    assert Counter(expected_values) == Counter(actual_values)


def test_transform_uppercase(accounts):
    "Tests uppercase transform works properly"
    df: DataFrame = accounts
    case = "uppercase"
    expected_values = [
        "ABC COMPANY",
        "XYZ CORPORATION",
        "RANDOM CASING LTD",
        "DEF INDUSTRIES",
    ]

    df = case_transform.transform(df, COLUMN_NAME, case)
    names_col = df.select(F.col(COLUMN_NAME)).collect()
    actual_values = [str(row[0]) for row in names_col]

    assert Counter(expected_values) == Counter(actual_values)


def test_transform_bad_case(accounts):
    "Tests bad case error is raised properly"
    df: DataFrame = accounts
    case = "Lowercase"

    with pytest.raises(ValueError) as e:
        df = case_transform.transform(df, COLUMN_NAME, case)

    assert str(e.value) == (
        "Provided value 'Lowercase' for parameter 'case' is invalid. Valid options are: uppercase, lowercase."  # pylint: disable=C0301
    )


def test_transform_missing_col(accounts):
    "Tests missing column error is raised properly"
    df: DataFrame = accounts

    with pytest.raises(ValueError) as e:
        df = case_transform.transform(df, "Name", CASE)

    assert str(e.value) == "Column 'Name' not found in DataFrame."


def test_transform_not_string(accounts):
    "Tests bad column type error is raised properly"
    df: DataFrame = accounts

    with pytest.raises(AnalysisException) as e:
        df = case_transform.transform(df, "created_date", CASE)

    assert str(e.value) == "Column 'created_date' is not of StringType."


def test_false():
    assert False
