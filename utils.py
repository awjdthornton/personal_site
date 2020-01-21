#bring in the glob module for looping through files in a directory
import glob

#bring in os module for parsing file paths
import os

#bring in Jinja templating module
from jinja2 import Template

#bring in markdown to convert to html
import markdown
md = markdown.Markdown(extensions=["markdown.extensions.meta"])

all_md_files = glob.glob("./content/*.md")

# sorting by file name which will impact how the links will be sorted. Ideally this should be less arbitrary
all_md_files.sort()

pages = []

for file_path in all_md_files:
	file_name = os.path.basename(file_path)
	name_only, extension = os.path.splitext(file_name)
	pages.append({
					'filename': file_path,
					'title': name_only.capitalize(),
					'output_file': './docs/'+name_only+'.html',
					'href': name_only+'.html',
	})

def open_template():		
	#open the template and define it as a Template object
	template = open('./templates/template.html').read()
	template = Template(template)
	return template

def create_main_pages (template):
	for page in pages:
		print('Generating ->',page)
		#combine template and content, replacing the page specific stuff
		page_content = open(page["filename"]).read()
		#converting from markdown to html
		page_content = md.convert(page_content)
		#bringing in markdown variables
		title = md.Meta['title'][0]
		bground = md.Meta['background'][0]
		#creating final output
		final_output = template.render(
									title=title,
									bground=bground,
									pages=pages,
									content=page_content,
									)
		open(page["output_file"] , 'w+').write(final_output)
		
def new_content():
	new_filename = input('What do you want to name the new file? ')
	open('./content/'+new_filename+'.md', 'w+').write(
'''title: sample_title
author: sample_author
background: sample_bg

<div class="content bg-light row rounded left_border">>
	
	<p>New content...</p>

</div>'''
)
	print('./content/'+new_filename+'.md')
	
def invalid_arg():
	print('''Invalid argument
Usage:
	Rebuild site: python manage.py build
	Create new page: python manage.py new
	''')

