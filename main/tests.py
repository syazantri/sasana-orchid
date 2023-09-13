from django.test import TestCase
from main.models import Item

class MainAppTestCase(TestCase):
    def test_name(self): #test apakah nama sudah sesuai
        response = self.client.get("/main/")
        self.assertContains(response, "Syazantri Salsabila")
        self.assertContains(response, "PBP D")
        self.assertContains(response, "main")

    def test_created_item(self): #test apakah fungsi pembuatan item pada views sudah berjalan dengan benar
        Item.objects.create(name="test", amount=2, price=3000, description='hi')

        anggrek = Item.objects.get(name="test")
        self.assertEqual(anggrek.name, "test")
        self.assertEqual(anggrek.amount, 2)
        self.assertEqual(anggrek.price, 3000)
        self.assertEqual(anggrek.description, "hi")