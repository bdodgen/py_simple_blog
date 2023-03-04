from post import Post


class Blog:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        s_or_blank = 's' if len(self.posts) != 1 else ''
        return f"{self.title}, a blog by {self.author} ({len(self.posts)} post{s_or_blank})"

    def create_post(self, title, content):
        p = Post(title, content)
        self.posts.append(p)

    def json(self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': [post.json() for post in self.posts],
        }
