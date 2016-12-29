# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def setUp(self):
        self.items = [Item("foo", 0, 0),  # 0
                      Item("inky", 2, 5),  # 1
                      Item("blinky", 0, 5),  # 2
                      Item("pinky", 0, 1),  # 3
                      Item("clyde", 1, 5),  # 4
                      Item("Aged Brie", 1, 5),  # 5
                      Item("Aged Brie", 1, 50),  # 6
                      Item("Sulfuras, Hand of Ragnaros", 4, 5),  # 7
                      Item("Sulfuras, Hand of Ragnaros", 4, 5),  # 8
                      Item("Backstage passes to a TAFKAL80ETC concert", 15, 0), # 9
                      Item("Conjured", 1, 30)]  # 10
        self.gilded_rose = GildedRose(self.items)

    def test_name_consistency(self):
        self.gilded_rose.update_quality()
        self.assertEquals("foo", self.items[0].name)
        self.assertEquals("inky", self.items[1].name)
        self.assertEquals("blinky", self.items[2].name)
        self.assertEquals("pinky", self.items[3].name)
        self.assertEquals("clyde", self.items[4].name)
        self.assertEquals("Aged Brie", self.items[5].name)
        self.assertEquals("Aged Brie", self.items[6].name)
        self.assertEquals("Sulfuras, Hand of Ragnaros", self.items[7].name)
        self.assertEquals("Sulfuras, Hand of Ragnaros", self.items[8].name)
        self.assertEquals("Backstage passes to a TAFKAL80ETC concert", self.items[9].name)
        self.assertEquals("Conjured", self.items[10].name)

    def test_default_item_quality_arc(self):
        self.gilded_rose.update_quality()
        self.assertEquals(4, self.items[1].quality)
        self.gilded_rose.update_quality()
        self.assertEquals(3, self.items[1].quality)
        self.gilded_rose.update_quality()
        self.assertEquals(1, self.items[1].quality)

    def test_quality_positive(self):
        self.gilded_rose.update_quality()
        self.assertEquals(0, self.items[3].quality)

    def test_sell_in_reduction(self):
        self.gilded_rose.update_quality()
        self.assertEquals(0, self.items[4].sell_in)
        self.gilded_rose.update_quality()
        self.assertEquals(-1, self.items[4].sell_in)

    def test_aged_brie_quality_increases(self):
        self.gilded_rose.update_quality()
        self.assertEquals(6, self.items[5].quality)
        self.gilded_rose.update_quality()
        self.assertEquals(8, self.items[5].quality)

    def test_quality_max_50(self):
        self.gilded_rose.update_quality()
        self.assertEquals(50, self.items[6].quality)

    def test_sulfuras_quality_constant(self):
        self.gilded_rose.update_quality()
        self.assertEquals(5, self.items[7].quality)

    def test_sulfuras_sell_in_constant(self):
        self.gilded_rose.update_quality()
        self.assertEquals(4, self.items[8].sell_in)

    def test_backstage_passes_quality_arc(self):
        for i in range(5):
            self.gilded_rose.update_quality()
        self.assertEquals(5, self.items[9].quality)
        for i in range(5):
            self.gilded_rose.update_quality()
        self.assertEquals(15, self.items[9].quality)
        for i in range(5):
            self.gilded_rose.update_quality()
        self.assertEquals(30, self.items[9].quality)

        self.gilded_rose.update_quality()
        self.assertEquals(0, self.items[9].quality)
        self.gilded_rose.update_quality()
        self.assertEquals(0, self.items[9].quality)

    def conjured_quality_arc(self):
        self.gilded_rose.update_quality()
        self.assertEquals(28, self.items[10].quality)
        self.gilded_rose.update_quality()
        self.assertEquals(24, self.items[10].quality)


if __name__ == '__main__':
    unittest.main()
