# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from multiprocessing import connection
from itemadapter import ItemAdapter
import sqlite3



class SQLlitePipeline(object):
    
    def open_spider(self, spider):
        self.connection = sqlite3.connect("IMDb.db")
        self.c = self.connection.cursor()
        self.c.execute('''
        CREATE TABLE imdb_top_250(
            title TEXT,
            year TEXT,
            duration TEXT,
            genre TEXT,
            rating TEXT,
            movie_url TEXT
        )
        ''')

        self.connection.commit()

    def close_spider(self, spider):
        self.connection.close()


    def process_item(self, item, spider):
        self.c.execute('''
            INSERT INTO imdb_top_250(title, year, duration, genre, rating, movie_url) VALUES (?, ?, ?, ?, ?, ?)

        ''', (
            item.get("title"),
            item.get("year"),
            item.get("duration"),
            item.get("genre"),
            item.get("rating"),
            item.get("movie_url")
        ))

        self.connection.commit()
        return item
