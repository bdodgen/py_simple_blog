from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test Title', 'Test Author')

        self.assertEqual('Test Title', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test Title', 'Test Author')
        b2 = Blog('Summer Breeze', 'Makesme Feelfine')
        expected_b = "Test Title, a blog by Test Author (0 posts)"
        expected_b2 = "Summer Breeze, a blog by Makesme Feelfine (0 posts)"

        self.assertEqual(expected_b, b.__repr__())
        self.assertEqual(expected_b2, b2.__repr__())

    def test_repr_multiple_posts(self):
        b2 = Blog('Summer Breeze', 'Makesme Feelfine')
        b2.posts = ['Cool Post']
        b3 = Blog('Why I Did It', 'The Butler')
        b3.posts = ['He Had It Coming', 'He Only Had Himself to Blame']

        expected_b2 = "Summer Breeze, a blog by Makesme Feelfine (1 post)"
        expected_b3 = "Why I Did It, a blog by The Butler (2 posts)"

        self.assertEqual(expected_b2, b2.__repr__())
        self.assertEqual(expected_b3, b3.__repr__())
