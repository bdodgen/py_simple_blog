import builtins
from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog
from post import Post


class AppTest(TestCase):
    def setUp(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Author')
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get('Test'))

    def test_ask_create_post(self):
        blog = app.blogs['Test']

        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Title', 'Test Content')

            app.ask_create_post()

            self.assertEqual(blog.posts[0].title, 'Test Title')
            self.assertEqual(blog.posts[0].content, 'Test Content')

    def test_ask_read_blog(self):
        blog = app.blogs['Test']

        with patch('builtins.input', return_value='Test'):
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()

                mocked_print_posts.assert_called_with(blog)

    def test_menu_calls_create_blog(self):
        with patch('app.ask_create_blog') as mocked_ask_create_blog:
            with patch('builtins.input') as mocked_input:
                mocked_input.side_effect = ('c', 'Blog Title', 'Author', 'q')
                app.menu()
                mocked_ask_create_blog.assert_called()

    def test_menu_calls_ask_create_post(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_create_post') as mocked_ask_create_post:
                mocked_input.side_effect = ('p', 'Test', 'Post Title', 'Post Content', 'q')
                app.menu()
                mocked_ask_create_post.assert_called()

    def test_menu_calls_ask_read_blog(self):
        with patch('app.ask_read_blog') as mocked_ask_read_blog:
            with patch('builtins.input') as mocked_input:
                mocked_input.side_effect = ('r', 'Test', 'q')
                app.menu()
                mocked_ask_read_blog.assert_called()

    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_menu_calls_print_blogs_from_selection(self):
       with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input') as mocked_input:
                mocked_input.side_effect = ('l', 'q')
                app.menu()
                mocked_print_blogs.assert_called()

    def test_menu_prints_prompt(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('l', 'q')
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test, a blog by Test Author (0 posts)')

    def test_print_post(self):
        post = Post('Post Title', 'Post Content')
        expected_print = '''
    --- Post Title ---
    
    Post Content
    
    '''

        with patch('builtins.print') as mocked_print:
            app.print_post(post)
            mocked_print.assert_called_with(expected_print)

    def test_print_posts(self):
        blog = app.blogs['Test']
        post = Post('Post Title', 'Post Content')
        blog.posts = [post]

        with patch('app.print_post') as mocked_print_post:
            app.print_posts(blog)

            mocked_print_post.assert_called_with(blog.posts[0])
