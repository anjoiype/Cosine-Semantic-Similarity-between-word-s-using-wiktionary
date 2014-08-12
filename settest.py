import nltk
from nltk.corpus import stopwords
import string
from collections import Counter
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import urllib
import re

u_reg=[]
first_noun=[]
v_reg=[]
second_noun=[]


a=raw_input("Enter the first word:\t")
url_a="http://en.wiktionary.org/w/index.php?action=raw&title="+a
b=raw_input("Enter the second word:\t")
url_b="http://en.wiktionary.org/w/index.php?action=raw&title="+b


f1=urllib.urlopen(url_a)
s1=f1.read()
f2=urllib.urlopen(url_b)
s2=f2.read()


regex_1=re.compile("{{en-noun.*?(?:(?:\n\n{{)|===)|{{en-proper\snoun.*?(?:(?:\n\n{{)|===)",re.DOTALL)
first_set=regex_1.findall(s1)


first_noun=first_set[0]


regex_2 = re.compile("(?:#\s(?:[A-Z]|\[\[)(?:(?:\s\[)|(?:\s[a-z])|(?:\s|[a-z])).*?\n)|(?:#\s{{countable.*?\n)|(?:#\s{{trademark.*?\n)|(?:#\s{{uncountable.*?\n)|(?:#\s{{botany.*?\n)|(?:#\s{{context\|music.*?\n)|(?:#\s{{geometry.*?\n)|(?:#\s{{US\|Canada.*?<)|",re.DOTALL)
first_subset=regex_2.findall(first_noun)

regexp_remvbkt=re.compile("{{.*?}}|#|\[\[|\]\]")
for item in first_subset:
	first_text=regexp_remvbkt.sub('',item)
   	u_reg.append(first_text)


#========================for v=========================================


second_set=regex_1.findall(s2)


second_noun=second_set[0]



second_subset=regex_2.findall(second_noun)


for item in second_subset:
	second_text=regexp_remvbkt.sub('',item)
   	v_reg.append(second_text)

w=[]
s_u=[]
s_v=[]
lemma_u=[]
lemma_v=[]
u_unique=[]
v_unique=[]
tfu_list=[]
tfv_list=[]
u_lower=[]
v_lower=[]
u_list=[]
joinstr_u=''
joinstr_v=''
#u_reg=[]

for item in u_reg:
	u_lower.append(item.lower())
	#print u_reg
for item in v_reg:
	v_lower.append(item.lower())


u_punc = [''.join(c for c in s if c not in string.punctuation) for s in u_lower]

#' '.join(string.strip() for string in u_punc)
for word in u_punc:
	joinstr_u=joinstr_u+word
print "\n\n"
print "Defenition of %s" %a
print "----------------------------------------------"
print "\n"
print joinstr_u



#' '.join(string.strip() for string in v_lower)
v_punc = [''.join(c for c in s if c not in string.punctuation) for s in v_lower]
for word in v_punc:
	joinstr_v=joinstr_v+word
print "\n\n"
print "Defenition of %s" %b
print "----------------------------------------------"
print "\n"

print joinstr_v





u_s= PorterStemmer()
v_s = PorterStemmer()
u_lemma = WordNetLemmatizer()
v_lemma = WordNetLemmatizer()



u_list=nltk.word_tokenize(joinstr_u)
	

v_list=nltk.word_tokenize(joinstr_v)
	


u_list = [word for word in u_list if word not in stopwords.words('english')] 
v_list = [word for word in v_list if word not in stopwords.words('english')] 




for items in u_list:
	lemma_u.append(u_lemma.lemmatize(items))
for items in v_list:
	lemma_v.append(v_lemma.lemmatize(items))


#print lemma_u
#print lemma_v

for item in lemma_u:
        if item not in u_unique:
            u_unique.append(item)
for item in lemma_v:
        if item not in v_unique:
            v_unique.append(item)
for item in (u_unique+v_unique):
	if item not in w:
		w.append(item)





frequ=Counter(lemma_u)
freqv=Counter(lemma_v)



for word in w:	
	tfu=float(frequ[word])/len(lemma_u)
	tfu_list.append(tfu)
	tfv=float(freqv[word])/len(lemma_v)
	tfv_list.append(tfv)

sum=0
squre_a=0
squre_b=0
for i in range(len(tfu_list)):
	sum=sum+(tfu_list[i]*tfv_list[i])

for i in range(len(tfu_list)):
	squre_a=squre_a+(tfu_list[i]*tfu_list[i])
	squre_b=squre_b+(tfv_list[i]*tfv_list[i])

alpha=sum/(((squre_a)**.5)*((squre_b)**.5))
print alpha
	


	
	

