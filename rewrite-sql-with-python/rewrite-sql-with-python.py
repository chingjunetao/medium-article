import pandas as pd 

titanic_df = pd.read_csv("titanic_test_data.csv")


# SELECT, DISTINCT, COUNT, LIMIT 
"""
SELECT name
FROM titanic_test_data

"""

titanic_df["name"]


"""
SELECT *
FROM titanic_test_data
LIMIT 5

"""
titanic_df.head(5)


"""
SELECT DISTINCT age
FROM titanic_test_data

"""
titanic_df["age"].unique()


"""
SELECT COUNT(DISTINCT age)
FROM titanic_test_data

"""
len(titanic_df["age"].unique())


# SELECT, WHERE, OR, AND, IN
"""
SELECT *
FROM titanic_test_data
WHERE pclass = 1
"""
titanic_df[titanic_df.pclass == 1]


"""
SELECT *
FROM titanic_test_data
WHERE pclass = 1
OR pclass = 2
"""
titanic_df[(titanic_df.pclass == 1) | (titanic_df.pclass == 2) ]



"""
SELECT *
FROM titanic_test_data
WHERE pclass IN (1,2)
"""
titanic_df[titanic_df.pclass.isin([1,2])]


"""
SELECT name
FROM titanic_test_data
WHERE pclass = 1 
AND gender = "male"
"""
titanic_df[(titanic_df.pclass == 1) & (titanic_df.gender == "male")]["name"] 


"""
SELECT name, age
FROM titanic_test_data
WHERE pclass NOT IN (1,2)
"""
titanic_df[~titanic_df.pclass.isin([1,2])][["name","age"]]



# GROUP BY, ORDER BY, COUNT, SUM
"""
SELECT
pclass,
gender,
COUNT(*)
FROM titanic_test_data
GROUP BY 1,2
"""
titanic_df.groupby(["pclass","gender"]).size()


"""
SELECT
pclass,
gender,
COUNT(*)
FROM titanic_test_data
GROUP BY 1,2
ORDER BY 3 DESC
"""
titanic_df.groupby(["pclass","gender"]).size().sort_values(ascending=False) 


"""
SELECT
name,
pclass,
gender
FROM titanic_test_data
ORDER BY 1, 2 DESC
"""
titanic_df.sort_values(["name","pclass"],ascending=[True,False])[["name","pclass","gender"]] 

"""
SELECT
pclass,
gender,
SUM(fare)
FROM titanic_test_data
GROUP BY 1,2
"""
titanic_df.groupby(["pclass","gender"]).sum()["fare"]


# MIN, MAX, MEAN, MEDIAN

"""
SELECT
MIN(age),
MAX(age),
AVG(age),
MEDIAN(age)
FROM titanic_test_data
"""
titanic_df.agg({'age': ['min', 'max', 'mean', 'median']})