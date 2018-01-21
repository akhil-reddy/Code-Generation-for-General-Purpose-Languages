import sys #Command Line Arguments
import re #RegeX
from nltk.corpus import stopwords #NLP
from gensim.models import word2vec #word2vec
import logging #logging of progress of model creation
import time #Time delay
from subprocess import call
from nltk.tag.stanford import StanfordPOSTagger as POS_Tag
import csv

class_matching_threshold = 0.70

classes = [['search','find','locate'],['arrange','sort'],['iterate','loop over']]
classnames = ['search','sort','iterate']
function_mappings = {'search':'re.search','sort':'sorted'}
'''
cb = wordnet.synset('cookbook')
ib = wordnet.synset('instruction_book')
cb.wup_similarity(ib)
'''

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
        
def findKW(word):
	for i in range(len(classes)):
		Class = classes[i]
		for classMember in Class:
			if(word==classMember):
				return i
	return 0
def StanfordParser(words):
	# Stanford Parser
	# Download the entire package from: http://nlp.stanford.edu/software/stanford-postagger-full-2014-08-27.zip
	# Set the paths to model and the .jar file
	# Use this to separate parameters and functions
	_path_to_model = '/Users/Reddy/Desktop/Research/stanford-postagger-full-2017-06-09/models/english-bidirectional-distsim.tagger' 
	_path_to_jar = '/Users/Reddy/Desktop/Research/stanford-postagger-full-2017-06-09/stanford-postagger-3.8.0.jar'
	st = POS_Tag(_path_to_model, _path_to_jar)
	print(st.tag(words.split()))
