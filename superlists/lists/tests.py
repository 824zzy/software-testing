from django.test import TestCase

from django.urls import resolve
from .views import homePage
from django.http import HttpRequest
from django.template.loader import render_to_string

class SmokeTest(TestCase):
    def test_bad_math(self):
        # 
        # self.assertEqual(1+1, 3)
        self.assertEqual(1+1, 2)

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self): 
        found = resolve('/') 
        self.assertEqual(found.func, homePage)

    def test_home_page_returns_correct_html(self):
        # # a bit of unwieldy way of testing that we use the right template
        # request = HttpRequest()
        # response = homePage(request)
        # html = response.content.decode('utf8')
        # expected_html = render_to_string('home.html')
        # self.assertEqual(html, expected_html)

        response = self.client.get('/')
        html = response.content.decode('utf8')

        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        # print(repr(html))
        # print(repr(html.strip()))
        self.assertTrue(html.endswith('</html>'))

        self.assertTemplateUsed(response, 'home.html')