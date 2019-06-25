#trying to generate sites, set page title, and set active class all in one step

#bring in the Template string methods
from string import Template

print("beginning build.py")

#open the advanced template and define it as a Template class
template = open('./templates/template.html').read()
template = Template(template)

#combine template and content, replacing the page specific stuff in the template portion
index_content = open('./content/index.html').read()
index_page = template.safe_substitute(title="About Me", active_bio="active", content=index_content, bg_class="bio")
open('./docs/index.html' , 'w+').write(index_page)

blog_content = open('./content/blog.html').read()
blog_page = template.safe_substitute(title="Blog", active_blog="active", content=blog_content, bg_class="blog")
open('./docs/blog.html' , 'w+').write(blog_page)

product_ideas_content = open('./content/product_ideas.html').read()
product_ideas_page = template.safe_substitute(title="Ideas", active_product_ideas="active", content=product_ideas_content, bg_class="product_ideas")
open('./docs/product_ideas.html' , 'w+').write(product_ideas_page)

print("build.py complete")
