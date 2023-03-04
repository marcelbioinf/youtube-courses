import tensorflow as td
from tensorflow import keras
import numpy as np

data = keras.datasets.imdb

(train_data, train_labels), (test_data, test_labels) = data.load_data(num_words=88000)


word_index = data.get_word_index()

word_index = {k:(v+3) for k, v in word_index.items()}
word_index["<PAD>"] = 0
word_index["<START>"] = 1
word_index["<UNK>"] = 2
word_index["<UNUSED>"] = 3

reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])


def decode_review(text):
	return " ".join([reverse_word_index.get(i, "?") for i in text])


train_data = keras.preprocessing.sequence.pad_sequences(train_data, value=word_index["<PAD>"], padding="post", maxlen=250)
test_data = keras.preprocessing.sequence.pad_sequences(test_data, value=word_index["<PAD>"], padding="post", maxlen=250)


# model = keras.Sequential()
# model.add(keras.layers.Embedding(88000, 16))  #tworzy wektory dla wszystkich słów - word factros i grupuje je na podstawie wzajemnego podobieństwa.Wekotry maja 16 koordynatów - 16D
# model.add(keras.layers.GlobalAveragePooling1D()) #it somehow lowers the dimension so its easier to compute, then data is passed to input layer
# model.add(keras.layers.Dense(16, activation="relu")) #our input layer is 16 neurons now
# model.add(keras.layers.Dense(1, activation="sigmoid"))#our ouput layer is one neuron that has a value 0 or 1
# #our model takes the vectors that correspond to different words such as 'good' and 'great' and 'bad' then preprocess these data and gives it to input layer so in the end we can determine whether its a positive or negative imdb review
#
# model.summary()  # prints a summary of the model
#
# model.compile(optimizer="adam", loss='binary_crossentropy', metrics=['accuracy'])
#
# val_data = train_data[:10000] #train data is split in 2 sets and one of them i validation data which will be used as efficiency measure that we tunes and tweaks we do at testing data
# train_data = train_data[10000:]
#
# val_labels = train_labels[:10000]
# train_labels = train_labels[10000:]
#
# fitModel = model.fit(train_data, train_labels, epochs=15, batch_size=512, validation_data=(val_data, val_labels), verbose=1)
#
# results = model.evaluate(test_data, test_labels)
#
# print(results)

#model.save("model_neural1.h5")

def review_encode(s):
    encoded = [1]  #START
    for word in s:
        if word.lower() in word_index:
            encoded.append(word_index[word.lower()])
        else:
            encoded.append(2)  #UNK
    return encoded

model = keras.models.load_model("model_neural1.h5")

with open("./test.txt", encoding='utf-8') as f:
    for line in f.readlines():
        nline = line.replace(',', '').replace('.', '').replace('(', '').replace(')', '').replace(':', '').replace('\"', '').strip().split(" ")  #line1 = re.sub('[^a-zA-Z]', ' ', line).strip().split(' ')
        encode = review_encode(nline)
        encode = keras.preprocessing.sequence.pad_sequences([encode], value=word_index["<PAD>"], padding="post", maxlen=250)
        predict = model.predict(encode)
        print(line)
        print(encode)
        print(predict[0])
