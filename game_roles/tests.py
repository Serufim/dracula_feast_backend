from django.test import TestCase
from django.contrib.auth.models import User
from .models import GameRole


class GameRoleTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user_1 = User.objects.create_user(username='testuser1', password='abcd123')
        test_user_1.save()

        test_role = GameRole.objects.create(
            name='Дракула', descriptions='Кусает за жопу', image='image/url.jpg'
        )
        test_role.save()

    def test_role_content(self):
        role = GameRole.objects.get(pk=1)
        expected_name = f'{role.name}'
        expected_description = f'{role.descriptions}'
        expected_image = f'{role.image}'
        self.assertEqual(expected_name, 'Дракула')
        self.assertEqual(expected_description, 'Кусает за жопу')
        self.assertEqual(expected_image, 'image/url.jpg')
