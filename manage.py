#Static site generation script

#bring in utils.py which has necessary functions for site building
import utils

#bring in system functionality
import sys

def main():
	print("manage.py static site generator - run started")
	if len(sys.argv) == 1:
		print('''Usage:
		Rebuild site: python manage.py build
		Create new page: python manage.py new_content
		''')
	else:
		command = sys.argv[1]
		if command == 'build':
			tmpl = utils.open_template()
			utils.create_main_pages(tmpl)
		elif command == 'new':
			utils.new_content()
		else:
			print('''Usage:
			Rebuild site: python manage.py build
			Create new page: python manage.py new_content
			''')
	print("manage.py static site generator - run complete")


if __name__ == "__main__":
	main()


