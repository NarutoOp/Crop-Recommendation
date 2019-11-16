def pre(a,b):
	import pandas as pd
	import matplotlib.pyplot as plt
	from sklearn.tree import DecisionTreeClassifier
	from sklearn import preprocessing
	from sklearn.linear_model import LinearRegression
	basic=pd.read_csv('location_Avail.csv')
	le = preprocessing.LabelEncoder()
	x1 = basic["SOIL"]
	y1 = basic["STATE"]
	x = le.fit_transform(x1)
	y = le.fit_transform(y1)

	location = a
	soil = b

	basic1 = basic.merge(pd.DataFrame({'SOIL_C':x,'STATE_C':y}),right_index=True,left_index = True)
	ordinary=basic1.query('STATE == @location and SOIL == @soil')
	Z = ordinary[['STATE_C','SOIL_C']].values

	X = basic1[['STATE_C','SOIL_C']]
	Y = basic1[['Rice','Cotton','Sugarcane','Wheat','Millets','Cardamom','Ginger','Coconut']]	
	classifier = DecisionTreeClassifier()
	classifier.fit(X,Y)	
	c = classifier.predict(Z)
	d = cropname(c,a)
	if len(d)==1:
		final_str = '%s : \nCurrent Year Yield : %s \nCurrent Year Profit : %s \nCurrent Year Cost : %s\n' %(str(d[0][0]),d[0][1],d[0][2],d[0][3])
		return final_str
	elif len(d) == 2:
		final_str = '%s : \nCurrent Year Yield : %s \nCurrent Year Profit : %s \nCurrent Year Cost : %s\n%s : \nCurrent Year Yield : %s \nCurrent Year Profit : %s \nCurrent Year Cost : %s\n' %(str(d[0][0]),d[0][1],d[0][2],d[0][3],str(d[1][0]),d[1][1],d[1][2],d[1][3])
		return final_str
	elif len(d)==3:
		final_str = '%s : \nCurrent Year Yield : %s \nCurrent Year Profit : %s \nCurrent Year Cost : %s\n%s : \nCurrent Year Yield : %s \nCurrent Year Profit : %s \nCurrent Year Cost : %s\n%s : \nCurrent Year Yield : %s \nCurrent Year Profit : %s \nCurrent Year Cost : %s\n' %(str(d[0][0]),d[0][1],d[0][2],d[0][3],str(d[1][0]),d[1][1],d[1][2],d[1][3],str(d[2][0]),d[2][1],d[2][2],d[2][3])
		return final_str
	else:
		final_str = 'No crops available with this match'
		return final_str



