# Categorical Embedder

 **Categorical Embedder** is a python package that let's you convert your categorical variables into numeric via Neural Networks

## Installation

`pip install categorical_embedder`

## Example
```py
import categorical_embedder as ce
from sklearn.model_selection import train_test_split

df = pd.read_csv('HR_Attrition_Data.csv')
X = df.drop(['employee_id', 'is_promoted'], axis=1)
y = df['is_promoted']

embedding_info = ce.get_embedding_info(X)
X_encoded,encoders = ce.get_label_encoded_data(X)

X_train, X_test, y_train, y_test = train_test_split(X_encoded,y)

embeddings = ce.get_embeddings(X_train, y_train, categorical_embedding_info=embedding_info, 
                            is_classification=True, epochs=100,batch_size=256)
```
A more detailed [Jupyter Notebook](http://www.github.com ) can be found here

> What's inside **Categorical Embedder** ?
* `ce.get_embedding_info(data,categorical_variables=None)`: This function identifies all categorical variables in the data, determines its embedding size. Embedding size of the categorical variables are determined by minimum of 50 or half of the no. of its unique values i.e. embedding size of a column  = Min(50, # unique values in that column)
One can pass explicit list of categorical variables in `categorical_variables` parameter. If `None`, this function automatically takes all the variables with data type `object`
* `ce.get_label_encoded_data(data, categorical_variables=None)`: This function label encodes (integer encoding) all the categorical variables using sklearn.preprocessing.LabelEncoder and returns a label encoded dataframe for training. Keras/tensorflow or any other deep learning library would expect the data to be in this format.
* `ce.get_embeddings(X_train, y_train, categorical_embedding_info=embedding_info, is_classification=True,                          epochs=100,batch_size=256)`: This function trains a shallow neural networks and returns embeddings of categorical variables. Under the hood, It is a 2 layer neural network architecture with 1000 and 500 neurons with 'ReLU' activation. It takes 4 required inputs -  `X_train`, `y_train`, `categorical_embedding_info`:output of get_embedding_info function and `is_classification`: `True` for classification tasks; `False` for regression tasks.

For classification: `loss = 'binary_crossentropy'; metrics = 'accuracy'` and for regression: `loss = 'mean_squared_error'; metrics = 'r2'`

## Dependencies
```numpy
pandas
scikit-learn
tensorflow
keras
tqdm
keras-tqdm
```


