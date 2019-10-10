from collections import defaultdict, Counter
import math, random, re, glob

documents = ["data science", "big data", "science fiction"]


def tokenize(message):
	message = message.lower()  # convert to lowercase
	all_words = re.findall("[a-z0-9']+", message)  # extract the words
	return set(all_words)  # remove duplicates


def word_count_old(documents):
	"""word count not using MapReduce"""
	return Counter(word
				   for document in documents
				   for word in tokenize(document))


def wc_mapper(document):
	"""for each word in the document, emit (word,1)"""
	for word in tokenize(document):
		yield (word, 1)


def wc_reducer(word, counts):
	"""sum up the counts for a word"""
	yield (word, sum(counts))

def word_count(documents):
	"""count the words in the input documents using MapReduce"""

	# place to store grouped values
	collector = defaultdict(list)

	for document in documents:
		for word, count in wc_mapper(document):
			collector[word].append(count)

	return [output
			for word, counts in collector.items()
			for output in wc_reducer(word, counts)]


def map_reduce(inputs, mapper, reducer):
    """runs MapReduce on the inputs using mapper and reducer"""
    collector = defaultdict(list)

    for input in inputs:
        for key, value in mapper(input):
            collector[key].append(value)

    return [output
            for key, values in collector.items()
            for output in reducer(key,values)]


print(word_count_old(documents))
