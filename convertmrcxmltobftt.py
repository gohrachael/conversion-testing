# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 15:37:42 2019

@author: #GOHRACHAEL#
"""

import lxml.etree
import os
import rdflib

marc2bibframe2 = lxml.etree.XSLT(lxml.etree.parse("D:/#GOHRACHAEL#/Documents/marc2bibframe2/xsl/marc2bibframe2.xsl"))
dl = os.listdir('F:/Test/Test/turtle')                                                  

#content = open('13061157.xml', 'rb')
#parsing = lxml.etree.parse(content)
#
#with open("new.rdf", "x") as new:
#    new.write(txt)
                
#content = open(lxml.etree.parse('12225465.xml'), 'rb')
#bibframe2 = marc2bibframe2(content)

extensions = ('.xml')                

for f in dl:
    ext = os.path.splitext(f)[-1].lower()
    if ext in extensions:
        with open(f, 'r', encoding="utf-8") as content:
            parsing = lxml.etree.parse(content)
            bibframe2 = marc2bibframe2(parsing)
            txt = str(bibframe2)
            bf_rdf = rdflib.Graph()
            bf_rdf.parse(data=txt, format='xml')
            turtle = bf_rdf.serialize(format='turtle').decode()
        with open("{}.rdf".format(f), "x", encoding="utf-8") as new:
            new.write(turtle)


#for rdf in dl:
#    ext = os.path.splitext(rdf)[-1].lower()
#    if ext == ".xml":
#        bf_rdf = rdflib.Graph()
#        bf_rdf.parse(data=rdf, format='xml')
#        bf_rdf.serialize(format='turtle').decode()
          
                                                  
                                                  