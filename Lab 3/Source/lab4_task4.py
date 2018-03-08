from collections import OrderedDict
import csv
import matplotlib.pyplot as plot
from sklearn.cluster import KMeans

i1 = []
s1 = []
def getData(filename):
    with open(filename,'r') as csvdocument:
        csv_File_Content = csv.reader(csvdocument)
        next(csv_File_Content)  # skipping column names
        for row in csv_File_Content:
            i1.append(int(row[3]))
            s1.append(int(row[4]))
    return
getData('StudentDetail.csv')
data = list(zip(i1,s1))
print("Data:")
print(data)

kmeans_data = KMeans(n_clusters=4)
kmeans_data.fit(data)

centroids = kmeans_data.cluster_centers_
labels_data = kmeans_data.labels_
print("Centroids:")
print(centroids)
colors_array = ["m","b","r","y"]
label_array = ["Cluster-1","Cluster-2","Cluster-3","Cluster-3"]

for i1 in range(len(data)):
    print("coordinate:",data[i1], "label_array:", labels_data[i1])
    plot.scatter(data[i1][0], data[i1][1], c = colors_array[labels_data[i1]], label_array = label_array[labels_data[i1]])

plot.scatter(centroids[:, 0],centroids[:, 1], label_array = "Centroids",marker = "x", s1=150, linewidths = 10, zorder = 15)
plot.title('Clusters of Student')
plot.xlabel('SAT Mark')
plot.ylabel('Grade %')
#remove duplicates of labels_data
handles, labels_data = plot.gca().get_legend_handles_labels()
by_label = OrderedDict(zip(labels_data, handles))
plot.legend(by_label.values(), by_label.keys())
plot.show()
#predictions
print("Predicted Class:")
print(kmeans_data.predict([(20,40)]))