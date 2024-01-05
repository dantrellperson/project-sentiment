# project sentiment

**My goal is to create an effective sentiment analysis data product that will discover latent aspects in review data using the LARAM model**

_-Sentiment analysis is the practice of using algorithms to classify various samples of related text into overall positive and negative categories._


# exploring different areas of text analytics.
_Looking to learn more about text analytics. My overall goal is to train an accurate sentiment analyzer_


*Amazon Customer Reviews with Sentiment
- https://www.kaggle.com/datasets/thedevastator/amazon-customer-reviews-with-2013-2019-sentiment

## methods I'm exploring 

### * Bag of Words method
> - taking each word from a sentence to get some kind of measure by which we can find out if the word exists in another sentence or not and also its importance
> - each sentence in the google reviews will be treated as a bag of words, in other words each sentence is a **document** and all the documents make up a **corpus**

#### goals
1. create a dictionary of all the unique words in the corpus (exclusding words like "the", "an", "is" etc)
1. convert all documents into vectors which will represent the presence of words from our dictionary in the documents.
* *We're going to do this with the Tf-idf vectorizer in sklearn*

#### steps
1. Count the number of times each word appears in each document(hotel review)
    1. create feature vector and find out of how many zeroes are in my feature vector.
    1. calculate the non-zero value density in the vector
    1. remove stopwords and non-english characters
    1. test stemming or lemmatization