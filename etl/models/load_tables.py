def process(sparksession, table_name, source_db_url, destination_db_url):
    # print(source_db_url)
    source_df = sparksession.read \
        .format("jdbc") \
        .option("url", source_db_url) \
        .option("dbtable", table_name) \
        .load()
    
    source_df.write.format("jdbc") \
        .option("url", destination_db_url) \
        .option("dbtable", table_name) \
        .mode('overwrite') \
        .save()
    