"""
def buildCommand(keyword,data):
	parameters = describeBuiltin(keyword)
	finalCommand = analyseData(data, parameters)
	print(finalCommand)
	#eval(finalCommand)



def describeBuiltin(keyword):
	if(keyword=='sort'):
		return ['sorted','iterable','[key]','[reverse]']
		# Issue #2, Not really a issue, just have to do this manual work of returning appropriate lists. I'll do it, no worries.
	# Just like this, we have to write an if condition for every built-in function we focus on
		# I'll complete this if you give me a list of all functions.
		# These are the functions I have: 
		# List of most popular constructs
		'''
		constructs = {"print":"print(*objects, sep=’ ‘, end=’\\n’, file=sys.stdout, flush=False)",
		"len":"len(object)",
		"sort":"sort(*, key=None, reverse=False)",
		"ascending":"sort(*, key=None, reverse=False)",
		"descending":"sort(*, key=None, reverse=False)",
		"sorted":"sorted(iterable, *, key=None, reverse=False)",
		"range":"range(start, stop[, step])",
		"xrange":"xrange(start, stop[, step])",
		"split":"string.split([sep[, maxsplit]])",
		"lstrip":"string.lstrip(s[, chars])",
		"rstrip":"string.rstrip(s[, chars])",
		"strip":"string.strip(s[, chars])",
		"str":"str(object=”)",
		"str":"str(object=”)",
		"string":"str(object=”)",
		"type":"class type(object)",
		"type":"class type(name, bases, dict)",
		"map":"map(function, iterable, …)",
		"enum":"enumerate(sequence, start=0)",
		"enumerate":"enumerate(sequence, start=0)",
		"count":"list.count(x)",
		"index":"list.index(x)",
		"position":"list.index(x)",
		"find":"string.find(s, sub[, start[, end]])",
		"list":"list([iterable])",
		"map":"map(function, iterable, …)",
		"lambda":"lambda arguments: expression",
		"file":"file(name[, mode[, buffering]])",
		"input":"input([prompt])",
		"dictionary":"class dict(**kwarg)",
		"dictionary":"class dict(mapping, **kwarg)",
		"dictionary":"class dict(iterable, **kwarg)",
		"open":"open(name[, mode[, buffering]])",
		"file":"open(name[, mode[, buffering]])",
		"reduce":"reduce(function, iterable[, initializer])",
		"reverse":"reversed(seq)",
		"slice":"class slice(stop)",
		"slice":"class slice(start, stop[, step])",
		"zip":"zip([iterable, …])"}
		'''

def analyseData(data,parameters):
	# 'analyses' data and assigns a tag to each member of data and returns the final command
	# Eg - If the string is 'sort my_list', my_list is given the tag 'iterable'
	# Issue #3, How do we figure out the parameters' tags. Do you have a fix for this (in your NLP engine)? Or do we have to figure out a way?
	# Use the StanfordParser Function, and find a pattern the parameters occur in. I've noticed that parameters typically get the tag "CD" (Cardinal Number), "VBG" (Verb, gerund or present participle), or occasionally "NN" (Named Nouns).
	# You can try examples on the Stanford Parser here: http://nlp.stanford.edu:8080/parser/index.jsp
	StanfordParser(original_words)
	for index in range(len(parameters)-1):
		if(parameters[index+1].startswith('[')):
			pass
			# Optional parameters
		else:
			pass
			# Required parameters
	return("Hello World")
"""
indent=0
def model(tokens):
	functional = []
	data = []
	# Search for 'functional' keyword
	Class = []
	for word in tokens:
		ret = findKW(word)
		if(ret):
			functional.append(word)
			Class.append(classnames[ret])
		else:
			data.append(word)

	'''for word_index in range(0, len(tokens)):
		if(tokens[word_index]):
	'''
	# Data Sentences: Create and Fill
	for word_index in range(0, len(tokens)):
		if(tokens[word_index]== "end"):
			indent-=1
		if(tokens[word_index]== "define"):
			final_string=indent*"\t"+""
			for i in range(0, len(tokens)):
				if(tokens[i]=='function' or tokens[i]=='method'):
					break
			final_string+='def '+tokens[i+1]
			if(tokens[i+2]!='parameters'|tokens[i+2]!='parameter'|tokens[i+2]!='arguments'|tokens[i+2]!='argument'):
			# if 'arguments'/'parameters' is at the end of sentence, use the previous x tokens as parameters
				i+=1
				final_string+='('
				while(tokens[i]!='arguments'|tokens[i]!='argument'|tokens[i]!='parameter'|tokens[i]=='parameters'):
					final_string+=tokens[i]+','
				final_string=final_string[:-1]
				final_string+='):\n'
			# or else, do the below
			else:
				for i in range(0, len(tokens)):
					if(tokens[i]=='parameter'|tokens[i]=='argument'):
						final_string+='('+tokens[i+1]+'):\n'
						break
					if(tokens[i]=='parameters'|tokens[i]=='arguments'):
						#Till the end of sentence, use the tokens as parameters. 
						j=i
						while(tokens[j]!='.'):#Akash, Take care of this. # Put a stopper (such as . or ,) to indicate where to stop 
							final_string+=tokens[i]+','
						final_string=final_string[:-1]
						final_string+='):\n'
						break
			indent+=1
		elif(tokens[word_index]== "generate"):
			final_string = indent*"\t"+""
			variable_name = ""
			for i in range(0, len(tokens)):
				if(re.match("[A-Za-z][A-Za-z][A-Za-z][A-Za-z]*\.", tokens[i])):
					variable_name = tokens[i]

			variable_name = variable_name[0:-1]
			if(tokens[len(tokens)-2] == "store"):
				final_string = variable_name + ' = []\n'
			if(re.match(r'[0-9][0-9]?[0-9]?', tokens[word_index+1])):
				final_string = indent*"\t"+final_string + "for i in range(0, " + str(tokens[word_index+1]) + "):\n"
			if(tokens[word_index+2]=='random'):
				if(tokens[word_index+3]=='integers' or tokens[word_index+3]=='integers'):
					final_string =indent*"\t"+ final_string + '\t'+variable_name+'.append(int(random.randint(1,' + str(tokens[word_index+1]) + ')))'
				else:
					final_string =indent*"\t"+ final_string + '\t'+variable_name+'.append(random.randint(1,' + str(tokens[word_index+1]) + '))'
			print(final_string)

		elif(tokens[word_index]== "import"):
			final_string = indent*"\t"+"import "
			'''if(tokens[word_index+3] == "store" ):
				final_string += str(tokens[len(tokens) - 1]) + " = []\n"
			for icsv in range(0, len(file_list)):
				if(re.match(r'[A-Za-z0-9]*.csv$', file_list[icsv])):
					final_string += "with open('"+file_list[icsv] + "', ‘rb’) as f:\n"
					final_string += "\treader = csv.reader(f)\n"
					final_string += "\tfor row in reader:\n"
					break
			if(tokens[word_index+3] == "print" or tokens[word_index+3] == "display"):
				final_string += "\t\tprint(row)"
			if(tokens[word_index+3] == "store" ):
				final_string += "\t\t"+str(tokens[len(tokens)-1])+".append(row)"
			'''
			i=0
			for i in range(0,len(tokens)):
				if(tokens[i]=='package' or tokens[i]=='module' or tokens[i]=='library'):
					break
			final_string+=tokens[word_index+1]
			if(i-word_index>2):
				for j in range(2,i-1-word_index):
					final_string+=','+tokens[word_index+j]
			final_string+=' from '+tokens[i-1]
			print(final_string)


		elif(tokens[word_index]== "create"):
			if(tokens[word_index+1] == "dictionary"):
				if(tokens[word_index+2]):
					print(indent*"\t",tokens[word_index+2]," = {}")
				else:
					print(indent*"\t","temp = {}")
			elif(tokens[word_index+1] == "list"):
				if(tokens[word_index+2]):
					print(indent*"\t",tokens[word_index+2]," = []")
				else:
					print(indent*"\t","temp = []")
			
		# Issue: Need to find parameter/[^\\]*\s
		elif(tokens[word_index] == "fill" or tokens[word_index] == "populate"):
			if(tokens[word_index+1] == "dictionary"):
				if(tokens[word_index+2]!='values'):
					final_string=indent*"\t"+tokens[word_index+2]+' = {'
				else:
					final_string=indent*"\t"+'temp = {'
				for index in range(0,len(tokens)):
					if(tokens[index]=='values' or tokens[index]=='value'):
						index+=1
						break
				for i in range(index,len(tokens),2):
					if(is_number(tokens[i])):
						final_string+=tokens[i]+":'"+tokens[i+1]+"',"
					else:
						final_string+="'"+tokens[i]+"':'"+tokens[i+1]+"',"
				final_string=final_string[:-1]
				final_string+='}'
				print(final_string)
			elif(tokens[word_index+1] == "list"):
				if(tokens[word_index+2]!='values'):
					final_string=indent*"\t"+tokens[word_index+2]+' = ['
				else:
					final_string=indent*"\t"+'temp = ['
				for index in range(0,len(tokens)):
					if(tokens[index]=='values'):
						index+=1
						break
				for i in range(index,len(tokens)):
					final_string+="'"+tokens[i]+"',"
				final_string=final_string[:-1]
				final_string+=']'
				print(final_string)

		# ADD 'range'

	# Operation Sentences:
	for word_index in range(0, len(tokens)):
		# Issue: Need to find parameters
		if(tokens[word_index]== "sort"):
			final_string=indent*"\t"+tokens[word_index+1]+'=sort('+tokens[word_index+1]
			for index in range(0,len(tokens)):
				if(tokens[index]=='descending'):
					final_string+=',reverse=True'
					break
			final_string+=')'
			print(final_string)
		elif(tokens[word_index]== "search"):
			final_string=indent*"\t"+'for i in '+tokens[word_index+2]
			final_string+=':\n'+indent*"\t"+'\tif(i=='+tokens[word_index+1]+'):\n'+indent*"\t"+'\t\t'
			final_string+='print("found")\n'
			print(final_string)
			'''
			digit_regex = re.compile('[0-9]+$')
			if(digit_regex.match(tokens[word_index+1])): # || digit_regex.match(tokens[word_index+1])):
				search_element = int(tokens[word_index+1])
				print("Must iterate over A, and find ", search_element)
			else: 
				print("Can't find search element")
			'''
		# Issue: How do we handle a textual description of the element to be searched
		# We could do it for say: negative, or 'over, above, under, below <value>'
		#Split
		elif(tokens[word_index]== "split"):
			for index in range(word_index+1,len(tokens)):
				if(tokens[index]=="seperator"):
					break
			seperator=tokens[index+1]
			split_element = tokens[word_index+1]
			print(indent*"\t",split_element,'.split(',seperator,')')
		#Strip
		elif(tokens[word_index]== "strip"):
			strip_element = tokens[word_index+1]
			final_string = indent*"\t"+tokens[len(tokens)-1]
			for index in range(0,len(tokens)):
				if(tokens[index]=="left"):
					final_string+='.l'
					break
				if(tokens[index]=="right"):
					final_string+='.r'
					break
			final_string+='strip('+strip_element+')'
			print(final_string)
		#Type
		elif(tokens[word_index]== "type"):
			final_string=indent*"\t"+'type('+tokens[word_index+1]+')'
			print(final_string)
		#Apply
		elif(tokens[word_index]== "apply"):
			for index in range(0,len(tokens)):
				if(tokens[index]=="function"):
					break
			final_string=indent*"\t"+'map('+tokens[index+1]+tokens[index+2]
			print(final_string)
		#Input
		elif(tokens[word_index]== "accept" or tokens[word_index]== "take"):
			final_string=indent*"\t"+''
			for index in range(0,len(tokens)):
				if(tokens[index]=='integer'):
					final_string='temp = int(input())'
				elif(tokens[index]=='decimal'):
					final_string='temp = double(input())'
				elif(tokens[index]=='array'):
					final_string='temp = list(input())'
				else:
					final_string='temp = (input())'
			print(final_string)
		#Open
		elif(tokens[word_index]== "open"):
			for index in range(0,len(tokens)):
				if(tokens[index]=='file'):
					break
			final_string = indent*"\t"+"tempfptr=open('"+tokens[index+1]+"')"
			print(final_string)
		elif(tokens[word_index] == 'number' and tokens[word_index+1] == 'elements'):
			print(indent*"\t","len(",tokens[word_index+2],")")
		elif(tokens[word_index] == 'number' and tokens[word_index+1] == 'keys'):
			print(indent*"\t","len(",tokens[word_index+2],".keys())")
	'''		
	# Fill-in the respective arguments for that method 
	for fkw in Class:
		buildCommand(fkw, data)
	if not Class:
		pass
		# Issue #1, what to do when we can't find a class. He did tell we have to make a new class but on what basis?
		# We don't have a predefined class. Handle this
		# I'm still working on this.
	'''
# Length of Command Line Arguments
length_of_arguments = len(sys.argv)
# Only when text contains 2 or more words.
word_list=''
file_list = []
query = []
if(length_of_arguments > 3):
    word_list = str(sys.argv[1:length_of_arguments])
else:
    print("Please enter a valid Problem Statement.")

original_words = word_list
# Tokenize ONLY WORDS
file_list = re.findall("[A-Za-z]*\.csv", word_list)
word_list = re.findall("\w+\.|\w+|d+", word_list)
# Remove stop words
filtered_words = [word for word in word_list if word not in stopwords.words('english')]
# Convert to lowercase if it is not a name
filtered_words = [word.lower() for word in filtered_words if len(word)>1]


model(filtered_words,0)
print("\n")