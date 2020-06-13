import ast,string

questionList = ["Number of movies released per month in a particular period. ",
    "Most popular top 20 movies in a particular period.",
    "Most popular top 20 movies released in a particular language.",
    "List most popular top 20 movies released in a particular genre type.",
    "List most popular top 20 movies produced in a particular country.",
    "Top 20 highest earning movies in a particular period.",
    "Top 20 highest earning movies released in a particular language.",
    "Top 20 highest earning movies released in a particular genre type.",
    "Top 20 highest earning movies released in a particular country.",
    "Number of movies produced per language.",
    "Number of movies produced per genre tyoe",
    "Number of movies produced per country",
    ]

def getQuestionDictList():
    qDictList = []
    alphabets = string.ascii_lowercase
    for i in range(len(questionList)):
        qDict = {}
        if i ==0:
            qDict['num']="1 "
        if i ==1:
            qDict['num'] ="2a"
        elif i == 2:
            qDict['num'] ="2b"
        elif i ==3:
            qDict['num'] ="2c"
        elif i==4:
            qDict['num'] ="2d"
        elif i ==5:
            qDict['num'] ="3a"
        elif i==6:
            qDict['num'] ="3b"
        elif i == 7:
            qDict['num'] ="3c"
        elif i == 8:
            qDict['num'] ="3d"
        elif i == 9:
            qDict['num'] ="4a"
        elif i == 10:
            qDict['num'] ="4b"
        elif i == 11:
            qDict['num'] ="4c"

        qDict['question'] = questionList[i]
        qDictList.append(qDict)
    return qDictList

def getValues(val):
    if (val == "[]"):
        return []
    else:
        valItems = ast.literal_eval(val)
        valList = []
        for item in valItems:
            valList.append(item['name'])
        return valList
