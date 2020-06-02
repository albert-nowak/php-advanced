from django.test import TestCase

from example.models import Gift, GiftList
from example.forms import GiftListForm


class GiftListTestCase(TestCase):
    def setUp(self):
        self.gift_list = GiftList.objects.create(name='Christmas presents')
        self.gift = Gift.objects.create(name='RC Car', gift_list=self.gift_list)

    def test_max_length(self):
        gf = GiftListForm(data={'name': 'X' * 100})
        self.assertFalse(gf.is_valid())

    def test_initial(self):
        gf = GiftListForm(instance=self.gift_list)
        self.assertEqual(gf.initial['name'], self.gift_list.name)
