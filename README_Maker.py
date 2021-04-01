def checkTopicFile(topics):
    filledFiles = []
    for topic in topics:
        with open("DATA/Topics/{}.csv".format(topic)) as Obj:
            Obj.readline()
            if(Obj.readline()):
                filledFiles.append(topic)
    return filledFiles


def topicDataExtraction(topic):
    strings = ["|  #  | Title           |   Run Time       | Difficulty    | Acceptance rate | LeetCode Link |\n",
        "|-----|---------------- |  --------------- | ------------- | ------------- | ------------- |\n"]
    with open("DATA/Topics/{}.csv".format(topic)) as Obj:
        Obj.readline()
        for line in Obj:
            tempLine = line[:-1].split(",")
            tempLine = "|  " + "   |   ".join(tempLine) + "  |\n"
            strings.append(tempLine)
    return strings



Obj = open("DATA/Index.txt", "r")

topicNames = []
for i in range(43):
    topicNames.append(Obj.readline()[:-1])
    
Obj.readline()
mainIndex = Obj.readlines()
Obj.close()


Obj = open("README.md", "w")
Obj.writelines(mainIndex)

topicNames = checkTopicFile(topicNames)

for topic in topicNames:
    Obj.write("# {}\n".format(topic))

    strings = topicDataExtraction(topic)
    for line in strings:
        Obj.write(line)
    
    Obj.write("\n\n\n")
    
Obj.close()