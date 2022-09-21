from django.test import TestCase

# Create your tests here.
class WatchlistTestCase(TestCase):
    def html_test(self):
        response = self.client.get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)

    def xml_test(self):
        response = self.client.get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

    def json_test(self):
        response = self.client.get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)