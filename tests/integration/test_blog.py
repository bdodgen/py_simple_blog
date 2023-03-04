from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_post_in_blog(self):
        b = Blog('Test Title', 'Test Author')
        b.create_post('Cool Title', 'Cool Content')

        self.assertEqual(len(b.posts), 1)
        self.assertEqual('Cool Title', b.posts[0].title)
        self.assertEqual('Cool Content', b.posts[0].content)
