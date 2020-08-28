from sklearn.metrics import f1_score
from sklearn.preprocessing import MultiLabelBinarizer

def f1_sampled(actual, pred):
    #converting the multi-label classification to a binary output
    mlb = MultiLabelBinarizer()
    actual = mlb.fit_transform(actual)
    pred = mlb.fit_transform(pred)

    #fitting the data for calculating the f1 score 
    f1 = f1_score(actual, pred, average = "samples")
    return f1

#defining the values of the actual and the predicted class
y_true = [[1,2,0,1], [0,4], [3], [1,2]]
y_pred = [[1,1,0,1], [1,4], [2], [1,3]]

if __name__ == "__main__":
    print(f1_sampled(y_true, y_pred))