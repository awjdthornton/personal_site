#trying to generate sites, set page title, and set active class all in one step

#bring in the Template string methods
from string import Template

main_pages = [
	{
		"filename": "./content/index.html",
		"output_file": "./docs/index.html",
		"title": "Bio",
		"href": "./index.html",
		"link_label": "Bio",
		"bg_class": "bio",
	},
	{
		"filename": "./content/blog.html",
		"output_file": "./docs/blog.html",
		"title": "Blog",
		"href": "./blog.html",
		"link_label": "Blog",
		"bg_class": "blog",
	},
	{
		"filename": "./content/product_ideas.html",
		"output_file": "./docs/product_ideas.html",
		"title": "Ideas",
		"href": "./product_ideas.html",
		"link_label": "Ideas",
		"bg_class": "product_ideas",
	},
]


def open_template():		
	#open the template and define it as a Template object
	template = open('./templates/template.html').read()
	template = Template(template)
	nav = nav_links()
	template = template.safe_substitute(nav_section=nav)	
	return template
	
def nav_links():
	#create nav links by looping through each page in the main_pages list
	top_links = ''
	for page in main_pages:
		top_links = top_links + '\n' + '''					<li class="nav-item">
						<a class="nav-link" href="'''+ page["href"] + '">' + page["link_label"] + '''</a>
					</li>'''
	return top_links

def create_main_pages (template):
	for page in main_pages:
		#combine template and content, replacing the page specific stuff 
		page_content = open(page["filename"]).read()
		#for some reason you to re-define template as an object of the Template class each time you do a substitution
		page_output = Template(template)
		page_output = page_output.safe_substitute(page, content=page_content)
		#update the nav section to convert the <a> to a <span> for the page itself and to set the active class on that nav item
		page_output = page_output.replace('<a class="nav-link" href="' + page['href'] + '">' + page['link_label'] + '</a>', '<span class="nav-link active" href="' + page['href'] + '">' + page['link_label'] + '</span>')
		open(page["output_file"] , 'w+').write(page_output)


def main():

	print("build.py static site generator - run beginning")
	
	tmpl = open_template()
	create_main_pages(tmpl)

	print("build.py static site generator - run complete")


if __name__ == "__main__":
	main()
