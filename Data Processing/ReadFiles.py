import json
#file = open('C:\\Users\\kavit gangar\\Documents\\SPAADIA\\SQuAd\\train_v2.json','r',encoding='UTF-8')
file = open('C:\\Users\\kavit gangar\\Documents\\SPAADIA\\SQuAd\\train-v2.0.json','r',encoding='UTF-8')
ques = open('C:\\Users\\kavit gangar\\Documents\\SPAADIA\\SQuAd\\q.txt','w',encoding='UTF-8')
ans = open('C:\\Users\\kavit gangar\\Documents\\SPAADIA\\SQuAd\\a.txt','w', encoding='UTF-8')


with file as f :
	data=json.load(f)
	
	#print (data['data'])
	for r in data['data'] :
		for q in r['paragraphs'] :
			for p in q['qas'] :
				ques.write(str(p['question']) + "\n")
				if(len(p['answers'])==0):
					for s in p['plausible_answers'] :
						ans.write(str(s['text']) + "\n")
				else :
					for s in p['answers'] :
						ans.write(str(s['text']) + "\n")
