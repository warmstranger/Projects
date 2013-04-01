from scrapy.conf import settings

from scrapy.exceptions import CloseSpider
import urllib, urllib2, json

def push_data(items):
    data = {
        'items': json.dumps(items),
        }
    encoded_data = urllib.urlencode(data)
    remote_server = '127.0.0.1:8000'
    if settings.get('REMOTE_SERVER'):
        remote_server = settings.get('REMOTE_SERVER')
    text = urllib2.urlopen('http://%s/robot/push' % remote_server, encoded_data).read()
    print text

class RobotPipeline(object):
    items_scanned = []
    push_count = 0

    def process_item(self, item, spider):
        self.items_scanned.append(item.__dict__['_values'])

        amount = 100 if not hasattr(spider, 'push_batch_amount') else spider.push_batch_amount
        push_limit = 300 if not hasattr(spider, 'push_limit') else spider.push_limit

        if len(self.items_scanned) >= amount:
            print 'pushing...'
            push_data(self.items_scanned)

            self.push_count += len(self.items_scanned)

            if self.push_count >  push_limit:
                spider.over_limit = True

            self.items_scanned = []

        return item

    def open_spider(self, spider):
        self.items_scanned = []

    def close_spider(self, spider):
        push_data(self.items_scanned)
