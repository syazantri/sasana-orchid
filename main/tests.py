from django.test import TestCase

class MainAppTestCase(TestCase):
    def test_name(self): #test apakah nama sudah sesuai
        response = self.client.get("/main/")
        self.assertContains(response, "Syazantri Salsabila")
        self.assertContains(response, "PBP D")
        self.assertContains(response, "main")