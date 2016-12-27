from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Info, InfoCategory


class InfoTest(APITestCase):
    fixtures = ['infos', 'info_categories']

    def test_info_list(self):
        response = self.client.get('/api/infos/', format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

        sample = response.data[0]
        self.assertIn('title', sample)
        self.assertIn('body', sample)
        self.assertIn('category', sample)
        self.assertEqual(len(sample), 3)

    def test_info_creation(self):
        post_data = {
            'title': 'Some weird title',
            'body': 'Some weird body',
            'category': InfoCategory.objects.values_list('id', flat=True).first(),
        }

        info_queryset = Info.objects.filter(**post_data)
        info_count = info_queryset.count()

        response = self.client.post('/api/infos/', post_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        object_created = response.data
        self.assertEqual(post_data['title'], object_created['title'])
        self.assertEqual(post_data['body'], object_created['body'])
        self.assertEqual(post_data['category'], object_created['category'])
        self.assertEqual(len(object_created), 3)

        self.assertEqual(info_count + 1, info_queryset.count())


class InfoCategoryTest(APITestCase):
    fixtures = ['infos', 'info_categories']

    def test_info_list(self):
        response = self.client.get('/api/info_categories/', format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

        for category in response.data:
            self.assertIn('name', category)
            self.assertIn('infos', category)
            self.assertEqual(len(category), 2)

            try:
                info_sample = category['infos'][0]
            except IndexError:
                continue

            self.assertIn('title', info_sample)
            self.assertIn('body', info_sample)
            self.assertEqual(len(info_sample), 2)

            break
