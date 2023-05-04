## M6-Data-Engineering-and-MLOps-Assignments

This Github repo contains the portfolio for Module 6: Data Engineering and MLOps. This portfolio is made to showcase projects and assignments dealing with said category within the Business data science master at Aalborg University.

_________________________________________________________________________________________________________________________________________________________________________

# Assignment 1: Develop a Proof-of-Concept version of an application that is querying a database to provide an output to the user.

Welcome to our first assignment for Module 6: Data Engineering and MLOps, for the business data science master program at Aalborg University. This assignment is a collaboration between Raiyan M.D and Kasper R. Haurum.

Our primary objective for this assignment is to develop a proof-of-concept application that queries a database to provide an output to the user. We chose to work with an SQL database, specifically SQLite, and demonstrated the implementation of a semantic search application using SQLite, Pandas, Sentence Transformers, and Gradio.

Initially, we installed the necessary libraries and tools, including SQLite, Pandas, NumPy, NLTK, scikit-learn, and Sentence Transformers. We then created an SQLite database and defined a table schema for storing documents. To populate the database, we used the 20 newsgroups dataset from scikit-learn.

Before analyzing the data, we loaded it from the SQLite database into a Pandas DataFrame and preprocessed the content using the Natural Language Toolkit (NLTK). Next, we created embeddings for the preprocessed content using the SentenceTransformer library with the "paraphrase-MiniLM-L6-v2" model.

Once the database was set up and the embeddings were generated, we implemented a search function that calculates cosine similarities between a user's query and the document embeddings. This function returns the most similar documents based on the user's input. To present the search results, we created a display function that shows the results in a readable format.

Finally, we installed Gradio and set up a Gradio interface for user interaction with the semantic search application. This interface allows users to search for similar documents within the 20 newsgroups dataset.

Throughout this assignment, we have successfully built a proof-of-concept application capable of performing semantic search and retrieving relevant documents based on user input. This project showcases our ability to work with various data engineering tools and techniques, thus showcasing a proof-of-concept application follows the logic of our course at AAU.
_________________________________________________________________________________________________________________________________________________________________________

# Assignment 2: PERFORMING A BIG DATA WORKFLOW WITH SPARK AND POLARS

Our primary objective for this assignment is to develop either Apache Spark or Polars to perform the complete EDA report. We went for both unified analytics engines for large-scale data processing. In order to test the strength of the understanding.

## Polars

In the first stage, we loaded the HR dataset into the platform and perform basic exploratory data analysis (EDA) to understand the structure of the data. This includes checking the dimensions of the dataset, examining the data types, and identifying missing values. Added to that we also fill in the missing values using Polars functionality in the first step.

In the second stage, we filter the data to include only the relevant observations. We did it by removing missing values and filtering based on certain criteria and conditions that are specific to our dataset. We filtered out HR_subset to focus on the specific part of the data and minimize memory loss. From that subset, we dig down further to find the attrition level at a different stage.

In the third stage, we aggregate the data to obtain summary statistics and metrics. We ran different aggregations using functions such as filter(), groupby(), etc. Added to that, we calculated the mean, median, or mode of certain variables to gain a better understanding of the data.

In the fourth stage, we join the employee satisfaction data with HR dataset to perform a more complex analysis. Here we merged two tables using a common key. Which is Employee ID. Through Employee ID, we tried to find out employees’ satisfaction levels in different categories. This gave us the opportunity to perform a more complex analysis.

Finally, We visualized the data plotly.express. Plotly express is a Polars’ visualization tool. We used it to identify the different variables and understand it in a better way.

## Apache Spark

For the Apache Spark we used the "Nomadlist" dataset. This dataset was used in the first semester within the M1 - Applied Data Science and Machine Learning module. We select this to start to perform the Exploratory Data Analysis (EDA) and data operations. 
 
To begin, we start by installing PySpark and creating a Spark session named "TripsEDA." It then downloads the dataset from a GitHub repository using the urllib.request library. The dataset is loaded into a Spark dataframe, and basic EDA is performed to understand its structure, including dimensions, data types, and missing values.

To filter relevant observations, the data is filtered based on three conditions: ensuring the trip end date is greater than the start date, and that both latitude and longitude values are not null. This process removes trips with negative durations and those missing location data points.

Next, the data is grouped by country, place, and username to identify the most popular destinations for digital nomads and the most frequent travelers. The code leverages Spark's groupBy and agg functions to count the number of trips per country, place, and user.

In Step 3, the data is aggregated to obtain summary statistics and metrics for trips per country, place, and username. The number of trips for each category is displayed, and to make the data cleaner and more understandable, the minimum, maximum, and average number of trips are calculated for each category.

