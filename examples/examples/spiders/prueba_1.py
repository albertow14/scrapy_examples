# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin 
from scrapy import Request

class VinosCorteInglesSpider(scrapy.Spider):
    name = 'vinos_corte_ingles_1'
    allowed_domains = ['elcorteingles.es']
    start_urls = ['https://www.elcorteingles.es/club-del-gourmet/vinos/espana/']

    # def __init__(self):
    #     self.counter = 0

    # def parse(self, response):
    #     self.after_parse(response)

    def parse(self, response):
        urls = response.xpath('//h3[@class="info-name"]/a/@href').extract()
        # print(urls)
        for url in urls:
            header = "https://www.elcorteingles.es"
            url = header + url
            print(url)
            titulo_ci = response.xpath('//h2[@itemprop="name"]/text()').extract_first()
            precio_ci_uno = response.xpath('//span[@class="current   "]/text()').extract_first()
            yield{'titulo_ci': titulo_ci, 'precio_ci':precio_ci_uno}
        
        siguiente_pagina = response.xpath('//a[text()="Siguiente"]/@href').extract_first()
        urls_siguiente_pagina = response.urljoin(header + siguiente_pagina)
        if urls_siguiente_pagina is not None:
            yield scrapy.Request(response.urljoin(urls_siguiente_pagina))
        # self.siguiente_url(siguiente_pagina, response)
        
        # extraes el culo de la url, que te da cuando pinchas en el boton siguiente, extra

    # def siguiente_url(self, tail_url, response):
    #     self.counter += 1
    #     HEADER = "https://www.elcorteingles.es"
    #     urls_siguiente_pagina = response.urljoin(HEADER + tail_url)
    #     print(urls_siguiente_pagina)
    #     if self.counter <= 36:
    #         self.after_parse(response)


            # print(completas, "esto esta completo")
            # self._next_page(response)

    # def _next_page(self, response):
    #     siguiente_pagina = response.xpath('//a[text()="Siguiente"]/@href').extract_first()
    #     header = "https://www.elcorteingles.es"
    #     urls = response.urljoin(header + siguiente_pagina)
    #     print(urls)
    #     for url in urls:            
    #         yield Request(url)
