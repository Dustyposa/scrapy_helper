from scrapy.cmdline import execute

spider_name = "xzl"  # spider name

execute(f"scrapy crawl {spider_name}".split())
