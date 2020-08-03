from Graph.getGraph import getGraph
from PIL import Image
#deaths, confirmed, recovered, critical
def getAllGraph():
    for key in ['confirmed', 'deaths']:
        getGraph(key)
        im = Image.open('./Graph/'+key+'.png')
        #im = im.crop((left, top, right, bottom))
        im = im.crop((300, 700, 1200, 1250))
        #im.show()
        im.save('./Graph/'+key+'.png')


