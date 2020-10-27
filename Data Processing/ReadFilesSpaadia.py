import os
import xml.dom.minidom
dir = 'C:\\Users\\kavit gangar\\Documents\\SPAADIA\\spaadia_release_v01'
ques = open('C:\\Users\\kavit gangar\\Documents\\SPAADIA\\SQuAd\\q.txt','a',encoding='UTF-8')
ans = open('C:\\Users\\kavit gangar\\Documents\\SPAADIA\\SQuAd\\a.txt','a', encoding='UTF-8')

for file in os.listdir(dir) :
	try :
		doc=xml.dom.minidom.parse(dir + "/" + file)
		tmp=doc.getElementsByTagName("q-wh")
		for s in tmp:
			ques.write(s.firstChild.nodeValue[1:])
		tmp=doc.getElementsByTagName("q-yn")
		for s in tmp:
			ques.write(s.firstChild.nodeValue[1:])
	except:
		continue
ques.close()

for file in os.listdir(dir) :
	try :
		doc=xml.dom.minidom.parse(dir + "/" + file)
		tmp=doc.getElementsByTagName("decl")
		for s in tmp:
			ans.write(s.firstChild.nodeValue[1:])
		tmp=doc.getElementsByTagName("imp")
		for s in tmp:
			ans.write(s.firstChild.nodeValue[1:])
	except:
		continue
ans.close()
