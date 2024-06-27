The spam detection project is a comprehensive implementation of a machine learning-based email classification system. The project is designed to detect spam emails using advanced data preprocessing techniques, natural language processing (NLP), and machine learning algorithms. The system is built using Python, leveraging its robust libraries for data processing and machine learning.


The project is organized into six main files, each serving a specific purpose in the overall system:

1. **data_preprocessing_funcs.py**:
    - This module contains functions for preprocessing email text. It handles tasks such as removing stopwords, cleaning text, extracting special symbols, and vectorizing text for machine learning models.

2. **symbols_vectorizer.py**:
    - This module defines a custom vectorizer for special symbols found in the emails. It provides methods to fit the vectorizer to a dataset and transform the symbols into numerical representations.

3. **data_preprocessing.ipynb**:
    - This Jupyter Notebook handles data loading, preprocessing, and splitting. It reads email data, cleans and processes the text, vectorizes the content, and prepares the dataset for training and testing the machine learning models.

4. **model_training.ipynb**:
    - This notebook is dedicated to training and evaluating various machine learning models. It includes hyperparameter tuning using GridSearchCV and evaluates models like Naive Bayes, Support Vector Machine, Random Forest, and Gradient Boosting.

5. **model.py**:
    - This script defines the `SpamFilter` class, encapsulating the entire spam detection process. It includes methods for checking single emails and batches of emails, using the trained model and vectorizers.

6. **model_testing.ipynb**:
    - This notebook is used for testing the `SpamFilter` class on new data. It demonstrates how to use the trained model to make predictions on unseen emails.

Key Components:

1. Data Preprocessing
Data preprocessing is a crucial step in building an effective spam filter. This project employs several techniques to clean and prepare the data:

- **Stopwords Removal**: Using NLTK, common English stopwords are removed from the email text.
- **Text Cleaning**: Regular expressions are used to remove non-alphabetic characters and redundant spaces.
- **Special Symbols Extraction**: Special symbols are extracted from emails to help identify patterns common in spam.

2. Vectorization
The project uses two types of vectorizers:

- **Text Vectorizer**: Converts cleaned email text into numerical features using `CountVectorizer` from scikit-learn.
- **Special Symbols Vectorizer**: A custom vectorizer defined in `symbols_vectorizer.py` that transforms special symbols into numerical representations.

3. Model Training and Evaluation
Several machine learning models are trained and evaluated to identify the best performing algorithm for spam detection:

- **Naive Bayes (MultinomialNB, BernoulliNB, ComplementNB)**
- **Support Vector Machine (SVC)**
- **Random Forest Classifier**
- **Gradient Boosting Classifier**

Hyperparameter tuning is performed using GridSearchCV to optimize the models.

4. Spam Filter Class
The `SpamFilter` class encapsulates the logic for spam detection. It utilizes the trained model and vectorizers to predict whether a given email is spam or not. The class provides methods to check individual emails and batches of emails.

5. Model Testing
The testing notebook demonstrates the usage of the `SpamFilter` class with real email data, showcasing its effectiveness and accuracy in identifying spam.

6. Dataset
The dataset used in this project comprises randomly collected emails, which are classified as either spam or ham (non-spam). The first column contains the spam/ham classification, while the second column contains the email text, it also contains 3 columns with NaNs. This dataset provides a diverse set of examples to train and test the spam detection models effectively.

7. Conclusion
This project highlights key skills in Python programming, data preprocessing, natural language processing, and machine learning. It demonstrates the complete workflow of building,training, and deploying a machine learning model for a practical application like spam detection. The Spam Filter project is an excellent showcase for aspiring Python developers and machine learning engineers, illustrating the application of these technologies in solving real-world problems.

The following image shows the result of ParkingTracker work:<img width="411" alt="aaa" src="https://github.com/osipgas/spam-detection/assets/115102730/b5a74b95-732a-47be-93bb-103a94035613">
