# Project2-WorkerGarment
 regression problem
Heart Disease Prediction
 Make prediction on patient have heart disease or not
 link: https://archive.ics.uci.edu/ml/datasets/Productivity+Prediction+of+Garment+Employees
 
 
 1. Summary
 - To make prediction productivity range of worker
 - This is regression problem as it's determine the productivity of worker range from 0 to 1
 - the deep learning model is used and trained
 - The model is self-made

2. IDE and Framework
- The project built with Spyder as the main IDE
- use Tensorflow, Keras, Numpy, Mathplot

3. Methodology
- The dataset was obtained in form of csv containing the 1196 samples with 15 features.
- perform data cleaning to see the null data is available or not. In this project there
  is null data in the 'wip' column. we fill up the null in wip column with the mean of the wip column.  
  There is data that are not relate dto work productivity such as date, day and quarter column. We remove this column.
  There are a categorical data in the department column. There are 2 deparment which is 'sweing' and 'finishing'. We perform OneHotLabel as the all data need to be in   int not in string.
  
- Perform data preprocessing where we spilt data into feature(inputs) and label (output). The output is in the form of probabilities (0~1), to show that this project     is regression problem
- the model constist of 7 dense layers. 
- Model summary:
![image](https://user-images.githubusercontent.com/73817610/174978773-e3b2c535-f39d-4386-80c3-79c30b793f9a.png)

-The model is compile with optimizer of 'adam' with learning rate = 0.001, loss= mse (mean-squared-error), metrics of mae(mean-absolute-error), batch_size of 16 and epochs of 200
- The value is display by using TensorBoard:

![image](https://user-images.githubusercontent.com/73817610/174979469-16ea0541-5e16-43fe-b7c2-0f25a075d550.png)


![image](https://user-images.githubusercontent.com/73817610/174979581-097b8d35-ec48-460d-9281-02121ef8349d.png)

