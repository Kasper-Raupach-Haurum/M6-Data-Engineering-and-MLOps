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

#Polars

In the first stage, we loaded the HR dataset into the platform and perform basic exploratory data analysis (EDA) to understand the structure of the data. This includes checking the dimensions of the dataset, examining the data types, and identifying missing values. Added to that we also fill in the missing values using Polars functionality in the first step.

In the second stage, we filter the data to include only the relevant observations. We did it by removing missing values and filtering based on certain criteria and conditions that are specific to our dataset. We filtered out HR_subset to focus on the specific part of the data and minimize memory loss. From that subset, we dig down further to find the attrition level at a different stage.

In the third stage, we aggregate the data to obtain summary statistics and metrics. We ran different aggregations using functions such as filter(), groupby(), etc. Added to that, we calculated the mean, median, or mode of certain variables to gain a better understanding of the data.

In the fourth stage, we join the employee satisfaction data with HR dataset to perform a more complex analysis. Here we merged two tables using a common key. Which is Employee ID. Through Employee ID, we tried to find out employees’ satisfaction levels in different categories. This gave us the opportunity to perform a more complex analysis.

Finally, We visualized the data plotly.express. Plotly express is a Polars’ visualization tool. We used it to identify the different variables and understand it in a better way.

##Apache Spark

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
