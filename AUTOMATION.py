import shutil
import os
import csv
import pandas as pd


ROOT = os.getcwd()
NEWFILES_PATH = "{}/DATA/New_Files".format(ROOT)
TOPIC_PATH = "{}/DATA/Topics".format(ROOT)

def getData(number):
    with open('LeetCode_Scrapping/leetcodeDataSet.csv', 'r') as file:
        reader = csv.DictReader(file)
        for index, line in enumerate(reader):
            if(index == number-1):
                return line

def checkTopicsAvaibality(topics):
    for topic in topics:
        if(not os.path.isfile("{}/{}.csv".format(TOPIC_PATH, topic))):
            return topic
    return 1


files = os.listdir(NEWFILES_PATH)

for file in files:
    main = {}
    
    with open("{}/{}".format(NEWFILES_PATH, file), "r") as Obj:
        main["Run Time"] = Obj.readline()[2:-1]
        topics = Obj.readline()[2:-1].split(", ")
    
    number = int(file[:4])
    main.update(getData(number))
    
    checkTopics = checkTopicsAvaibality(topics)
    if(checkTopics == 1):
        for topic in topics:
            topicFileName = "{}/{}.csv".format(TOPIC_PATH, topic)
            df = pd.read_csv(topicFileName)
            df = df.append(main, ignore_index=True)
            df.to_csv(topicFileName, index=False)
    else:
        print("ERROR : ============> '{}.csv' NOT PRESENT".format(checkTopics))
        continue
    
    folderName = main["Difficulty"]

    source = "{}/{}".format(NEWFILES_PATH, file)
    destination = "{}/{}".format(folderName, file)
    
    shutil.move(source, destination)
    print("{} PROCESSED SUCCESSFULLY".format(file))
