from scrapy.cmdline import execute

spider_name = "lianjia"  # spider name

execute(f"scrapy crawl {spider_name}".split())
