import pymongo

client = pymongo.MongoClient("mongodb+srv://root:mjaFCaDuVWcYLybT@myfirstcluster.uaxcr.mongodb.net/?retryWrites=true&w=majority")
db = client["shakira_tickets"]
liveShows = db["live_shows"]

for show in liveShows.find():
    print(show)