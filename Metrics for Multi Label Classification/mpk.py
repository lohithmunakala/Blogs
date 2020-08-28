import numpy as np
import apk

def mapk(acutal, pred, k):

	#creating a list for storing the Average Precision Values
	average_precision = []
	#interating through the whole data and calculating the apk for each 
	for i in range(len(acutal)):
		average_precision.append(apk.apatk(acutal[i], pred[i], k))

	#returning the mean of all the data
	return np.mean(average_precision)

#defining the values of the actual and the predicted class
y_true = [[1,2,0,1], [0,4], [3], [1,2]]
y_pred = [[1,1,0,1], [1,4], [2], [1,3]]

if __name__ == "__main__":
    print(mapk(y_true, y_pred,3))