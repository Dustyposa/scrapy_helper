from scrapy.cmdline import execute

spider_name = "ftx"  # spider name

execute(f"scrapy crawl {spider_name}".split())
