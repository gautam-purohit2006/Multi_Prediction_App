import pickle

# Load Model
with open("saved_pkl/spam_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load Vectorizer
with open("saved_pkl/tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)


def predict_spam(message):

    # Convert text into TF-IDF Features
    message_feature = vectorizer.transform([message])

    # Predict
    prediction = model.predict(message_feature)

    return prediction[0]
