from awsglue import DynamicFrame
import pyspark.sql.functions as F
from pyspark.sql import DataFrame
from pyspark.sql.utils import AnalysisException

def transform(df: DataFrame, column_name: str, case: str) -> DataFrame:
    """
    transform handles the transformation and error handling logic for case_transform

    Args:
        df (DataFrame): The PySpark DataFrame of your data.
        column_name (str): The name of the column you would like to transform.
        case (str): Determines if you will transform to lowercase or uppercase.
    
    Returns:
        DynamicFrame: AWS Glue Dynamic frame with transformed column
    
    Raises:
        pypspark.sql.utils.AnalysisException if specified column isn't of type str.
        ValueError if column_name is not found in the DataFrame.
    """
    valid_cases = ['uppercase','lowercase']
    if case not in valid_cases:
        raise ValueError(f"Provided value '{case}' for parameter 'case' is invalid. Valid options are: {', '.join(valid_cases)}.")

    if not column_name in df.columns:
        raise ValueError(f"Column '{column_name}' not found in DataFrame.")
    
    if df.schema[column_name].dataType.simpleString() != "string":
        raise AnalysisException(f"Column '{column_name}' is not of StringType.")
    
    if case == "uppercase":
        df = df.withColumn(column_name, F.upper(F.col(column_name)))
    else:
        df = df.withColumn(column_name, F.lower(F.col(column_name)))
    
    return df
    

def case_transform(self, column_name: str, case: str) -> DynamicFrame:
    """
    case_transform will take your specified column name and either transform it to all upper or all lowercase.

    Args:
        column_name (str): The name of the column you would like to transform.
        case (str): Determines if you will transform to lowercase or uppercase.
    
    Returns:
        DynamicFrame: AWS Glue Dynamic frame with transformed column
    
    Raises:
        pypspark.sql.utils.AnalysisException if specified column isn't of type str.
        ValueError if column_name is not found in the DataFrame.
    """
    df: DataFrame = self.toDF()
    df = transform(df, column_name, case)
    return DynamicFrame.fromDF(df, self.glue_ctx, "case_transform")    
    
DynamicFrame.case_transform = case_transform