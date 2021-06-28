#This is for the variable number of inputs in a function
#def function(asfs, *args = [], **kwargs = [])

blog_1 = 'I am so awesome'
blog_2 = 'Cars are cool'
blog_3 = 'I have got a new computer'
site_title = 'My New BlogPosts'


def blog_posts(title, *args):
	print(title)
	for post in args:
		print(post+ "\n")


blog_posts(site_title,blog_1)
blog_posts(site_title, blog_1,blog_2)
blog_posts(site_title, blog_1,blog_2,blog_3)
#U can actually extend the number of arguments u want 


