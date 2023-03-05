from blog import Blog


MENU_PROMPT = 'Enter "c" to create a new blog, ' \
              '"l" to list blogs, ' \
              '"r" to read one, ' \
              '"p" to create a new post, ' \
              'or "q" to quit'
POST_TEMPLATE = '''
    --- {} ---
    
    {}
    
    '''

blogs = dict()      # blog_name : Blog object


def ask_create_blog():
    # asks for title and author and creates new blog, adds to blogs list
    title = input("Enter the new blog's title: ")
    author = input("Enter the new blog's author: ")

    blogs[title] = Blog(title, author)


def ask_create_post():
    blog_key = input("Enter the title of the blog to add a post to: ")
    blog = blogs[blog_key]
    post_title = input("Enter the new post's title: ")
    post_content = input("Enter the new post's content: ")

    blog.create_post(post_title, post_content)


def ask_read_blog():
    # asks for the blog title and prints out posts from that blog
    blog_key = input("Enter the title of the blog to read: ")

    print_posts(blogs[blog_key])


def menu():
    pass
    # show user available blogs
    print_blogs()
    # allow user to make a choice
    selection = input(MENU_PROMPT)
    # do something with that choice
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)

    # eventually exit


def print_blogs():
    # print the available blogs
    for key, blog in blogs.items():
        print(f"- {blog}")


def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))


def print_posts(blog):
    for post in blog.posts:
        print_post(post)
