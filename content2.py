import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

# Step 1: Create a larger dataset with 50 webtoon descriptions
data = {
    'description': [
        "A high school girl navigates life and romance while hiding her true self from the world.",
        "A prince with supernatural powers fights against evil forces to protect his kingdom.",
        "A shy girl develops feelings for a popular boy, leading to a complicated love triangle.",
        "In a futuristic world, a group of rebels fight against a totalitarian government.",
        "A group of high school students discover they have magical abilities and must fight to save the world.",
        "A young woman works to achieve her dreams while dealing with the ups and downs of relationships.",
        "A man with superhuman strength must save the city from a crime syndicate.",
        "Two childhood friends reconnect and discover hidden feelings for each other.",
        "A warrior from another dimension is sent to Earth to protect it from an ancient evil.",
        "A girl from a wealthy family falls in love with a poor boy, but their love is tested by societal pressures.",
        "An ordinary boy finds a magical notebook that gives him the power to control people's fates.",
        "A talented musician falls in love with a dancer, but their dreams push them apart.",
        "A young woman discovers she's the reincarnation of an ancient warrior and must battle dark forces.",
        "Two best friends from different social classes try to navigate high school life and their growing feelings.",
        "A mysterious boy transfers to a new school and causes chaos among the student body.",
        "A man wakes up in a video game world where he must level up to escape.",
        "A romance blossoms between a vampire and a human, but danger lurks around every corner.",
        "A high school sports team faces their biggest rivals in the championship game.",
        "A detective with psychic abilities solves crimes in a world where magic is real.",
        "A princess must choose between duty to her kingdom and the love of her life.",
        "A girl discovers her drawings come to life and uses her powers to fight evil.",
        "A team of misfits comes together to protect their town from supernatural threats.",
        "A romance story between a chef and a food critic who can't stand each other.",
        "A martial artist trains to become the strongest fighter in the world.",
        "A young woman with amnesia tries to piece together her past while being hunted by mysterious forces.",
        "A secret agent falls in love with the enemy while on a dangerous mission.",
        "Two high school students accidentally swap bodies and must learn to live each other's lives.",
        "A wizard goes on a quest to find an ancient artifact that can save the world.",
        "A romance develops between two people who meet through an online game.",
        "A group of high schoolers must survive after being stranded on a mysterious island.",
        "A girl with the ability to see ghosts helps spirits move on to the afterlife.",
        "A rising star in the fashion world must choose between career success and true love.",
        "A young boy discovers he has superpowers and joins a superhero academy.",
        "A prince is betrayed by his closest allies and must fight to reclaim his throne.",
        "A romance between a mermaid and a human is threatened by their different worlds.",
        "A group of treasure hunters race against time to find a lost city.",
        "A high school girl with a secret crush tries to confess her feelings before it's too late.",
        "A boy from the future is sent back in time to save the world from destruction.",
        "A detective and a criminal mastermind engage in a deadly game of cat and mouse.",
        "A young woman must choose between her family's expectations and the man she loves.",
        "A vampire hunter falls in love with his prey, leading to a forbidden romance.",
        "A group of friends uncover a conspiracy that threatens to destroy their city.",
        "A romance between two coworkers is complicated by office politics.",
        "A samurai seeks revenge after his family is killed by a rival clan.",
        "A boy who can control time must stop an evil organization from taking over the world.",
        "A high school girl competes in a national singing competition to achieve her dreams.",
        "A warrior embarks on a journey to avenge the death of his mentor.",
        "A boy who is cursed to turn into a monster must find a way to break the curse.",
        "A romance develops between two childhood friends who lost touch over the years."
    ],
    'category': [
        "romance", "action", "romance", "action", "fantasy", "romance", "action", "romance", "fantasy", "romance",
        "fantasy", "romance", "fantasy", "romance", "fantasy", "fantasy", "romance", "action", "fantasy", "romance",
        "fantasy", "fantasy", "romance", "action", "fantasy", "romance", "fantasy", "romance", "action", "fantasy",
        "fantasy", "romance", "fantasy", "action", "romance", "action", "romance", "fantasy", "action", "romance",
        "fantasy", "action", "romance", "action", "fantasy", "romance", "action", "fantasy", "romance"
    ]
}

df = pd.DataFrame(data)

# Step 2: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['description'], df['category'], test_size=0.3, random_state=42)

# Step 3: Text vectorization (convert text to numerical data) and model setup
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('clf', RandomForestClassifier(random_state=42))
])

# Step 4: Define parameter grid for GridSearchCV
param_grid = {
    'tfidf__ngram_range': [(1, 1), (1, 2), (1, 3)],
    'tfidf__max_features': [None, 1000, 5000],
    'clf__n_estimators': [100, 200],
    'clf__max_depth': [None, 10, 20]
}

# Step 5: Perform GridSearchCV
grid_search = GridSearchCV(pipeline, param_grid, cv=5, n_jobs=-1, verbose=1)
grid_search.fit(X_train, y_train)

# Print best parameters
print("Best parameters:", grid_search.best_params_)

# Step 6: Make predictions and evaluate the model
y_pred = grid_search.predict(X_test)

# Step 7: Display accuracy and classification report
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print("Classification Report:\n", classification_report(y_test, y_pred, zero_division=1))

# Step 8: Test on a new description
new_description = ["a high school girl falls in love"]
new_description_pred = grid_search.predict(new_description)
print(f"Prediction for new description: {new_description_pred[0]}")

# Step 9: Perform cross-validation
scores = cross_val_score(grid_search.best_estimator_, df['description'], df['category'], cv=5)
print(f"Cross-validated scores: {scores}")
print(f"Mean cross-validated score: {scores.mean()}")