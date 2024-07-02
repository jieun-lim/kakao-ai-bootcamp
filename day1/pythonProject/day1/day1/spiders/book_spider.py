import scrapy

class Book1Spider(scrapy.Spider):
  name = 'bookspider'
  start_urls = [
    'https://wikibook.co.kr/list/'
  ]

  def parse(self, response):
    # 도서 목록 추출
    title = response.css('title')
    print(title.extract())




