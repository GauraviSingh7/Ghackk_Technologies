# Webtoon Content Classifier, Sentiment Analysis, and Chatbot

## Project Overview
This project consists of three main tasks focused on webtoons and user comments. The tasks include building a content classifier for webtoon descriptions, performing sentiment analysis on user comments about manga and manhwa, and developing a basic chatbot that provides information about the "Castle Swimmer" webtoon.

## Tasks

### Task 1: Content Classifier
- **Objective**: Create a simple content classifier that categorizes webtoon descriptions into genres such as romance, action, and fantasy.
- **Dataset**: A dataset of 50 webtoon descriptions was utilized for training the model.
- **Implementation**: 
  - Used Python with the scikit-learn library.
  - Implemented a basic classification model (Decision Tree/Logistic Regression).
  - **Accuracy**: The model achieved an accuracy of approximately 60% due to the small dataset size and basic implementation.

### Task 2: Sentiment Analysis
- **Objective**: Perform a basic sentiment analysis on user comments regarding "The Difference Between Manga And Manhwa".
- **Dataset**: A dataset of 46 user comments was used for analysis.
- **Implementation**: 
  - Utilized the TextBlob library to classify comments as positive or negative.
  - Provided a summary of results, including the percentage of positive vs. negative comments.

### Task 3: Basic Chatbot
- **Objective**: Build a simple chatbot that answers questions related to "Castle Swimmer Chapter 83-89".
- **Implementation**: 
  - Used Python and the NLTK library for basic natural language processing.
  - The chatbot utilizes predefined keywords and responses to answer questions like "What is Castle Swimmer about?" and "Who are the main characters?".
  - Note: This implementation is not an intelligent chatbot and relies on fixed responses.
