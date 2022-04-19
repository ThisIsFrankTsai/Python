# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class PttPipeline:
    def process_item(self, item, spider):
        item['push'] = int(item['push'])
        return item

class DeleteNullTitlePipeline(object):
    def process_item(self, item, spider):
        title = item['title']
        if title:
            return item
        else:
            raise DropItem('found null title %s', item)