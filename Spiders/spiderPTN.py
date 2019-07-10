import scrapy
import os
import pandas as pd


class spiderPTN(scrapy.Spider):
    name = 'spiderPTN'
    allowed_domains = ['sbmptn.ltmpt.ac.id']

    start_urls = ['https://sbmptn.ltmpt.ac.id/index.php?mid=14']

    fileFormat = 'csv'
    fileName = 'dataPTN' + '.' + fileFormat
    fileAvailable = os.path.isfile(fileName)

    if fileAvailable:
        open(fileName, 'w+')

    custom_settings = {
        'FEED_FORMAT': fileFormat,
        'FEED_URI': fileName
    }

    def parse(self, response):
        MAIN_XPATH = '/html/body/div[2]/div/div[2]/div/div/div'

        TABLE_XPATH = MAIN_XPATH + '/table[1]/tbody'
        TABLE_SELECTOR = response.xpath(TABLE_XPATH)

        RECORD_XPATH = './/tr[position()>0 and position()<=last()]'
        RECORD_SELECTOR = TABLE_SELECTOR.xpath(RECORD_XPATH)

        for rset in RECORD_SELECTOR:
            DATA = {
                'kode_ptn': rset.xpath('.//td[1]/text()').extract_first(),
                'nama_ptn': rset.xpath('.//td[2]/text()').extract_first(),
            }

            yield DATA
