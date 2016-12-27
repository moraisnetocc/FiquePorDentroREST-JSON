from rest_framework.test import APITestCase


class InfoTest(APITestCase):
    fixtures = ['info']

    def test_info_list(self):
        response = self.client.get('/info/', format='json')

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)

        sample = response.data[0]
        self.assertIn('title', sample)
        self.assertIn('body', sample)
        self.assertEqual(len(sample), 2)
