## M6-Data-Engineering-and-MLOps-Assignments

This Github repo contains the portfolio for Module 6: Data Engineering and MLOps. This portfolio is made to showcase projects and assignments dealing with said category within the Business data science master at Aalborg University.

_________________________________________________________________________________________________________________________________________________________________________

# Assignment 1: Develop a Proof-of-Concept version of an application that is querying a database to provide an output to the user.

Welcome to our first assignment for Module 6: Data Engineering and MLOps, in the Business Data Science master program at Aalborg University. This assignment is a collaboration between Raiyan M.D and Kasper R. Haurum.

Our primary objective for this assignment is to develop a proof-of-concept application that queries a database to provide an output to the user. We chose to work with an SQL database, specifically SQLite, and demonstrated the implementation of a semantic search application using SQLite, Pandas, Sentence Transformers, and Gradio.

Initially, we installed the necessary libraries and tools, including SQLite, Pandas, NumPy, NLTK, scikit-learn, and Sentence Transformers. We then created an SQLite database and defined a table schema for storing documents. To populate the database, we used the 20 newsgroups dataset from scikit-learn.

Before analyzing the data, we loaded it from the SQLite database into a Pandas DataFrame and preprocessed the content using the Natural Language Toolkit (NLTK). Next, we created embeddings for the preprocessed content using the SentenceTransformer library with the "paraphrase-MiniLM-L6-v2" model.

Once the database was set up and the embeddings were generated, we implemented a search function that calculates cosine similarities between a user's query and the document embeddings. This function returns the most similar documents based on the user's input. To present the search results, we created a display function that shows the results in a readable format.

Finally, we installed Gradio and set up a Gradio interface for user interaction with the semantic search application. This interface allows users to search for similar documents within the 20 newsgroups dataset and can be deployed on Hugging Face Spaces.

Throughout this assignment, we have successfully built a proof-of-concept application capable of performing semantic search and retrieving relevant documents based on user input. This project showcases our ability to work with various data engineering tools and techniques, thus showcasing a proof-of-concept application follows the logic of our course at AAU.
