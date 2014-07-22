# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class PropertyItem(Item):
    attr = Field()
    file_id = Field()
    seq = Field()
    stage = Field()
    date = Field()
    name = Field()
    journal = Field()
    department = Field()
    title = Field()
    category = Field()
    publication_date = Field()
    at_page = Field()
    download_url = Field()
    pass
