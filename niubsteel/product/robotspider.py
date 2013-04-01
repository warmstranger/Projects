from scrapy.spider import BaseSpider
from scrapy.item import Item, Field
from scrapy.http import Request
from scrapy.conf import settings

from lxml import etree
from BeautifulSoup import BeautifulSoup
import urlparse, re, random

class RobotSpider(BaseSpider):

    encoding = 'utf8'
    analyze_config = []
    interest_rate = 0.65
    delay = 0
    push_batch_amount = 100

    def __init__(self):
        super(RobotSpider, self).__init__()

        settings.overrides['DOWNLOAD_DELAY'] = self.delay
        self._links_crawled = []

        if not self.middle_pages:
            self.middle_pages = []
            for root_url in self.start_urls:
                parse_result = urlparse.urlsplit(root_url)
                middle_pattern = '%s://%s' % (parse_result.scheme, parse_result.netloc)
                if not middle_pattern in self.middle_pages:
                    self.middle_pages.append(middle_pattern)

    def build_item(self, page_element, parse_config, base_url):
        item = Item()
        item.fields['url'] = Field()
        item['url'] = base_url
        for key, xpath in parse_config.iteritems():
            if not item.fields.has_key(key):
                item.fields[key] = Field()
            if xpath.startswith('!'):
                item[key] = xpath[1:]
                continue
            if xpath:
                text = ''.join(page_element.xpath(xpath)).strip()
            else:
                text = ''
            if 'image' in key or 'url' in key:
                text = urlparse.urljoin(base_url, text)
            item[key] = text
        return item

    def get_parse_config(self, url):
        for url_pattern, parse_config in self.analyze_config:
            if re.match(url_pattern, url):
                return parse_config

    def is_middle_page(self, url):
        for middle_page_pattern in self.middle_pages:
            if re.match(middle_page_pattern, url):
                return True
        return False

    def start_requests(self):
        self._links_crawled = []
        return super(RobotSpider, self).start_requests()

    def parse(self, response):
        if response.url in self._links_crawled:
            return

        self._links_crawled.append(response.url)
        element = etree.HTML(response.body, parser=etree.HTMLParser(encoding=self.encoding))
        soup = BeautifulSoup(response.body)
        parse_config = self.get_parse_config(response.url)
        if parse_config:
            yield self.build_item(element, parse_config, response.url)

        links = [urlparse.urljoin(response.url, _['href']) for _ in soup.findAll('a') if _.has_key('href')]
#        links = [urlparse.urljoin(response.url, _) for _ in element.xpath('//*/a/@href')]
        for link in links:
            if self.get_parse_config(link):
                yield Request(link)

            if self.is_middle_page(link):
                interest = response.meta.get('interest', 1.0)
                sample = random.random()
                if interest > sample:
                    yield Request(link, meta={'interest': interest*self.interest_rate})
