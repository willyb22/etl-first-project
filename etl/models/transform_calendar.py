def process(sparksession, source_db_url, destination_db_url):
    # print(source_db_url)
    source_df = sparksession.read \
        .format("jdbc") \
        .option("url", source_db_url) \
        .option("dbtable", "calendar") \
        .load() \
        .select("date", "holidaytype") 

    source_df.write.format("jdbc") \
        .option("url", destination_db_url) \
        .option("dbtable", "calendar") \
        .mode('overwrite') \
        .save()
    