echo "starting build.sh"
cat ./templates/top.html ./content/index.html ./templates/bottom.html > ./docs/index.html
cat ./templates/top.html ./content/blog.html ./templates/bottom.html > ./docs/blog.html
cat ./templates/top.html ./content/product_ideas.html ./templates/bottom.html > ./docs/product_ideas.html
echo "finished build.sh"
