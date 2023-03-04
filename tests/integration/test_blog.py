from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_post_in_blog(self):
        b = Blog('Test Title', 'Test Author')
        b.create_post('Cool Title', 'Cool Content')

        self.assertEqual(len(b.posts), 1)
        self.assertEqual('Cool Title', b.posts[0].title)
        self.assertEqual('Cool Content', b.posts[0].content)

    def test_json(self):
        b = Blog('Test Title', 'Test Author')
        b2 = Blog('Summer Breeze', 'Makesme Feelfine')
        b.create_post('Cool Title', 'Cool Content')
        b2.create_post('This', 'This Content')
        b2.create_post('That', 'That Content')
        expected_b = {'title': 'Test Title',
                      'author': 'Test Author',
                      'posts': [{'title': 'Cool Title',
                                 'content': 'Cool Content'
                                 }]}
        expected_b2 = {'title': 'Summer Breeze',
                       'author': 'Makesme Feelfine',
                       'posts': [{'title': 'This', 'content': 'This Content'},
                                 {'title': 'That', 'content': 'That Content'}]}

        self.assertDictEqual(expected_b, b.json())
        self.assertDictEqual(expected_b2, b2.json())

    def test_json_no_posts(self):
        b = Blog('Test Title', 'Test Author')

        expected_b = {'title': 'Test Title', 'author': 'Test Author', 'posts': []}

        self.assertDictEqual(expected_b, b.json())
