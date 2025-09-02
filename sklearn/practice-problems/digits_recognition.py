from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC 
from sklearn.decomposition import PCA
# classify handwritten digits with > 97% accuracy
digits = load_digits()
x_train,x_test,y_train,y_test = train_test_split(digits.data,digits.target,test_size=0.2,random_state=42)
# PCA for dimensionality reduction
pca = PCA(n_components=50)
x_train_pca = pca.fit_transform(x_train)
x_test_pca = pca.transform(x_test)

model = SVC(kernel='rbf',random_state=42)
model.fit(x_train_pca,y_train)
accuracy = model.score(x_test_pca,y_test)

print(f"Digits Recognition Accuracy : {accuracy:.3f}")