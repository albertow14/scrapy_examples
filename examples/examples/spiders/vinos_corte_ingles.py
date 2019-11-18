# -*- coding: utf-8 -*-
import scrapy


# queremos extraer todos los precios y titulos de los vinos con sus paginaciones
# Normalmente el parse nos sirve para definir el proceso de extraccion de las urls




class VinosCorteInglesSpider(scrapy.Spider):
    name = 'vinos_corte_ingles'
    allowed_domains = ['https://www.elcorteingles.es/club-del-gourmet/vinos/espana/']
    start_urls = ['http://https://www.elcorteingles.es/club-del-gourmet/vinos/espana//']

    def parse(self, response):
            
        for n in range (0,38):
            print(f'https://www.elcorteingles.es/club-del-gourmet/vinos/espana/{n}/')
            # urls = 'https://www.elcorteingles.es/club-del-gourmet/vinos/espana/{n}/'
                #hacer con una comprenhension list 


        # siguiente_url = response.xpath('//a[contains(.,"Siguiente")]').extract()
       
        pass

    # def extractor(self,response):
        # titulo_ci = response.xpath('//h3[@class="info-name]/a/@title').extract()
        # precio_ci = response.xpath('//div[@class="product-price"]/span/text()').extract()

        # yield{'titulo_ci': titulo_ci, 'precio_ci':precio_ci}