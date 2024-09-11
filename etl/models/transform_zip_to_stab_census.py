from pyspark.sql.functions import sum

def process(sparksession, source_db_url, destination_db_url):
    print(source_db_url)
    source_df = sparksession.read \
        .format("jdbc") \
        .option("url", source_db_url) \
        .option("dbtable", "zipcensus") \
        .load()
    
    group_df = source_df.groupBy("stab") \
        .agg(
            sum("landsqmi").alias("total_landsqmi"),
            sum("totpop").alias("total_population")
        )
    # dfp = group_df.toPandas()
    # dfp.to_sql('stabcensus', con=engine, if_exists='replace', index=False)
    group_df.write.format("jdbc") \
        .option("url", destination_db_url) \
        .option("dbtable", "stabcensus") \
        .mode('overwrite') \
        .save()
    