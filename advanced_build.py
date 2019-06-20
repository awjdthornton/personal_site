#trying to generate sites, set page title, and set active class all in one step

#bring in the Template string methods
from string import Template

print("beginning advanced_build.py")

#open the advanced template and define it as a Template class
template = open('./templates/advanced_template.html').read()
template = Template(template)

#combine template and content, replacing the page specific stuff in the template portion
index_content = open('./content/index.html').read()
index_page = template.safe_substitute(title="About Me", active="active", content=index_content, bg_class="bio")
open('./docs/index.html' , 'w+').write(index_page)

#blog_content = open('./content/blog.html').read()
#open('./docs/blog.html' , 'w+').write(top + blog + bottom)

#product_ideas_content = open('./content/product_ideas.html').read()
#open('./docs/product_ideas.html' , 'w+').write(top + product_ideas + bottom)

print("advanced_build.py complete")
