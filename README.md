# Language Recognition Model
This repository contains a language recognition model that can identify the language of a given text. The model uses word n-grams and CountVectorizer to transform the text data into numerical features, and it employs three different classifiers to perform the language detection:

## Features

- **CountVectorizer**: Converts a collection of text documents to a matrix of token counts.
- **Word n-grams**: Uses n-grams (contiguous sequences of n items from a given sample of text) for feature extraction. The n-grams can capture patterns and structures in the text that are specific to different languages.
- **Multiple Classifiers**: Trains three different classifiers to recognize languages:
  - **Naive Bayes**: A probabilistic classifier based on applying Bayes' theorem with strong (naive) independence assumptions.
  - **Logistic Regression**: A statistical model that in its basic form uses a logistic function to model a binary dependent variable.
  - **Random Forest**: An ensemble learning method that constructs multiple decision trees during training and outputs the class that is the mode of the classes of the individual trees.

## Evaluation

The models were evaluated on a dataset consisting of six languages: English, Finnish, German, Italian, Polish, and Spanish. The evaluation metrics are as follows:

### Naive Bayes

| Language | Precision | Recall | F1-Score | Support |
|----------|-----------|--------|----------|---------|
| English  | 1.00      | 1.00   | 1.00     | 200     |
| Finnish  | 1.00      | 1.00   | 1.00     | 200     |
| German   | 1.00      | 1.00   | 1.00     | 200     |
| Italian  | 1.00      | 1.00   | 1.00     | 200     |
| Polish   | 1.00      | 0.99   | 1.00     | 200     |
| Spanish  | 1.00      | 1.00   | 1.00     | 200     |
| **Accuracy** |        |        | **1.00** | 1200    |
| **Macro avg** | 1.00 | 1.00   | 1.00     | 1200    |
| **Weighted avg** | 1.00 | 1.00 | 1.00     | 1200    |

### Logistic Regression

| Language | Precision | Recall | F1-Score | Support |
|----------|-----------|--------|----------|---------|
| English  | 1.00      | 1.00   | 1.00     | 200     |
| Finnish  | 1.00      | 1.00   | 1.00     | 200     |
| German   | 1.00      | 1.00   | 1.00     | 200     |
| Italian  | 1.00      | 1.00   | 1.00     | 200     |
| Polish   | 1.00      | 1.00   | 1.00     | 200     |
| Spanish  | 1.00      | 1.00   | 1.00     | 200     |
| **Accuracy** |        |        | **1.00** | 1200    |
| **Macro avg** | 1.00 | 1.00   | 1.00     | 1200    |
| **Weighted avg** | 1.00 | 1.00 | 1.00     | 1200    |

### Random Forest

| Language | Precision | Recall | F1-Score | Support |
|----------|-----------|--------|----------|---------|
| English  | 1.00      | 1.00   | 1.00     | 200     |
| Finnish  | 1.00      | 1.00   | 1.00     | 200     |
| German   | 1.00      | 1.00   | 1.00     | 200     |
| Italian  | 1.00      | 1.00   | 1.00     | 200     |
| Polish   | 1.00      | 1.00   | 1.00     | 200     |
| Spanish  | 1.00      | 1.00   | 1.00     | 200     |
| **Accuracy** |        |        | **1.00** | 1200    |
| **Macro avg** | 1.00 | 1.00   | 1.00     | 1200    |
| **Weighted avg** | 1.00 | 1.00 | 1.00     | 1200    |
