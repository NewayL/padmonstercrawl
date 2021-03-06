# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PadmonsterItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    rarity = scrapy.Field()
    attrs = scrapy.Field()
    types = scrapy.Field()
    hp_lv_max = scrapy.Field()
    att_lv_max = scrapy.Field()
    rec_lv_max = scrapy.Field()
    active_skill_name = scrapy.Field()
    active_skill_init_cd = scrapy.Field()
    active_skill_min_cd = scrapy.Field()
    active_skill_description = scrapy.Field()
    awaken_skills = scrapy.Field()
    leader_skill_name = scrapy.Field()
    leader_skill_type = scrapy.Field()
    leader_skill_description = scrapy.Field()
    pass
