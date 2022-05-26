from flask import Flask, request, render_template
import fasttext
import pickle

app = Flask(__name__)
clf = pickle.load(open('rf_50_65_50.sav', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    feature_list = request.form.to_dict()
    feature_list = list(feature_list.values())
    print(feature_list)
    model = fasttext.load_model(
        "./ubertext.fiction_news_wikipedia.filter_rus+short.tokens.txt.algo-cbow.epochs-15.subwords-2..5.neg_sampling-15.bin")
    vectors = model.get_sentence_vector(feature_list[0])

    prediction = clf.predict(vectors.reshape(1, -1))
    output = int(prediction[0])
    if output == 1:
        text = "propaganda"
    else:
        text = "not propaganda"

    return render_template('index.html', prediction_text='The news is {}'.format(text))


if __name__ == "__main__":
    app.run(debug=True)