import numpy as np
import pk

def apatk(acutal, pred, k):
	#creating a list for storing the values of precision for each k 
	precision_ = []
	for i in range(1, k+1):
		#calculating the precision at different values of k 
		#      and appending them to the list 
		precision_.append(pk.patk(acutal, pred, i))

	#return 0 if there are no values in the list
	if len(precision_) == 0:
		return 0 

	#returning the average of all the precision values
	return np.mean(precision_)

#defining the values of the actual and the predicted class
y_true = [[1,2,0,1], [0,4], [3], [1,2]]
y_pred = [[1,1,0,1], [1,4], [2], [1,3]]

if __name__ == "__main__":
	for i in range(len(y_true)):
		for j in range(1, 4):
			print(
				f"""
				y_true = {y_true[i]}
				y_pred = {y_pred[i]}
				AP@{j} = {apatk(y_true[i], y_pred[i], k=j)}
				"""
			)