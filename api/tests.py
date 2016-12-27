from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Info


class InfoTest(APITestCase):
    fixtures = ['info']

    def test_info_list(self):
        response = self.client.get('/info/', format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

        sample = response.data[0]
        self.assertIn('title', sample)
        self.assertIn('body', sample)
        self.assertEqual(len(sample), 2)

    def test_info_creation(self):
        post_data = {
            'title': 'Some weird title',
            'body': 'Some weird body'
        }

        info_queryset = Info.objects.filter(**post_data)
        info_count = info_queryset.count()

        response = self.client.post('/info/', post_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        object_created = response.data
        self.assertEqual(post_data['title'], object_created['title'])
        self.assertIn(post_data['body'], object_created['body'])
        self.assertEqual(len(object_created), 2)

        self.assertEqual(info_count + 1, info_queryset.count())
