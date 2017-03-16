import os
from collections import Counter
from sklearn.naive_bayes import GaussianNB

os.chdir('c:\\Users\Massimo\Desktop\Temp\EmaNaiveBayes')

dangerous_words = ["click", "here", "the", "and"]

train_set = []
target = []
for f in os.listdir(".\TrainingSet"):
	open_file = open(".\TrainingSet\\"+f, 'r', newline='\n')
	spam = open_file.readline()
	words_list =[]
	contents = open_file.readlines()
	for i in range(len(contents)):
		for word in contents[i].split():
			if word in dangerous_words:
				words_list.append(word.lower())
	open_file.close()
	count = Counter({'click': 0, 'here': 0, 'the': 0, 'and': 0})
	count.update(words_list)
	train_set.append(np.array(list(count.values())))
	if spam == "YES":
		target.append(2)
	else:
		target.append(1)

#dummy file
train_set.append(np.array([3,4,1,2]))
target.append(2)

gnb = GaussianNB()
gnb.fit(train_set, target)
print(gnb.predict([[3, 4, 2, 5]]))

