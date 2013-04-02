from product.robotspider import RobotSpider

class Spider(RobotSpider):
    encoding = 'gbk'
    name = 'opsteel'

    start_urls = ('http://www.opsteel.cn/quote/shanghai.html',)
    interest_rate = 1.0
    delay = 2
    push_batch_amount = 4

    middle_pages = (
        r'^http://www.opsteel.cn/quote/shanghai(_\d)?.html',
        r'^http://www.opsteel.cn/quote/guangzhou(_\d)?.html',
        r'^http://www.opsteel.cn/quote/foshan(_\d)?.html',
        r'^http://www.opsteel.cn/quote/lecong(_\d)?.html',
        r'^http://www.opsteel.cn/quote/wuhan(_\d)?.html',
        r'^http://www.opsteel.cn/quote/beijing(_\d)?.html',
        r'^http://www.opsteel.cn/quote/tianjin(_\d)?.html',
    )

    analyze_config = (
        (r'^http://www.opsteel.cn/products/quote-\S+.html', {
            'model': '//*//div[@class="item1"]//div[@class="fL"]/p[1]/text()',
            'trademark': '//*//div[@class="item1"]//div[@class="fL"]/p[3]/text()',
            'spec': '//*//div[@class="item1"]//div[@class="fL"]/p[2]/text()',
            'producer': '//*//div[@class="item1"]//div[@class="fL"]/p[4]/text()',
            'origin':'//*//div[@class="item1"]//div[@class="fL"]/p[6]/text()',
            'stock_location':'//*//div[@class="item1"]//div[@class="fL"]/p[7]/text()',
            'provider': '//*//p[@id="pro-comp-name"]//a[@class="blue"]/text()',
            'price': '//*//div[@class="item1"]//div[@class="fL"]/p[9]/em/span/text()',
            'weight': '//*//div[@class="item1"]//div[@class="fL"]/p[5]/text()',
            }),
        )