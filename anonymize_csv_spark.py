from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from faker import Faker

fake = Faker()

spark = SparkSession.builder.appName("Anonymize CSV").getOrCreate()

def anonymize_row(row):
    row.first_name = fake.first_name()
    row.last_name = fake.last_name()
    row.address = fake.street_address()
    return row

anonymize_udf = udf(anonymize_row)

input_file = 'input.csv'
output_file = 'output.csv'

df = spark.read.csv(input_file, header=True, inferSchema=True)
anonymized_df = df.select(anonymize_udf('first_name', 'last_name', 'address').alias('first_name', 'last_name', 'address'), 'date_of_birth')
anonymized_df.write.csv(output_file, header=True)

spark.stop()