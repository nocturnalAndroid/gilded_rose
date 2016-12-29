# -*- coding: utf-8 -*-
# Leroy you are just stupid as hell

class GildedRose(object):

    QUALITY_MAX = 50
    QUALITY_MIN = 0

    def __init__(self, items):
        self.items = items
        self.default_item_updater = GildedRose.get_coefficient_updater(-1)
        self.rules = {"Aged Brie": GildedRose.get_coefficient_updater(1),
                      "Sulfuras, Hand of Ragnaros": GildedRose.sulfuras_updater,
                      "Backstage passes to a TAFKAL80ETC concert": GildedRose.backstage_passes_updater,
                      "Conjured": GildedRose.get_coefficient_updater(2)
                      }

    def update_quality(self):
        for item in self.items:
            if item.name in self.rules:
                self.rules[item.name](item)
            else:
                self.default_item_updater(item)


    @staticmethod
    def get_coefficient_updater(coefficient):
        def updater(item):
            item.sell_in -= 1
            item.quality = GildedRose.restrict_quality_to_bounds(
                                                        item.quality
                                                        + coefficient
                                                        * (1 + (item.sell_in < 0)))
        return updater

    @staticmethod
    def backstage_passes_updater(item):
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0
        else:
            item.quality = GildedRose.restrict_quality_to_bounds(
                                                        item.quality + 1
                                                        + (item.sell_in < 10)
                                                        + (item.sell_in < 5))

    @staticmethod
    def sulfuras_updater(item):
        pass

    @staticmethod
    def restrict_quality_to_bounds(quality):
        return min(max(GildedRose.QUALITY_MIN, quality), GildedRose.QUALITY_MAX)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
