from quickdraw import QuickDrawDataGroup
import os

# categories to be downloaded -> can be found in categories.txt
categories = ["apple","ice cream","police car","lightning","octopus"]
# number of samples for each category
n_samples = 100

for category in categories:
    qdg = QuickDrawDataGroup(category,max_drawings=n_samples)

    if not os.path.exists(category):
        os.makedirs(category)

    for x,drawing in enumerate(qdg.drawings):
        drawing.image.save(category + "/" + category +"_"+ str(x) +".png")

