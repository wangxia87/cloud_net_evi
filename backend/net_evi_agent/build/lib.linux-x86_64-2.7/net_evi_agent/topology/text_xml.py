#!/usr/bin/python
import xml.etree.ElementTree as ET
try:
	print "!!!!"
       	xmlstr=""
        #f=open("test.xml","r")
        #tree=ET.ElementTree(file='test.xml')
        tree=ET.parse('test.xml')
        print tree
        root=tree.getroot()
        print root
        xmlstr=ET.tostring(root,encoding='utf-8', method='xml')
except:
        print "there is some errors parsing with the xml file"
finally:
        print xmlstr

