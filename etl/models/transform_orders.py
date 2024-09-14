def process(sparksession, source_db_url, destination_db_url):
    df_orders = sparksession.read \
        .format("jdbc") \
        .option("url", source_db_url) \
        .option("dbtable", "orders") \
        .load() \
        .select("orderid", "numorderlines", "numunits", "paymenttype" \
                , "totalprice", "state", "city", "orderdate", "campaignid") 
    
    df_orders.write.format("jdbc") \
        .option("url", destination_db_url) \
        .option("dbtable", "orders") \
        .mode('overwrite') \
        .save()
    
    df_orderlines = sparksession.read \
        .format("jdbc") \
        .option("url", source_db_url) \
        .option("dbtable", "orderlines") \
        .load() \
        .select("orderid", "productid", "shipdate", "billdate", "unitprice", "numunits")
    
    df_orderlines.write.format("jdbc") \
        .option("url", destination_db_url) \
        .option("dbtable", "orderlines") \
        .mode('overwrite') \
        .save()
    
    df_products = sparksession.read \
        .format("jdbc") \
        .option("url", source_db_url) \
        .option("dbtable", "products") \
        .load() \
        .select("productid", "groupname", "isinstock", "fullprice")
    
    df_products.write.format("jdbc") \
        .option("url", destination_db_url) \
        .option("dbtable", "products") \
        .mode('overwrite') \
        .save()