For countries, the most popular one received 7,337 digital nomads, while the least popular had only one visitor. On average, countries receive 181 visitors. Summary statistics are also calculated for trips per place and trips per username.

Next, we display the top 10 countries, places, and usernames with the highest number of trips. The data is ordered by the number of trips in descending order, and the top 10 entries are shown without truncation.

Similarly, the bottom 10 countries, places, and usernames with the least number of trips are displayed. The data is arranged based on the number of trips in increasing order, and the top 10 entries are shown without truncation. This analysis helps to identify popular destinations and frequent travelers, as well as less-visited locations and less-active users on the Nomadlist platform.

In the final steps, the data is visualized using bar charts to display the top 10 most visited places, countries, and usernames. First, the necessary libraries are imported, and the data is grouped by place, username, and country, counting the number of trips in each group.

For each category, the top 10 entries are selected, ordered by the number of trips in descending order. These entries are then converted to Pandas dataframes and plotted as bar charts. The x-axis represents the place, username, or country, while the y-axis represents the number of trips. The bar charts provide a clear visual representation of the most popular places, countries, and users on the Nomadlist platform.

In conclusion, the coding used in this assignment demonstrates high-quality data processing and analysis using Apache Spark. It efficiently performs EDA, filters relevant observations, calculates summary statistics, and visualizes the results. By leveraging the power of Spark and its groupBy, agg, and orderBy functions, the code effectively analyzes the Nomadlist dataset to provide insights into popular destinations and frequent travelers.

_________________________________________________________________________________________________________________________________________________________________________

# Assignment 3: TRACKING AND MANAGING PROJECT WITH MLFLOW

At the first phase of the project importing important libraries and loading the HR dataset is the main key. Here, HR dataset from our previous project will be used for Elastic net and it will be transfered to MLflow to track and monitor the project. Where the optimal and best case model can be identified.

In the second phase of the project there will be some EDA. Where data will be resized and reshaped for the machine learning purpose. The HR dataset have some missing values and some unsupported conditions for machine learning project. In this section managing data through EDA will be the key.

In the third phase of the project, here, Elasticnet is selected from scikit-learn. To perform Elasticnet at forst some evaluation metrics has been set. Where RMSE, MAE and R2 (R square test) will be the priority. Then data has been spilited for train and test focusing on the attrition in the data set. Where yes is 1 and No is 0. Added to that for the prediction MLflow has started to run. Where in the backend API MLflow will start to store the prediction of the model with the accuracy level and the result. In the final stage of the MLflow, logging parameter and metrics is the final task. Based on which MLflow API will perform the chart related analysis. After performing the code, all the model will shift to MLflow. In the next step evaluation of every training model based on different parameter will give different RMSE, MAE and R2 score. The operator of the model then can identify which model is the best depending on the different parameter that has been used in the model. In this project 5 different set of training model has been evaluated.

NGROK has been used to visualize the MLflow UI. Through NGROK the local host will able to showcase the different model through MLflow UI. Here 5000 Mlflow UI port has been used in this project.

In Conclusion this project demonstrate the tracking and managing project with MLflow. Either it can be done with google drive or SQLite to store the structured and unstructured data of the project. Added to that managing the project and registering the model also can be done through MLflow.
_________________________________________________________________________________________________________________________________________________________________________

# Assignment 4: Dockerizing an MLflow-based ML App with SQLite and Streamlit Interface

In this last assignment for Module 6: Data Engineering and MLOps, We, Raiyan M.D and Kasper R. Haurum collaborate to enhance a previous machine learning project by incorporating MLflow for experiment tracking and management. The assignment also involves integrating SQLite for storing structured and unstructured information related to the trained model. As part of the task, we have developed a user-friendly interface for the machine learning application using Streamlit, with the option to create a custom three-layer app. Finally, we dockerize the application and upload it to Docker Hub.

To meet the objectives of the assignment, we picked a suitable machine learning model, which is ran by the HR-dataset from our 1st semester, that is specifically an ElasticNet regression model. We then successfully integrate MLflow for tracking and managing machine learning experiments by logging hyperparameters, metrics, and artifacts of the experiments in MLflow. Additionally, we then save structured and unstructured information related to the trained model in SQLite within MLflow.

The results presented showcase the performance of the ElasticNet regression model for different combinations of alpha and l1_ratio hyperparameters. The performance is evaluated using three metrics: Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), and R-squared (R2).

* For alpha = 0.5 and l1_ratio = 0.5, the model yields:
RMSE: 0.36593
MAE: 0.26888
R2: 0.02966

