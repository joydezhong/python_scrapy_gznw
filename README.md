## 基于 Python+scrapy 的爬虫案例

以贵州农产品网为例 https://www.gznw.com/eportal/ui?pageId=595091 ，仅供学习使用。

对于 win 环境来说：

首先，安装 python 并配置环境变量，通过 pip 安装，

```
pip install Scrapy
```

然后，通过 scrapy 命令创建爬虫项目，

```
scrapy startproject GZProject
```

编辑好对应的代码，终端 cd 到项目目录下，执行命令把获取的数据输出到 json 文件中，

```
scrapy crawl gznw -o products.json --nolog
```
