# coding: utf-8
import os
import numpy
from collections import Counter
from sklearn.naive_bayes import GaussianNB

def word_counter(open_file):
	word_list = []
	content = open_file.readlines()
	for i in range(len(content)):
		for word in content[i].split():
			if word in dangerous_words:
				word_list.append(word.lower())
	count = Counter(dangerous_words)
	for i in count:
		count[i] = 0
	count.update(word_list)
	return count


os.chdir('C:\\Users\Emanuela\Documents\\UNI\IntroAI\\NaiveBayes')

dangerous_words = ['click', 'here', 'link', 'cheap', 'buy', 'free', 'viagra',
				'win', 'cash', 'credit', 'debit', 'card', 'deposit', 'investment',
				'easy', 'lose', 'weight', 'interest', 'payment', 'money', 'offer',
				'dollars', 'earnings', 'income', 'junk', 'spam', 'deal', 'financial',
				'prize', 'casino', 'play', 'extra', 'webcam', 'sexy', 'naked',
				'secrets', 'easy', 'diet', 'winner', 'rich', '$', 'share']

train = []
target = []
for f in os.listdir('.\\train'):
	open_file = open('.\\train\\' + f, 'r', newline='\n', encoding="utf-8")
	spam = open_file.readline().strip()
	if spam == 'FALSE':
		target.append(1)
	elif spam == 'TRUE':
		target.append(2)
	else:
		print('Error: could not classify')
	word_count = word_counter(open_file)
	open_file.close()
	train.append(numpy.array(list(word_count.values())))


gnb = GaussianNB()
gnb.fit(train, target)
for f in os.listdir('.\\test'):
	open_file = open('.\\test\\' + f, 'r', newline='\n', encoding="utf-8")
	spam = open_file.readline().strip()
	word_count = word_counter(open_file)
	open_file.close()
	pred = gnb.predict([ numpy.array(list(word_count.values())) ])
	print(spam, pred, end=': ')
	if spam == 'TRUE' and pred == [2]:
		print('SPAM WAS CORRECTLY CLASSIFIED')
	elif spam == 'FALSE' and pred == [1]:
		print('HAM WAS CORRECTLY CLASSIFIED')
	elif spam == 'TRUE' and pred == [1]:
		print('SPAM WAS ERRONEOUSLY CLASSIFIED AS HAM')
	elif spam == 'FALSE' and pred == [2]:
		print('HAM WAS ERRONEOUSLY CLASSIFIED AS SPAM')
