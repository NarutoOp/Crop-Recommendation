def pre(a,b):
	import pandas as pd
	from sklearn import preprocessing
	from sklearn.model_selection import train_test_split
	from sklearn.tree import DecisionTreeClassifier
	from sklearn.linear_model import LinearRegression
	from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
	 
	data=pd.read_csv("cropdata.csv",index_col=0)
	le = preprocessing.LabelEncoder()
	x1=data["State"]
	y1=data["Soil"]
	z1=data["Month"]
	x = le.fit_transform(x1)
	y = le.fit_transform(y1)
	z = le.fit_transform(z1)
	data1 = data.merge(pd.DataFrame({'State_C':x,'Soil_C':y,'Month_C':z}),right_index=True, left_index=True)
	X = data1[['State_C','Soil_C','Month_C']]
	Y = data1['Rice']
	X_train,X_test,Y_train,Y_test =train_test_split(X,Y, random_state = 0)
	classifier = DecisionTreeClassifier()
	classifier.fit(X_train,Y_train)
	c = classifier.predict([[a,b,'3']])
	final_str = 'City : %s'%(c)

	#EXIT
	return final_str
