import matplotlib.pyplot as plot

from sklearn import datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

iris = datasets.load_iris()

data = iris.data
target = iris.target
input_data = iris.target_names

from sklearn.model_selection import train_test_split
X_training_Data, X_testing_Data, y_training_Data, y_testing_Data = train_test_split(data, target, test_size=0.732)

from sklearn.neighbors import KNeighborsClassifier
classifier_input = KNeighborsClassifier(n_neighbors=5)
classifier_input.fit(X_training_Data, y_training_Data)

y_predictor = classifier_input.predict(X_testing_Data)


lda_data = LinearDiscriminantAnalysis(n_components=2)
X_r2 = lda_data.fit(X_testing_Data, y_predictor).transform(data)

plot.figure()
colors_array = ['red', 'green', 'blue']
lw = 2


for color, i, target_name in zip(colors_array, [0, 1, 2], input_data):
    plot.scatter(X_r2[target == i, 0], X_r2[target == i, 1], alpha=.8, color=color,
                label=target_name)
plot.legend(loc='best', shadow=False, scatterpoints=1)
plot.title('Prediction Model of IRIS Data using LDA')

plot.show()