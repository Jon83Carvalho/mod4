from pyspark import SparkContext, SparkConf
from pyspar.sql import SparkSession
import os

aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID']
aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']

print("Chegamos até aqui-1")

conf=(
SparkConf()
    .set("spark.hadoop.fs.s3a.access.key",aws_access_key_id)
    .set("spark.hadoop.fs.s3a.secret.key",aws_secret_access_key)
    .set("spark.hadoop.fs.s3a.fast.upload",True)
    .set("spark.hadoop.fs.s3a.impl","org.apache.hadoop.fs.s3a.S3AFileSystem")
    .set("spark.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.3")
)

print("Chegamos até aqui-2")

sc=SparkContext(conf=conf).getOrCreate()

if __name__="__main__":
    spark=SparkSession\
        .builder\
        .appName("Repartition Job")\
        .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    df=(
        spark
        .read
        .format("csv")
        .options(header='true',inferSchema='true', delimiter=',')
        .load("s3a://igticlusterbucket/raw/enem/MICRODADOS_ENEM_2019.csv")
    )

    df.show()
    df.printSchema()

    (df
    .write
    .mode("overwrite")
    .format("parquet")
    .save("s3a://igticlusterbucket/process/enem")
    )

    print("***********")
    print("Funcionou")
    print("***********")

    spark.stop()

