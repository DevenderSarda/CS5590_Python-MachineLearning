import numpy as np
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn import metrics

wine_data = datasets.load_wine()
x_data = wine_data.data[:,:2]
y_data = wine_data.target

z=0.3
xaxis_min, xaxis_max = x_data[:, 0].min() - 1, x_data[:, 0].max() + 1
yaxis_min, yaxis_max = x_data[:, 1].min() - 1, x_data[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(xaxis_min, xaxis_max, z),
                     np.arange(yaxis_min, yaxis_max, z))

x_train,x_test,y_train,y_test=train_test_split(x_data,y_data,test_size=0.2)
train_model = svm.SVC()

predictions_linear = train_model.set_params(kernel='linear').fit(x_train, y_train).predict(x_test)

predictions_rbf = train_model.set_params(kernel='rbf').fit(x_train, y_train).predict(x_test)

accuracy_linear = metrics.accuracy_score(y_test,predictions_linear)
accuracy_rbf = metrics.accuracy_score(y_test,predictions_rbf)

print("Accuracy using kernel=linear-",accuracy_linear)
print("Accuracy using kernel=rbf-",accuracy_rbf)