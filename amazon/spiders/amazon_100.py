import scrapy
from ..items import AmazonItem

class Amazon100Spider(scrapy.Spider):
    name = 'amazon-100'
    start_urls = ['https://www.amazon.in/s?k=books&i=stripbooks&rh=n%3A976389031%2Cp_n_publication_date%3A2684819031&dc&page=1&qid=1638185601&rnid=2684818031&ref=sr_pg_2']
    page_number = 2

    def _parse(self, response, **kwargs):
        items = AmazonItem()

        book_name = response.css('.a-color-base.a-text-normal').css("::text").extract()
        book_author = response.css('.a-color-secondary .a-size-base.a-link-normal , .a-color-secondary .a-size-base+ .a-size-base').css("::text").extract()
        book_price = response.css('.a-spacing-top-small .a-price-whole').css("::text").extract()
        book_image = response.css('.a-spacing-top-small .a-price-whole::attr(src)').extract()


        items['book_name'] = book_name
        items['book_author'] = book_author
        items['book_price'] = book_price
        items['book_image'] = book_image

        next_page = 'https://www.amazon.in/s?k=books&i=stripbooks&rh=n%3A976389031%2Cp_n_publication_date%3A2684819031&dc&page= '+ str(Amazon100Spider.page_number) +'&qid=1638185601&rnid=2684818031&ref=sr_pg_2'

        if Amazon100Spider.page_number <= 100:
            Amazon100Spider.page_number +=1
            yield response.follow(next_page, callback=self.parse)





