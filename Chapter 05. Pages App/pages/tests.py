from django.test import SimpleTestCase
from django.urls import reverse, resolve  # new
from .views import HomePageView  # new

# Create your tests here.
class HomepageTests(SimpleTestCase):
    def setUp(self):   
        url = reverse("home")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, "home.html")

    def test_homepage_contains_correct_html(self):  
        self.assertContains(self.response, "home page")

    def test_homepage_does_not_contain_incorrect_html(self): 
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_home_url_resolves_homepageview(self):  # new
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)