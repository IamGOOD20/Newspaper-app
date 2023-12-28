from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

class TestHomePage(SimpleTestCase):
    def test_home_status_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200, 'Home page not founded')

    # def test_view_url_by_name(self):
    #     response = self.client.get(reverse('/'))
    #     self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html', 'Template name is not correct')

class SignupPageTests(TestCase):
    username = 'newuser'
    email = 'newuser@email.com'
    def test_signup_page_status_code(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200, 'page not founded')
    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200, 'name "sign up" was not founded')
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html', 'the name of template was not founded')
    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1, 'The count user name =! 1')
        self.assertEqual(get_user_model().objects.all()[0].username, self.username,
                         'The user name not comply with test user name(newuser)')
        self.assertEqual(get_user_model().objects.all()[0].email, self.email,
                         'The user email not comply with test user email(newuser@email.com)')
