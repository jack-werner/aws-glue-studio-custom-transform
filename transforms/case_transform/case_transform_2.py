from awsglue import DynamicFrame
import pyspark.sql.functions as F
from pyspark.sql.utils import AnalysisException



def case_transform(self, column_name, case):
    """
    case_transform will take your specified column name and either transform it to all upper or all lowercase.

    params:
        co 
    """
    # logger = self.glue_ctx.get_logger()
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