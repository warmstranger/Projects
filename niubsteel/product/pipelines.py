from scrapy.conf import settings
from scrapy.exceptions import DropItem

import urllib, urllib2, json

class RobotPipeline(object):
    items_scanned = []

    def process_item(self, item, spider):
        self.items_scanned.append(item.__dict__['_values'])
        return item

    def open_spider(self, spider):
        self.items_scanned = []

    def close_spider(self, spider):
        data = {
            'items': json.dumps(self.items_scanned),
        }
        encoded_data = urllib.urlencode(data)
        remote_server = '127.0.0.1:8000'
        if settings.get('REMOTE_SERVER'):
            remote_server = settings.get('REMOTE_SERVER')

        text = urllib2.urlopen('http://%s/robot/push' % remote_server, encoded_data).read()
        print text

class LimitPipeline(object):
    limit = 500
    count = 0

    def process_item(self, item, spider):
        if self.count == self.limit:
            raise DropItem('exceed limit. Dropping item.')
        self.count += 1
        return item

    def open_spider(self, spider):
        self.count = 0
