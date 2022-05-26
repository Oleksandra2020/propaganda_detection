from flask import Flask, request, render_template
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
    # model = tf.load_model(
    #     "./model.ckpt.data-00000-of-00001")
    # vectors = model.get_sentence_vector(feature_list[0])

    # prediction = clf.predict(vectors.reshape(1, -1))
    # output = int(prediction[0])
    output = 1
    if output == 1:
        text = "propaganda"
    else:
        text = "not propaganda"

    return render_template('index.html', prediction_text='The news is {}'.format(text))


if __name__ == "__main__":
    app.run(debug=True)