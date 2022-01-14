from django.test import SimpleTestCase
from django.urls import reverse


class HomepageTest(SimpleTestCase):

    def setUp(self):
        url = reverse('stage')
        self.response = self.client.get(url)

    def test_home_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):

        self.assertTemplateUsed(self.response, 'stage.html')
    
    def test_homepage_contains_correct_html(self):

        self.assertContains(self.response, 'Stage')
    
    def test_homepage_does_not_contain_incorrect_html(self):

        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')
