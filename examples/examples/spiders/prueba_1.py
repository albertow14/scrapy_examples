# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin 
from scrapy import Request

class VinosCorteInglesSpider(scrapy.Spider):
    name = 'vinos_corte_ingles_1'
    allowed_domains = ['elcorteingles.es']
    start_urls = ['https://www.elcorteingles.es/club-del-gourmet/vinos/espana/']

    def parse(self, response):
        urls = response.xpath('//h3[@class="info-name"]/a/@href').extract()
        # print(urls)
        for url in urls:
            header = "https://www.elcorteingles.es"
            url = header + url
            print(url)
            yield Request(url, callback=self.extractor)
            # print(completas, "esto esta completo")
            # self._next_page(response)

    # def _next_page(self, response):
    #     siguiente_pagina = response.xpath('//a[text()="Siguiente"]/@href').extract_first()
    #     header = "https://www.elcorteingles.es"
    #     urls = response.urljoin(header + siguiente_pagina)
    #     print(urls)
    #     for url in urls:            
    #         yield Request(url)

    def extractor(self,response):
        titulo_ci = response.xpath('//h2[@itemprop="name"]/text()').extract_first()
        precio_ci_uno = response.xpath('//span[@class="current   "]/text()').extract_first()
        yield{'titulo_ci': titulo_ci, 'precio_ci':precio_ci_uno}
    pass
