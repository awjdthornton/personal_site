#trying to generate sites, set page title, and set active class all in one step

def main():
#bring in the Template string methods
	from string import Template

	print("build.py static site generator - run beginning")
	
	pages = [
		{
			"filename": "./content/index.html",
			"output_file": "./docs/index.html",
			"title": "About Me",
			"active": "active_bio",
			"bg_class": "bio",
		},
		{
			"filename": "./content/blog.html",
			"output_file": "./docs/blog.html",
			"title": "Blog",
			"active": "active_blog",
			"bg_class": "blog",
		},
		{
			"filename": "./content/product_ideas.html",
			"output_file": "./docs/product_ideas.html",
			"title": "Ideas",
			"active": "active_product_ideas",
			"bg_class": "product_ideas",
		},
	]				
			

	#open the template and define it as a Template object
	template = open('./templates/template.html').read()
	template = Template(template)

	#combine template and content, replacing the page specific stuff 
	index_content = open('./content/index.html').read()
	index_page = template.safe_substitute(title="About Me", active_bio="active", content=index_content, bg_class="bio")
	open('./docs/index.html' , 'w+').write(index_page)

	blog_content = open('./content/blog.html').read()
	blog_page = template.safe_substitute(title="Blog", active_blog="active", content=blog_content, bg_class="blog")
	open('./docs/blog.html' , 'w+').write(blog_page)

	product_ideas_content = open('./content/product_ideas.html').read()
	product_ideas_page = template.safe_substitute(title="Ideas", active_product_ideas="active", content=product_ideas_content, bg_class="product_ideas")
	open('./docs/product_ideas.html' , 'w+').write(product_ideas_page)

	print("build.py static site generator - run complete")


if __name__ == "__main__":
	main()
