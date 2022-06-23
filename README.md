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











####Start eith tiny model
![image](https://user-images.githubusercontent.com/73817610/175193619-f99b4852-2a1f-4e74-ae06-2cfa796170c3.png)
![image](https://user-images.githubusercontent.com/73817610/175193927-63c50ffa-2fbd-46b2-bee7-9b6bd5caafb4.png)
![image](https://user-images.githubusercontent.com/73817610/175194007-656ad73f-ffc3-43b9-ae98-56092d8073dd.png)

###Then small model
![image](https://user-images.githubusercontent.com/73817610/175194178-972c7e45-a779-4847-8e1d-144fdf46bb95.png)
![image](https://user-images.githubusercontent.com/73817610/175194265-cd532d8b-ec4c-4e49-8b97-ecf3034d9dcb.png)
![image](https://user-images.githubusercontent.com/73817610/175194390-72d533a3-02d2-4a9b-a85b-9908b078ff50.png)
##medium model
![image](https://user-images.githubusercontent.com/73817610/175194591-a89df7fa-b0c4-4157-b0a0-52f3578c585b.png)
![image](https://user-images.githubusercontent.com/73817610/175194661-d1e0fcf5-93c8-4a58-a894-3dcdb126cc7f.png)
![image](https://user-images.githubusercontent.com/73817610/175194795-80af2829-c8e5-4520-bac2-9abfa31ce484.png)





