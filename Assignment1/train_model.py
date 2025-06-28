import joblib
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.naive_bayes import MultinomialNB

def data_load(file_path):
    df = pd.read_csv(file_path)
    print(df.info())
    print(df.head(3))
    return df

def split_XY(dataset):
    X = dataset.review
    y = dataset.sentiment.map({'positive': 1, 'negative': 0})
    return X,y

def create_pipeline(X,y):
    model = Pipeline([ 
           ('tfidf', TfidfVectorizer()),
           ('clf', MultinomialNB())
           ])
    model.fit(X, y)
    joblib.dump(model, 'sentiment_model.pkl')
    print("Pretrained weight is saved.")

def main():
    file_path = './IMDB_Dataset.csv'
    movie_reviews = data_load(file_path)
    X,y = split_XY(movie_reviews)
    create_pipeline(X,y)

if __name__ == '__main__':
    main()