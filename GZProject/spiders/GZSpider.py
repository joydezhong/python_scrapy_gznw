import scrapy
import pprint
from GZProject.items import GzprojectItem

class GZSpider(scrapy.Spider):
    name = "gznw"  # 贵州农产品爬虫
    allowed_domains = ["gznw.com"]
    base_url = "https://www.gznw.com/eportal/ui"  # 这是获取分页数据的API端点
    pageNumber = 1  # 初始页数
    pageSize = 20   # 每页条目数量

    def start_requests(self):
        # 初始化第一页的GET请求
        yield scrapy.Request(
            url=self.build_url(self.pageNumber),
            callback=self.parse,
            meta={'page_number': self.pageNumber},
            dont_filter=True
        )

    def build_url(self, page_num):
        return f"{self.base_url}?pageSize={self.pageSize}&pageNum={page_num}&recruitType=1&moduleId=ab59857100d84dcca372ff4473198d88&struts.portlet.mode=view&struts.portlet.action=/portlet/priceFront!queryFrontList.action"

    def parse(self, response):
        print(response.url)
        print('----------------------Start Parsing Page {}-----------------------'.format(response.meta['page_number']))

        try:
            data = response.json()  # 解析JSON响应
            items = data.get('rows', [])  # JSON数据在一个名为'rows'的键中
            pprint.pprint(items)
            for item in items:
                gz_item = GzprojectItem()
                gz_item['name'] = item.get('v0027')
                gz_item['price_type'] = item.get('v0036')
                gz_item['price'] = item.get('v0005')
                gz_item['unit'] = item.get('v0014')
                gz_item['market_name'] = item.get('v0031')
                gz_item['time'] = item.get('v0004')
                yield gz_item  # 使用yield返回每一个item

            print('----------------------End Parsing Page {}-----------------------'.format(response.meta['page_number']))
            print(f'Page Number: {response.meta["page_number"]}')
            # 控制分页
            # total_pages = data.get('totalPages', 0)  # 假设总页数在一个名为'totalPages'的键中
            if response.meta['page_number'] < 3:  # 确保还有更多页面可抓取
                next_page_number = response.meta['page_number'] + 1
                # 发送下一页的GET请求
                yield scrapy.Request(
                    url=self.build_url(next_page_number),
                    callback=self.parse,
                    meta={'page_number': next_page_number},
                    dont_filter=True
                )
        except Exception as e:
            self.logger.error(f"Failed to parse or navigate to the next page: {e}")


#### 最后执行命令 输出 json 文件：scrapy crawl gznw -o products.json --nolog