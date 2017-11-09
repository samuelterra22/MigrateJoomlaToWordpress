# http://python-wordpress-xmlrpc.readthedocs.io/en/latest/overview.html

from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo

wp = Client('http://localhost/corrego/xmlrpc.php', 'admin', 'admin')
wp.call(GetPosts())

user_info = wp.call(GetUserInfo())

print(user_info)

post = WordPressPost()
post.title = 'My new title'
post.content = 'This is the body of my new post.'
post.terms_names = {
    'post_tag': ['test', 'firstpost'],
    'category': ['Introductions', 'Tests']
}
# wp.call(NewPost(post))
