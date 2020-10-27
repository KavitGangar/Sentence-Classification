# Sentence-Classification
Classifying if a sentence is a question or an answer using different predictive models

Datasets used: 
https://rajpurkar.github.io/SQuAD-explorer/ (SQuAD)

http://martinweisser.org/index.html#Amex_a (SPAADIA)

Combined size of records: 0.24million(after cleaning)

Feature Engineering techniques used:

Bag-of-words model using Term frequency
Bag-of-words model using TF-IDF
Word Embeddings using GloVe
Language modelling with BERT


Predictive Models used: 

Naive Bayes

Random Forest

Support Vector Machine(SVM)

Deep Learning Model(CNN)

Combination of different feature engineering techniques and predictive models are used to compare the accuracy, training time and model size.

Models(to compare model size): https://drive.google.com/drive/folders/150-grlaCHK46xrsqrl-XAA7BHKnarXyJ?usp=sharing

Training time:

Naive Bayes: 2 seconds

Random Forest: 5 seconds

SVM: 5-7minutes

CNN: 5-7minutes(5 epochs)

BERT: 1 hour 8minutes

