from scrapy.crawler import CrawlerProcess
from multiprocessing import Pool
import os


def _crawl(spiderName=None):
    if spiderName:
        cmd = 'scrapy runspider ./Spiders/{}.py'.format(spiderName)
        os.system(cmd)

    return None


def run(spider_names):
    pool = Pool(processes=len(spider_names))
    pool.map(_crawl, spider_names)