* For alpha = 0.5 and l1_ratio = 0.4, the model yields:
RMSE: 0.35482
MAE: 0.26236
R2: 0.00893

* For alpha = 0.5 and l1_ratio = 0.3, the model yields:
RMSE: 0.36319
MAE: 0.26633
R2: 0.03157

* For alpha = 0.5 and l1_ratio = 0.2, the model yields:
RMSE: 0.36605
MAE: 0.26781
R2: 0.05331

* For alpha = 0.5 and l1_ratio = 0.1, the model yields:
RMSE: 0.33680
MAE: 0.25141
R2: 0.06528

The results reveal that the model with alpha = 0.5 and l1_ratio = 0.1 has the lowest RMSE and MAE, and the highest R2 value. This combination of hyperparameters provides the best performance among the tested configurations.

The next step is to create a user-friendly interface for the machine learning application using Streamlit, a popular open-source framework. The interface is designed to allow users to input data and obtain predictions from the trained model easily. The main application file is named "app.py," which contains the necessary code to create and run the Streamlit interface.

The code in "app.py" first imports necessary libraries such as NumPy, pandas, and Streamlit. It then loads the pre-trained model from a pickle file. The predict_HR function is defined to take in three parameters: Mean Absolute Error (mae), Root Mean Squared Error (rmse), and R-squared (r2), and returns the prediction from the trained model.

The main function is responsible for creating the web interface using Streamlit functions. It starts by setting the title of the web application and then adds a styled header using HTML. The user is prompted to enter the values for mae, rmse, and r2 through text input fields. When the "Predict" button is clicked, the predict_HR function is called, and the prediction result is displayed on the interface. An "About" button is also provided to display additional information about the application.

To ensure that the application runs smoothly and has all the necessary dependencies, a "requirements.txt" file is created. This file lists the required packages and their respective versions to be installed, such as mlflow, numpy, scikit-learn, and streamlit. By specifying the dependencies in this file, it becomes easier to manage the application's environment and ensure compatibility across different systems.

To further enhance the portability and ease of deployment for the machine learning application, it is dockerized. Dockerization involves creating a lightweight, standalone, and executable software package called a Docker container. This container encapsulates the application, its dependencies, and system tools, ensuring that it runs consistently across different environments.

In this project, a Dockerfile is created to define the necessary instructions to build the Docker image. The Dockerfile contains the following steps:

* The base image is set to Python 3.9, which provides the required Python runtime environment.
* The package list is updated, and sudo is installed for any additional package management needs within the container.
* The application files are copied from the local directory to the /app directory within the container.
* The working directory inside the container is set to /app.
* The requirements.txt file is used to install the necessary packages via pip, ensuring that all dependencies are available within the container.
* The rest of the application code is copied into the /app directory in the container.
* The main script, M6_Data_Engineering_and_MLOps_Assignment_4_appfile.py, is made executable.
* The container's exposed port is set to 8501, allowing communication with the Streamlit web interface.
* Finally, the ENTRYPOINT command specifies how the container should be executed. In this case, the command runs the Streamlit application (M6_Data_Engineering_and_MLOps_Assignment_4_appfile.py) on port 8501 and allows it to accept connections from any IP address (0.0.0.0).

By following these instructions in the Dockerfile, the application, SQLite database, MLflow, and Streamlit interface are all encapsulated within a Docker container. This ensures that they function correctly and consistently, regardless of the host environment. Once the Docker image is built, it can be easily shared, deployed, and run on any system with Docker installed.

To upload my dockerized app to Docker Hub and provide instructions for running the app from the Docker Hub repository based on the provided Dockerfile, I followed these steps:

First, I ensured I had a Docker Hub account. If I didn't have one, I would sign up at https://hub.docker.com/signup.

Then, I opened the terminal or command prompt and logged in to my Docker Hub account using the following command:


docker login --username=raiyan1012 --password=<my_dockerhub_password>

I replaced <my_dockerhub_password> with my actual Docker Hub password.

Next, I built my Docker image using the provided Dockerfile. I navigated to the directory containing the Dockerfile and ran the following command:

docker build -t raiyan1012/dockerfile:v1.0.0 .

After successfully building the image, I pushed it to my Docker Hub repository with this command:

docker push raiyan1012/dockerfile:v1.0.0

To run the app from the Docker Hub repository, I provided these instructions:
First, execute the following command on any machine with Docker installed:

docker run -p 8501:8501 raiyan1012/dockerfile:v1.0.0

Once the app is running, open a web browser and navigate to http://localhost:8501 to access the Streamlit app.

By following these steps, I successfully uploaded my dockerized app to Docker Hub using the username raiyan1012 and provided instructions for running the app from the Docker Hub repository.
