from awsglue import DynamicFrame
import pyspark.sql.functions as F
from pyspark.sql.utils import AnalysisException

def case_transform(self, column_name, case):
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
    df = self.toDF()

    try:
        if df.schema[column_name].dataType.simpleString() == "string":
            if case == "uppercase":
                df = df.withColumn(column_name, F.upper(F.col(column_name)))
            else:
                df = df.withColumn(column_name, F.lower(F.col(column_name)))
        else:
            raise AnalysisException(f"Column '{column_name}' is not of StringType.")
    except KeyError:
        raise ValueError(f"Column '{column_name}' not found in DataFrame.")
    
    return DynamicFrame.fromDF(df, self.glue_ctx, "case_transform")    
    
DynamicFrame.case_transform = case_transform