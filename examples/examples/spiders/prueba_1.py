# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin 
from scrapy import Request

class Prueba2Spider(scrapy.Spider):
    name = 'prueba2'
    allowed_domains = ['elcorteingles.es']
    start_urls = ['https://www.elcorteingles.es/club-del-gourmet/vinos/espana/']

    def parse(self, response):
        urls = response.xpath('//h3[@class="info-name"]/a/@href').extract()
        for url in urls:
            string = "https://www.elcorteingles.es"
            completas = [string + y for y in urls]
            for x in completas:
                todas_las_urls = x 
            yield Request(todas_las_urls, callback=self.extractor)

        siguiente_pagina = response.xpath('//a[text()="Siguiente"]/@href').extract_first()
        string = "https://www.elcorteingles.es"
        completas = response.urljoin("https://www.elcorteingles.es" + siguiente_pagina)
        print(completas)
        for x in completas:
            todas_las_urls_1 = x 
        yield Request (todas_las_urls_1)

    def extractor(self,response):
        titulo_ci = response.xpath('//h2[@itemprop="name"]/text()').extract_first()
        precio_ci_uno = response.xpath('//span[@class="current   "]/text()').extract_first()
        yield{'titulo_ci': titulo_ci, 'precio_ci':precio_ci_uno}
    pass
