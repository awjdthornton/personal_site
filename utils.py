#bring in the glob module for looping through files in a directory
import glob

#bring in os module for parsing file paths
import os

#bring in Jinja templating module
from jinja2 import Template

all_html_files = glob.glob("./content/*.html")

pages = []

for file_path in all_html_files:
	file_name = os.path.basename(file_path)
	name_only, extension = os.path.splitext(file_name)
	pages.append({
					'filename': file_path,
					'title': name_only.capitalize(),
					'output_file': './docs/'+file_name,
					'href': file_name,
	})


def open_template():		
	#open the template and define it as a Template object
	template = open('./templates/template.html').read()
	template = Template(template)
	return template

def create_main_pages (template):
	for page in pages:
		#combine template and content, replacing the page specific stuff
		page_content = open(page["filename"]).read()
		final_output = template.render(pages=pages, content=page_content, title=page["title"])
		open(page["output_file"] , 'w+').write(final_output)
		
def new_content():
	new_filename = input('What do you want to name the new file? ')
	open('./content/'+new_filename+'.html', 'w+').write('''<h1>New Content!</h1>
	
	<p>New content...</p>''')
	print('./content/'+new_filename+'.html')

