print("beginning build.py")
top = open('./templates/top.html').read()
bottom = open('./templates/bottom.html').read()

index = open('./content/index.html').read()
open('./docs/index.html' , 'w+').write(top + index + bottom)

blog = open('./content/blog.html').read()
open('./docs/blog.html' , 'w+').write(top + blog + bottom)

product_ideas = open('./content/product_ideas.html').read()
open('./docs/product_ideas.html' , 'w+').write(top + product_ideas + bottom)

print("build.py complete")
