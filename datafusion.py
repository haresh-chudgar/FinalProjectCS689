__author__ = 'haresh'

import time
import datetime
import os
import csv
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.cross_validation import cross_val_score
from patsy import dmatrices

numberOfMovies = 10
movieRatings = []
movieInfo = {}
with open('data\movie_titles.txt', mode='r') as infile:
    reader = csv.reader(infile)
    movieInfo = dict((rows[0],rows[1]) for rows in reader)

for subdir, dirs, files in os.walk("data/training_set"):
    for filePath in files:
        with open(os.path.join(subdir, filePath)) as movieFile:
            currentMovie = 0
            for line in movieFile:
                if(line.__contains__(":")):
                    splitStrings = line.split(":")
                    currentMovie = int(splitStrings[0])
                else:
                    splitStrings = line.split(",")
                    userId = int(splitStrings[0])
                    userRating = int(splitStrings[1])
                    splitStrings[2] = splitStrings[2].split("\n")[0]
                    dateOfRating = int(time.mktime(datetime.datetime.strptime(splitStrings[2], "%Y-%m-%d").timetuple()))
                    mId = currentMovie.__str__()
                    dateOfRelease = int(movieInfo[currentMovie.__str__()])
                    movieRatings.append([currentMovie, userId, userRating, dateOfRating, dateOfRelease])

with open("consolidatedRatings.csv", "wb") as csvFile:
    writer = csv.writer(csvFile,delimiter=',')
    writer.writerows(movieRatings)

df_ = pd.DataFrame(movieRatings, columns=['movieid', 'userid', 'rating', 'ratingdate', 'releasedate'])
y, X = dmatrices('rating ~ movieid + userid + ratingdate + releasedate', df_, return_type="dataframe")
print(X)
print(y)



