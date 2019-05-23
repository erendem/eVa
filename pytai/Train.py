import nltk
from nltk.tokenize import word_tokenize
import numpy as np
class Train:
    def __init__(self, dataset,all_words2):
        self.dataset=dataset
        self.all_words = all_words2
        self.classifier=None  
        data = self.dataset
        data = np.array(data)
        Y=data[:,1]
        X=data[:,0]
    def fit(self):
       # t = [({word: (word in word_tokenize(x[0])) for word in self.all_words}, x[1]) for x in self.dataset]
        self.classifier = nltk.DecisionTreeClassifier.train(self.dataset)
    def fit2(self):
    
        #t = [({word: (word in word_tokenize(x[0])) for word in self.all_words}, x[1]) for x in self.dataset]
        self.classifier = nltk.NaiveBayesClassifier.train(self.dataset)
        #self.classifier.show_most_informative_features(15)
    
    def predict(self,sentence):
        test_sentence = sentence.lower()
        test_sent_features = {word: (word in word_tokenize(test_sentence.lower())) for word in self.all_words}
        return self.classifier.classify(test_sent_features)
    def accuracy(self,testdata):
        return nltk.classify.accuracy(self.classifier,testdata)