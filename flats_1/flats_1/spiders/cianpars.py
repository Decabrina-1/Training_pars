import scrapy


class CianparsSpider(scrapy.Spider):
    name = "cianpars"
    allowed_domains = ["cian.ru"]
    start_urls = ["https://cian.ru/cat.php?bbox=55.66337203407646%2C37.431589993648245%2C55.68786539541125%2C37.56342593114823&center=55.675620639866175%2C37.49750796239824&deal_type=sale&demolished_in_moscow_programm=0&district[0]=119&electronic_trading=2&engine_version=2&object_type[0]=1&offer_seller_type[0]=2&offer_type=flat&only_flat=1&region=1&room1=1&zoom=14"]

    def parse(self, response):
        pass
