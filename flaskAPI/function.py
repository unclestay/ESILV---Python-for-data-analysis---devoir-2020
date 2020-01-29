import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import seaborn as sns

df = pd.read_csv("log_final.csv")
X = df.iloc[:, :-1]
y = df["rest_time2"]
X_train, X_test, Y_train, Y_test = train_test_split(X, y)


def get_hyperparametres(n_estimators, max_features, max_depth):
    hyperparametres = {"n_estimators": n_estimators,
                       "max_features": max_features,
                       "max_depth": max_depth}
    return hyperparametres


def get_algorithm(n_estimators, max_features, max_depth):
    algorithm = RandomForestRegressor(n_estimators=n_estimators, max_features=max_features, max_depth=max_depth)
    return algorithm


def get_score(algorithm, X_train, X_test, Y_train, Y_test):
    modele = algorithm.fit(X_train, Y_train)
    score = modele.score(X_test, Y_test)
    return score


#score = get_score(get_algotithm(50,9,50)),X_train, X_test, Y_train, Y_test)
#print(score)