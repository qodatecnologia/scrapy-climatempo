# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class ClimatempoPipeline:
    def __init__(self):
    	self.conn = pymongo.MongoClient(
    		'localhost',
    		27017
    		)  #connect to mongodb
    	db = self.conn['ctdatabase'] # create database
    	self.collection = db['ct_table'] # create collection

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
