from urllib2 import urlopen
from lxml import etree
from models import Product, ProductMeta
from tag.models import Tag
from config.tags import MODEL_TAGS, TRADEMARK_TAGS
import re, utils, spiders


def analyze(url):
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url

    response = urlopen(url).read()

    for spider_class in spiders.all_spiders:
        spider = spider_class()
        element = etree.HTML(response, parser=etree.HTMLParser(encoding=spider.encoding))
        parse_config = spider.get_parse_config(url)
        if parse_config:
            item = spider.build_item(element, parse_config, url)
            product = Product()
            product.url = url
            product.title = item['title']
            product.image = item['image']
            product.price = item['price']
            return product

keyword_model_dict = {}
for model_tag in MODEL_TAGS:
    for keyword in model_tag:
        keyword_model_dict[keyword.upper()], _ = Tag.objects.get_or_create(name=model_tag[0])

keyword_trademark_dict = {}
for trademark_tag in TRADEMARK_TAGS:
    for keyword in trademark_tag:
        keyword_trademark_dict[keyword.upper()], _ = Tag.objects.get_or_create(name=trademark_tag[0])

def query_analyze(query):
    keywords = query.split(' ')

    search_model_tags = []
    search_trademark_tags = []
    width, thick = 0.0, 0.0

    for keyword in keywords:
        is_tag = False
        if keyword_model_dict.has_key(keyword.upper()):
            search_model_tags.append(keyword_model_dict[keyword.upper()])
            is_tag = True

        if keyword_trademark_dict.has_key(keyword.upper()):
            search_trademark_tags.append(keyword_trademark_dict[keyword.upper()])
            is_tag = True

        if not is_tag:
            if '*' in keyword:
                width, thick = utils.analyze_spec(keyword)
            try:
                number = float(keyword)
                if not width:
                    width = number
                else:
                    if not thick:
                        thick = number
            except:
                continue

    model_tags = [_.name for _ in search_model_tags]
    model_tags.sort()
    model_tags = ' '.join(model_tags)
    trademark_tags = [_.name for _ in search_trademark_tags]
    trademark_tags.sort()
    trademark_tags = ' '.join(trademark_tags)

    return model_tags, trademark_tags, width, thick

def search(query):
    model_tags, trademark_tags, width, thick = query_analyze(query)
    meta_candidates = ProductMeta.objects.all()
    if model_tags:
        meta_candidates = meta_candidates.filter(model_tags=model_tags)
    if trademark_tags:
        meta_candidates = meta_candidates.filter(trademark_tags=trademark_tags)
    if width:
        meta_candidates = meta_candidates.filter(width=width)
    if thick:
        meta_candidates = meta_candidates.filter(thick=thick)

    meta_candidates = meta_candidates.order_by('best_price')

    search_result = []
    for meta in meta_candidates:
        search_result.append(meta)

    return search_result


