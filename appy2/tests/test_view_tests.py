from django.urls import resolve, reverse
from django.test import TestCase


class FrontPageTests(TestCase):
    def test_view_resolves_url(self):
        url = '/'
        view = resolve(url)
        self.assertEqual(view.view_name, 'appy2:front_page')

    def test_view_gets_success_status_code(self):
        url = reverse('appy2:front_page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        url = reverse('appy2:front_page')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'appy2/front_page.html')

    def test_view_contains_ha(self):
        url = reverse('appy2:front_page')
        response = self.client.get(url)
        self.assertIn('bwahahahahaha', response.content.decode())
