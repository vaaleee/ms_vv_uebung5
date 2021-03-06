#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Vorlage
# Uebung 5, Aufgabe 2
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

        accuracy_ = accuracy(classifier, test_set)
   
        refsets = collections.defaultdict(set)
        testsets = collections.defaultdict(set)
 
        for index, (feats, label) in enumerate(test_set):
            refsets[label].add(index)
            observed = classifier.classify(feats)
            testsets[observed].add(index)
 
        male_p = 'male precision: \t {:.3}'.format(precision(refsets['male'], testsets['male']))
        male_r = 'male recall: \t\t {:.3}'.format(recall(refsets['male'], testsets['male']))
        male_F = 'male F-measure: \t {:.3}'.format(f_measure(refsets['male'], testsets['male']))
        female_p = 'female precision: \t {:.3}'.format(precision(refsets['female'], testsets['female']))
        female_r = 'female recall: \t\t {:.3}'.format(recall(refsets['female'], testsets['female']))
        female_F = 'female F-measure: \t {:.3}'.format(f_measure(refsets['female'], testsets['female']))
        accuracy_ = 'accuracy: \t\t {:.3}'.format(accuracy_)

        return '{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(male_p, male_r, male_F, female_p, female_r, female_F, accuracy_)

         


        
    @staticmethod
    def gender_features(name):
        """Return a dictionary with all features to identify the gender of
        a name"""

        feature_dict = {
            #'ends_with_a': True if name.endswith('a') else False,
            
            'long_name': True if len(name) > 9 else False,
            #'ends_with_r': True if name.endswith('r') else False,
            'contains_ll': True if 'll' in name else False,
            #'ends_with_o': True if name.endswith('o') else False,
            #'ends_with_k': True if name.endswith('k') else False,
            #'ends_with_p': True if name.endswith('p') else False,
            'short_name': True if len(name) < 4 else False,
            'contains_a': True if 'a' in name else False,
            #'ends_with_s': True if name.endswith('s') else False,
        }

        if len(name) >0:
            #feature_dict['first_char_2'] = name[0]
            feature_dict['first_char'] = name[0]
            feature_dict['last_char'] = name[-1]

        if len(name) >3:
            feature_dict['last_three'] = name[-3:]
            feature_dict['last_two'] = name[-2:]
            feature_dict['first_two'] = name[:2]
            feature_dict['first_three'] = name[:3]
            feature_dict['ia_in_name'] = True if 'ia' in name else False

        return feature_dict
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

        train_feature_list = []
        test_feature_list = []

        train_dict = {}
        test_dict = {}

        for male_name in male_training_data:
            train_dict[male_name] = 'male'

        for female_name in female_training_data:
            train_dict[female_name] = 'female'

        for name in train_dict.keys():
            train_feature_list.append((self.gender_features(name), train_dict[name]))

        for male_name in male_test_data:
            test_dict[male_name] = 'male'

        for female_name in female_test_data:
            test_dict[female_name] = 'female'

        for name in test_dict:
            test_feature_list.append((self.gender_features(name), test_dict[name]))


        return train_feature_list, test_feature_list
            

        #for male_name in male_training_data:
            #train_feature_list.append((gender_features(male_name), 'male'))
        #for female_name in female_training_data:
            #train_feature_list.append((gender_features(female_name), 'female'))

    
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
        anzahl_maenner = len(male_alles)
        male_test_data = male_alles[:round(anzahl_maenner*0.1)]
        male_train_data = male_alles[round(anzahl_maenner*0.1):]

        
        random.shuffle(female_alles)
        anzahl_frauen = len(female_alles)
        female_test_data = female_alles[:round(anzahl_frauen*0.1)]
        female_train_data = female_alles[round(anzahl_frauen*0.1):]

        return male_train_data, male_test_data, female_train_data, female_test_data



    def main(self):
        male_data = self.extract_data(self.male_file)
        female_data = self.extract_data(self.female_file)



        male_train_data, male_test_data, female_train_data, female_test_data = \
            self.get_train_and_test_data(male_data, female_data)




        # get the training and test set for the classifier and the evaluation
        train_set, test_set = self.get_training_and_test_labeled_features(
            female_train_data, male_train_data, female_test_data,
            male_test_data)


        # create classifier with the training set
        classifier = NaiveBayesClassifier.train(train_set)

        # print the evaluation with the precision, recall and f-measure
        print(self.evaluation(test_set, classifier))
        
        # print the 10 most informative features 
        classifier.show_most_informative_features(15)


if __name__ == '__main__':
    NaiveBayesClassifierNameGenderPrediction('female.txt',
                                             'male.txt')




# http://stackoverflow.com/questions/17412439/how-to-split-data-into-trainset-and-testset-randomly
# http://www.nltk.org/book/ch06.html
