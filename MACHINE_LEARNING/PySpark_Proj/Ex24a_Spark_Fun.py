from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.tree import DecisionTree
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import to_binary
from numpy import array

spark = SparkSession.builder.master("local").appName("Spark Test").getOrCreate()
#conf = SparkConf().setMaster("local").setAppName("SparkDecisionTree")
#sc = SparkContext(conf = conf)

def binary(YN):
    if (YN == 'Y'):
        return 1
    else:
        return 0

def createLabeledPoints(row):
    yearsExperience = int(row[0])
    employed = binary(row[1])
    previousEmployers = int(row[2])
    #educationLevel = mapEducation(row[3])
    topTier = binary(row[4])
    interned = binary(row[5])
    hired = binary(row[6])
    return LabeledPoint(hired, array([yearsExperience, employed, previousEmployers, topTier, interned]))

rawData = spark.read.option("header", True).option("inferSchema", True).csv("/Users/sanjaybiswas/Documents/Pycharm/data/PastHires.csv")
header = rawData.columns
trainingData = rawData.rdd.map(createLabeledPoints)
trainingData.toDF().show()
print(header)