from product.robotspider import RobotSpider

class Spider(RobotSpider):
    name = 'baostar'

    start_urls = ('http://beta.baostar.com/search/bggm',)
    interest_rate = 1.0

    middle_pages = (
        r'^http://beta.baostar.com/search/bggm/\d+',
    )

    analyze_config = (
        (r'^http://beta.baostar.com/package/BGGM/\d+/', {
            'model': '//*//table[@class="dtl_sub_table"]//tr[1]/td[2]/text()',
            'trademark': '//*//table[@class="dtl_sub_table"]//tr[1]/td[4]/em/text()',
            'spec': '//*//table[@class="dtl_sub_table"]//tr[2]/td[2]/em/text()',
            'producer': '//*//table[@class="dtl_sub_table"]//tr[1]/td[6]/text()',
            'origin':'//*//table[@class="dtl_sub_table"]//tr[2]/td[6]/text()',
            'stock_location':'//*//table[@class="dtl_sub_table"]//tr[3]/td[4]/text()',
            'provider': '!beta.baostar.com',
            'price': '//*//div[@class="dtl_main_area"]//div[@class="right_area"]/ul/li[2]/strong/text()',
            'weight': '//*//div[@class="dtl_main_area"]//div[@class="right_area"]/ul/li[1]/strong/text()',
        }),
    )