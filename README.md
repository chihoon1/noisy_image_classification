This project was a class project in Deep Learning course, and the dataset is comprised of MNIST image contaminated by noise. I used deep residual CNN model with squeeze and excitation trained with cos decay learning rate with warmup and achieved above 90% testing accuracy.
The dataset was zipped after dividing into three dataset due to the size of dataset. To combine all the data into one dataset, the function in data_merge.py can be used.

For future work, I will analyzed the features learned in the model to analyze the noise applied into the dataset.
