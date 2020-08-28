def patk(actual, pred, k):
	#we return 0 if k is 0 because 
	#   we can't divide the no of common values by 0 
	if k == 0:
		return 0

	#taking only the top k predictions in a class 
	k_pred = pred[:k]

	#taking the set of the actual values 
	actual_set = set(actual)

	#taking the set of the predicted values 
	pred_set = set(k_pred)

	#taking the intersection of the actual set and the pred set
		# to find the common values
	common_values = actual_set.intersection(pred_set)

	return len(common_values)/len(pred[:k])

#defining the values of the actual and the predicted class
y_true = [1 ,2, 0]
y_pred = [1, 1, 0]

if __name__ == "__main__":
    print(patk(y_true, y_pred,3))












