#!/urs/bin/env python3
# -*- coding: utf-8 -*-
# FS17, PCL II, Übung 5
# Aufgabe 2
# Valentina Vogel & Martina Stüssi

"""This module uses a naive bayes classifier to identify the gender of names"""

import random
import collections
from nltk.metrics import *
from nltk.classify import NaiveBayesClassifier, accuracy


class NaiveBayesClassifierNameGenderPrediction:
    """This class implements the naive bayes classification on gender 
    recognition of names"""
    def __init__(self, female_file, male_file):
        self.male_file = male_file
        self.female_file = female_file

        self.main()

    @staticmethod
    def extract_data(data_file):
        """extract the given data file"""
        extracted_file = open(data_file, 'r', encoding='utf-8')
        extracted_file = extracted_file.read()
        return extracted_file

    @staticmethod
    def evaluation(test_set, classifier):
        """Evaluate the classifier with the test set. Print the accuracy,
        precision, recall and f-measure."""
        # TODO: Evaluate the classifier with the test set. Print the
        # overall classifier accuracy, as well as precision, recall and
        # f-measure for male and female
        
    @staticmethod
    def gender_features(name):
        """Return a dictionary with all features to identify the gender of
        a name"""
        return {
            'ends_with_a': True if name.endswith('a') else False,
            'first_char': name[0],
        }
        # TODO: Add further features to maximise the classifier's performance.

    def get_training_and_test_labeled_features(self, female_training_data,
                                               male_training_data,
                                               female_test_data,
                                               male_test_data):
        """return a labeled dictionary of all features for the training
        and test data"""
        # TODO: return two feature, label lists, one for training and one 
        # for testing. Each list should be in the form 
        # [({feature1_name:feature1_value, ...}, label), ...]
    
    @staticmethod
    def get_train_and_test_data(male_data, female_data):
        """Split the male and female data into training and test data."""
        # TODO: Decide on how to split the male and female data into training
        # and test data. Turn the test and training data into lists which
        # contain each name as an element. Return these lists.
        male_alles = []
        for word in male_data.split('\n'):
            male_alles.append(word)

        female_alles = []
        for word in female_data.split('\n'):
            female_alles.append(word)

        random.shuffle(male_alles)
        male_test_data = male_alles[50:]
        male_train_data = male_alles[:50]

        
        random.shuffle(female_alles)

        female_test_data = female_alles[50:]
        female_train_data = female_alles[:50]

        return male_train_data, male_test_data, female_train_data, female_test_data



    def main(self):
        male_data = self.extract_data(self.male_file)
        female_data = self.extract_data(self.female_file)



        male_train_data, male_test_data, female_train_data, female_test_data = \
            self.get_train_and_test_data(male_data, female_data)

        # get the training and test set for the classifier and the evaluation
        """train_set, test_set = self.get_training_and_test_labeled_features(
            female_train_data, male_train_data, female_test_data,
            male_test_data)

        # create classifier with the training set
        classifier = NaiveBayesClassifier.train(train_set)

        # print the evaluation with the precision, recall and f-measure
        self.evaluation(test_set, classifier)
        
        # print the 10 most informative features 
        classifier.show_most_informative_features(1)"""


if __name__ == '__main__':
    NaiveBayesClassifierNameGenderPrediction('female.txt',
                                             'male.txt')




# http://stackoverflow.com/questions/17412439/how-to-split-data-into-trainset-and-testset-randomly
