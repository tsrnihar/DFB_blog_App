from django.test import Client,TestCase
from django.contrib.auth import get_user_model
from .models import BlogPost
from django.urls import reverse

# Create your tests here.

class BlogTests(TestCase,Client):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
        username = "testuser",
        email = "test@email.com",
        password = "test password"
        )

        self.blog = BlogPost.objects.create(
            title = "Testing",
            author = self.user,
            content = "test content"
        )

    def test_title_string_rep(self):
        blog = BlogPost(title = "chumma")
        self.assertEqual(str(blog),"chumma")

    def test_detail_user(self):
        response = self.client.get('/blog/1/')
        self.assertEqual(response.status_code,200)

    def test_list(self):
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response, 'test content')
        self.assertContains(response, 'Testing')
        self.assertTemplateUsed(response, 'detail.html')