def cropname(c,a):
	import pandas as pd
	from sklearn.linear_model import LinearRegression
	location = a

	rice_predict_yeild = ""
	rice_predict_profit = ""
	rice_predict_cost =  ""
	cotton_predict_yeild = ""
	cotton_predict_profit = ""    
	cotton_predict_cost = ""
	sugarcane_predict_yeild = ""
	sugarcane_predict_profit = ""
	sugarcane_predict_cost = ""
	wheat_predict_yeild = ""
	wheat_predict_profit = ""
	wheat_predict_cost = ""
	millets_predict_yeild = ""
	millets_predict_profit = ""
	millets_predict_cost = ""
	carda_predict_yeild = ""
	carda_predict_profit = ""
	carda_predict_cost =""
	gin_predict_yeild =""
	gin_predict_profit =""
	gin_predict_cost =""
	coco_predict_yeild =""
	coco_predict_profit =""
	coco_predict_cost =""
	orange_predict_yeild =""
	orange_predict_profit =""
	orange_predict_cost =""
	soya_predict_yeild =""
	soya_predict_profit =""
	soya_predict_cost =""
	mai_predict_yeild =""
	mai_predict_profit =""
	mai_predict_cost = ""

	arr = []
	for i in range(0,7,1):
	    if c[0][i] == 1:
	        if i == 0:
	        	
	        	A = []
	        	A.append("Rice")
	        	arr.append(A)
	        	data = pd.read_csv('cropdata.csv')
	        	data1=data.query('STATE == @location and CROP == @A')
	        	regressor=LinearRegression()
	        	X=data1[['YEAR']]
	        	Y=data1['YEILD']
	        	Z=data1['PROFIT']
	        	W=data1['COST OF CULTIVATION']
	        	#predection of yeild
	        	regressor.fit(X,Y)
	        	#a1=regressor.score(X,Y)*100
	        	rice_predict_yeild = regressor.predict([[2019]])
	        	#predection of profit
	        	regressor.fit(X,Z)
	        	#b1=regressor.score(X,Z)*100
	        	rice_predict_profit = regressor.predict([[2019]])
	        	#prediction of cost of cultivation
	        	regressor.fit(X,W)
	        	#c1=regressor.score(X,W)*100
	        	rice_predict_cost = regressor.predict([[2019]])           
	        elif i == 1:
	            B = []
	            B.append("Cotton")
	            arr.append(B)
	            data = pd.read_csv('cropdata.csv')
	            data2=data.query('STATE == @location and CROP == @B')
	            regressor=LinearRegression()
	            X=data2[['YEAR']]
	            Y=data2['YEILD']
	            Z=data2['PROFIT']
	            W=data2['COST OF CULTIVATION']
	            #prediction of the yeild
	            regressor.fit(X,Y)
	            
	            cotton_predict_yeild = regressor.predict([[2019]])
	            #prediction of the profit
	            regressor.fit(X,Z)
	            
	            cotton_predict_profit = regressor.predict([[2019]])
	            #prediction of cost of cultivation
	            regressor.fit(X,W)
	            cotton_predict_cost = regressor.predict([[2019]])
	        elif i == 2:
	            C = []
	            C.append("Sugarcane")
	            
	            arr.append(C)
	            data = pd.read_csv('cropdata.csv')
	            data3=data.query('STATE == @location and CROP == @C')
	            regressor=LinearRegression()
	            X=data3[['YEAR']]
	            Y=data3['YEILD']
	            Z=data3['PROFIT']
	            W=data3['COST OF CULTIVATION']
	            #prediction of the yeild
	            regressor.fit(X,Y)
	            sugarcane_predict_yeild = regressor.predict([[2019]])
	            #prediction of the profit
	            regressor.fit(X,Z)
	            sugarcane_predict_profit = regressor.predict([[2019]])
	            #prediction of cost of cultivation
	            regressor.fit(X,W)
	            sugarcane_predict_cost = regressor.predict([[2019]])
	        elif i == 3:
	        	D = []
	        	D.append("Wheat")
	        	arr.append(D)
	        	data = pd.read_csv('cropdata.csv')
	        	data4=data.query('STATE == @location and CROP == @D')
	        	regressor=LinearRegression()
	        	X=data4[['YEAR']]
	        	Y=data4['YEILD']
	        	Z=data4['PROFIT']
	        	W=data4['COST OF CULTIVATION']
	        	#prediction of yeild
	        	regressor.fit(X,Y)
	        	wheat_predict_yeild = regressor.predict([[2019]])
	        	#prediction of the profit
	        	regressor.fit(X,Z)
	        	wheat_predict_profit = regressor.predict([[2019]])
	        	#prediction of cost of cultivation
	        	regressor.fit(X,W)
	        	wheat_predict_cost = regressor.predict([[2019]])
	        elif i == 4:
	            E = []
	            E.append("Millets")
	            arr.append(E)
	            data = pd.read_csv('cropdata.csv')
	            data5=data.query('STATE == @location and CROP == @E')
	            regressor=LinearRegression()
	            X=data5[['YEAR']]
	            Y=data5['YEILD']
	            Z=data5['PROFIT']
	            W=data5['COST OF CULTIVATION']
	            #prediction of the yeild
	            regressor.fit(X,Y)
	            millets_predict_yeild = regressor.predict([[2019]])
	            #prediction of the profit
	            regressor.fit(X,Z)
	            millets_predict_profit = regressor.predict([[2019]])
	            #prediction of cost of cultivation
	            regressor.fit(X,W)
	            millets_predict_cost = regressor.predict([[2019]])
	        elif i == 5:
	            F = []
	            F.append("Cardamom")
	            
	            arr.append(F)
	            data = pd.read_csv('cropdata.csv')
	            data6=data.query('STATE == @location and CROP == @F')
	            regressor=LinearRegression()
	            X=data6[['YEAR']]
	            Y=data6['YEILD']
	            Z=data6['PROFIT']
	            W=data6['COST OF CULTIVATION']
	            #prediction of the yeild
	            regressor.fit(X,Y)
	            carda_predict_yeild = regressor.predict([[2019]])
	            #prediction of the profit
	            regressor.fit(X,Z)
	            carda_predict_profit = regressor.predict([[2019]])
	            #prediction of cost of cultivation
	            regressor.fit(X,W)
	            carda_predict_cost = regressor.predict([[2019]])
	        elif i == 6:
	            G = []
	            G.append("Ginger")
	            arr.append(G)
	            data = pd.read_csv('cropdata.csv')
	            data7=data.query('STATE == @location and CROP == @G')
	            regressor=LinearRegression()
	            X=data7[['YEAR']]
	            Y=data7['YEILD']
	            Z=data7['PROFIT']
	            W=data7['COST OF CULTIVATION']
	            #prediction of the yeild
	            regressor.fit(X,Y)
	            gin_predict_yeild = regressor.predict([[2019]])
	            #prediction of the profit
	            regressor.fit(X,Z)
	            gin_predict_profit = regressor.predict([[2019]])
	            #prediction of cost of cultivation
	            regressor.fit(X,W)
	            gin_predict_cost = regressor.predict([[2019]])
	        elif i == 7:
	            H = []
	            H.append("Coconut")
	            
	            arr.append(H)
	            data = pd.read_csv('cropdata.csv')
	            data8=data.query('STATE == @location and CROP == @H')
	            regressor=LinearRegression()
	            X=data8[['YEAR']]
	            Y=data8['YEILD']
	            Z=data8['PROFIT']
	            W=data8['COST OF CULTIVATION']
	            #prediction of the yeild
	            regressor.fit(X,Y)
	            coco_predict_yeild = regressor.predict([[2019]])
	            #prediction of the profit
	            regressor.fit(X,Z)
	            coco_predict_profit = regressor.predict([[2019]])
	            #prediction of cost of cultivation
	            regressor.fit(X,W)
	            coco_predict_cost = regressor.predict([[2019]])
	        elif i == 8:
	            I = []
	            I.append("Orange")
	            arr.append(I)
	            data = pd.read_csv('cropdata.csv')
	            data9=data.query('STATE == @location and CROP == @I')
	            regressor=LinearRegression()
	            X=data9[['YEAR']]
	            Y=data9['YEILD']
	            Z=data9['PROFIT']
	            W=data9['COST OF CULTIVATION']
	            #prediction of the yeild
	            regressor.fit(X,Y)
	            orange_predict_yeild = regressor.predict([[2019]])
	            #prediction of the profit
	            regressor.fit(X,Z)
	            orange_predict_profit = regressor.predict([[2019]])
	            #prediction of cost of cultivation
	            regressor.fit(X,W)
	            orange_predict_cost = regressor.predict([[2019]])
	        elif i == 9:
	            J = []
	            J.append("SOYABEAN")
	            arr.append(J)
	            data = pd.read_csv('cropdata.csv')
	            data10=data.query('STATE == @location and CROP == @J')
	            regressor=LinearRegression()
	            X=data10[['YEAR']]
	            Y=data10['YEILD']
	            Z=data10['PROFIT']
	            W=data10['COST OF CULTIVATION']
	            #prediction of the yeild
	            regressor.fit(X,Y)
	            soya_predict_yeild = regressor.predict([[2019]])
	            #prediction of the profit
	            regressor.fit(X,Z)
	            soya_predict_profit = regressor.predict([[2019]])
	            #prediction of cost of cultivation
	            regressor.fit(X,W)
	            soya_predict_cost = regressor.predict([[2019]])
	        elif i == 10:
	            K = []
	            K.append("Maize")
	            
	            arr.append(K)
	            data = pd.read_csv('cropdata.csv')
	            data11=data.query('STATE == @location and CROP == @K')
	            regressor=LinearRegression()
	            X=data11[['YEAR']]
	            Y=data11['YEILD']
	            Z=data11['PROFIT']
	            W=data11['COST OF CULTIVATION']
	            #prediction of the yeild
	            regressor.fit(X,Y)
	            mai_predict_yeild = regressor.predict([[2019]])
	            #prediction of the profit
	            regressor.fit(X,Z)
	            mai_predict_profit = regressor.predict([[2019]])
	            #prediction of cost of cultivation
	            regressor.fit(X,W)
	            mai_predict_cost = regressor.predict([[2019]])



	#diplaying the prediction data (for RICE)
	if rice_predict_yeild != "" :
	    A.append(rice_predict_yeild)
	if rice_predict_profit != "" :
	    A.append(rice_predict_profit)
	if rice_predict_cost !="" :
	    A.append(rice_predict_cost)

	    
	#displaying the prediction data (for COTTON)
	if cotton_predict_yeild != "" :
	    B.append(cotton_predict_yeild)
	if cotton_predict_profit != "":
	    B.append(cotton_predict_profit)
	if cotton_predict_cost != "":
	    B.append(cotton_predict_cost)

	#diplaying the prediction data (for SUGARCANE)
	if sugarcane_predict_yeild != "":
	    C.append(sugarcane_predict_yeild)
	if sugarcane_predict_profit !="":
	    C.append(sugarcane_predict_profit)
	if sugarcane_predict_cost != "":
	    C.append(sugarcane_predict_cost)

	#displaying prediction data (for WHEAT)
	if wheat_predict_yeild != "":
	    D.append(wheat_predict_yeild)
	if wheat_predict_profit !="":
	    D.append(wheat_predict_profit)
	if wheat_predict_cost != "":
	    D.append(wheat_predict_cost)

	#displaying prediction data(for MILLETS)
	if millets_predict_yeild != "":
	    E.append(millets_predict_yeild)
	if millets_predict_profit !="":
	    E.append(millets_predict_profit)
	if millets_predict_cost != "":
	    E.append(millets_predict_cost)
	    

	#displaying prediction data(for CARDAMOM)
	if carda_predict_yeild != "":
	    F.append(carda_predict_yeild)
	if carda_predict_profit !="":
	    F.append(carda_predict_profit)
	if carda_predict_cost != "":
	    F.append(carda_predict_cost)

	#displaying prediction data(for GINGER)
	if gin_predict_yeild != "":
	    G.append(gin_predict_yeild)
	if gin_predict_profit !="":
	    G.append(gin_predict_profit)
	if gin_predict_cost != "":
	    G.append(gin_predict_cost)
	    
	#displaying prediction data(for COCONUT)
	if coco_predict_yeild != "":
	    H.append(coco_predict_yeild)
	if coco_predict_profit !="":
	    H.append(coco_predict_profit)
	if coco_predict_cost != "":
	    H.append(coco_predict_cost)

	#displaying prediction data(for ORANGE)
	if orange_predict_yeild != "":
	    I.append(orange_predict_yeild)
	if orange_predict_profit !="":
	    I.append(orange_predict_profit)
	if orange_predict_cost != "":
	    I.append(orange_predict_cost)
	    
	#displaying prediction data(for SOYABEAN)
	if soya_predict_yeild != "":
	    J.append(soya_predict_yeild)
	if soya_predict_profit !="":
	    J.append(soya_predict_profit)
	if soya_predict_cost != "":
	    J.append(soya_predict_cost)
	    
	#displaying prediction data(for MAIZE)
	if mai_predict_yeild != "":
	    K.append(mai_predict_yeild)
	if mai_predict_profit !="":
	    K.append(mai_predict_profit)
	if mai_predict_cost != "":
	    K.append(mai_predict_cost)
	return arr
