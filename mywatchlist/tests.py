from django.test import TestCase, Client

# Create your tests here.
class WatchlistTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.html = "/mywatchlist/html/"
        self.xml = "/mywatchlist/xml/"
        self.json = "/mywatchlist/json/"

    def test_html(self):
        response = self.client.get(self.html)
        self.assertEqual(response.status_code, 200)

    def test_xml(self):
        response = self.client.get(self.xml)
        self.assertEqual(response.status_code, 200)

    def test_json(self):
        response = self.client.get(self.json)
        self.assertEqual(response.status_code, 200)