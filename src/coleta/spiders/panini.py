import scrapy


class AmazonSpider(scrapy.Spider):
    name = "panini"
    allowed_domains = ["panini.com.br"]
    start_urls = ["https://panini.com.br/planet-manga"]
    page_count = 1
    max_pages = 150


    def parse(self, response):
        produtos = response.css('div.product-item-info')
        for produto in produtos:
            yield {
            'nome': produto.css('a.product-item-link::text').get(),
            'preco': produto.css('span.price::text').get(),
            'pagina': self.page_count
            }
        if self.page_count < self.max_pages:
            next_page = response.css('li.item.pages-item-next a::attr(href)').get()
            if next_page:
                self.page_count += 1
                yield scrapy.Request(url=next_page, callback=self.parse)
