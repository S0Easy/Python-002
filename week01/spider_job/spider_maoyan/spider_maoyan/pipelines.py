# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class SpiderMaoyanPipeline:


    def process_item(self, item, spider):
         
        Title = item["Title"]
        Type = item["Type"]
        Release_Date = item["Release_Date"]

        import csv
        with open('./maoyanmovie.csv','a+',encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([Title, Type, Release_Date])
        return item