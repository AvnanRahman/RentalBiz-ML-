from flask import Flask, request, render_template, jsonify
import pickle
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

model = pickle.load(open('model_tf.pkl', 'rb'))
X_train = pickle.load(open("X_train.pkl", "rb"))
# word_index = pickle.load(open("word_index.pkl", "rb"))
app = Flask(
    __name__, template_folder=r"C:\Users\Achmad Shiddiqi\Belajar_ML\capstone_model")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/result', methods=['POST'])
def result():
    barang = [request.form.get('nama_produk')]
    tokenizer = Tokenizer(oov_token="<OOV>")
    tokenizer.fit_on_texts(X_train)
    tokenizer.word_index
    sequences = tokenizer.texts_to_sequences(barang)
    padded = pad_sequences(sequences, maxlen=21,
                           padding='post', truncating='post')
    result = model.predict(padded)
    if result.argmax() == [0]:
        result = "Dapur"
    elif result.argmax() == [1]:
        result = "Kafe"
    elif result.argmax() == [2]:
        result = "Hobi"
    elif result.argmax() == [3]:
        result = "Elektronik"
    elif result.argmax() == [4]:
        result = "Travel"
    elif result.argmax() == [5]:
        result = "Baju"
    elif result.argmax() == [6]:
        result = "Musik"
    elif result.argmax() == [7]:
        result = "Transportasi"
    elif result.argmax() == [8]:
        result = "Kamera"
    return render_template("result.html", result=result)


if __name__ == '__main__':
    app.run(debug=True)