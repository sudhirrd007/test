import shutil
import os
import pandas as pd


ROOT = os.getcwd()
NEWFILES_PATH = "{}/New_Files".format(ROOT)
TOPIC_PATH = "{}/Topics".format(ROOT)


files = os.listdir(NEWFILES_PATH)

for file in files:
    main = {}
    
    Obj = open("{}/{}".format(NEWFILES_PATH, file), "r")
    fileName = Obj.readline()
    fileName = fileName[2:-1].split(", ")
    fileName = fileName[1]
    for i in range(7):
        string = Obj.readline()
        string = string[2:-1].split(", ")
        if(i != 6):
            main[string[0]] = string[1]
        else:
            topics = string[1:]
    
    for topic in topics:
        topicFileName = "{}/{}.csv".format(TOPIC_PATH, topic)
        if(os.path.isfile(topicFileName)):
            df = pd.read_csv(topicFileName)
            df = df.append(main, ignore_index=True)
        else:
            print("ERROR: NOT FOUND !!!!!!!!! ==>", topicFileName)
            topic = input("TYPE NAME MANUALLY :")
            df = pd.read_csv("{}/{}.csv".format(TOPIC_PATH, topic))
            df = df.append(main, ignore_index=True)
        df.to_csv("{}/{}.csv".format(TOPIC_PATH, topic), index=False)
    
    Obj.close()
    
    folderName = main["Difficulty"]

    source = "{}/{}".format(NEWFILES_PATH, fileName)
    destination = "{}/{}".format(folderName, fileName)
    
    shutil.move(source, destination)
    
print("PROCESS FINISHED :)")
