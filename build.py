#trying to generate sites, set page title, and set active class all in one step

def main():
#bring in the Template string methods
	from string import Template

	print("build.py static site generator - run beginning")
	
	pages = [
		{
			"filename": "./content/index.html",
			"output_file": "./docs/index.html",
			"title": "Bio",
			"active_bio": "active",
			"bg_class": "bio",
		},
		{
			"filename": "./content/blog.html",
			"output_file": "./docs/blog.html",
			"title": "Blog",
			"active_blog": "active",
			"bg_class": "blog",
		},
		{
			"filename": "./content/product_ideas.html",
			"output_file": "./docs/product_ideas.html",
			"title": "Ideas",
			"active_product_ideas": "active",
			"bg_class": "product_ideas",
		},
	]				
			
	#open the template and define it as a Template object
	template = open('./templates/template.html').read()
	template = Template(template)
					
	for page in pages:
		#combine template and content, replacing the page specific stuff 
		page_content = open(page["filename"]).read()
		page_output = template.safe_substitute(page, content=page_content)
		open(page["output_file"] , 'w+').write(page_output)

	print("build.py static site generator - run complete")


if __name__ == "__main__":
	main()
