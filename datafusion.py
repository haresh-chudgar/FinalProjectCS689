__author__ = 'haresh'

import time
import datetime
import csv

numberOfMovies = 17770
movieRatings = []
movieInfo = {}
with open('data\movie_titles.txt', mode='r') as infile:
    reader = csv.reader(infile)
    movieInfo = dict((rows[0],rows[1]) for rows in reader)

for currentMovie in range(1,numberOfMovies + 1):
    filePath = 'data/training_set/mv_%07d.txt' % currentMovie
    with open(filePath) as movieFile:
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
                if(splitStrings[2] == "NULL"):
                    dateOfRating = -1
                else:
                    dateOfRating = int(time.mktime(datetime.datetime.strptime(splitStrings[2], "%Y-%m-%d").timetuple()))
                mId = currentMovie.__str__()
                if(movieInfo[currentMovie.__str__()] == "NULL"):
                    dateOfRelease = -1
                else:
                    dateOfRelease = int(movieInfo[currentMovie.__str__()])
                movieRatings.append([currentMovie, userId, userRating, dateOfRating, dateOfRelease])
    print(filePath, movieRatings.__len__())
    if(currentMovie % 1000 == 0 or currentMovie == numberOfMovies):
        with open("consolidatedRatings_" + currentMovie.__str__() +  ".csv", "wb") as csvFile:
            writer = csv.writer(csvFile,delimiter=',')
            writer.writerows(movieRatings)