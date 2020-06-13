import calendar

import numpy
import numpy as np
from dateutil.relativedelta import relativedelta
from moviedatareader import csv_dict_reader
from datetime import datetime
from constants import getQuestionDictList
from constants import getValues
import matplotlib.pyplot as plt

DASH_LENGTH = 250
#Daekyung Kim 110887867 CSE_216
def userDateInput(first_date, last_date):
    print("Available date interval is from: ", first_date, "till", last_date)
    validity = True
    while(validity):
        validity = False;
        try:
            ufDate = input("Enter valid interval start date in the format YYYY-MM-DD: ")
            fDate = datetime.strptime(ufDate, "%Y-%m-%d").date()

        except ValueError:
            print("Invalid Date Format, Try again")
            validity = True

    while fDate.year <1900 or fDate.year>2020 or (fDate.year ==2020 and fDate.month == 12 and fDate.day>16):
        print("Invalid interval date. Try again.")
        ufDate = input("Enter valid interval start date in the format YYYY-MM-DD: ")
        fDate = datetime.strptime(ufDate, "%Y-%m-%d").date()

    validity=True
    while (validity):
        validity = False;
        try:
            ulDate = input("Enter valid interval end date in the format YYYY-MM-DD: ")
            lDate = datetime.strptime(ulDate, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid Date Format, Try again")
            validity = True

    while (lDate.year < fDate.year) or (lDate.year == fDate.year and lDate.month < fDate.month) or (lDate.year == fDate.year and lDate.month == fDate.month and lDate.day< fDate.day) or (lDate.year >2020) or (lDate.year==2020 and lDate.month==12 and lDate.day>16) :
        print("It's not within valid interval. Try again.")
        ulDate = input("Enter valid interval end date in the format YYYY-MM-DD: ")
        lDate = datetime.strptime(ulDate, "%Y-%m-%d").date()
    print("You entered: ", fDate, " - ", lDate)
    return fDate, lDate

def userQuestionInput(qDictList):
    print("Available questions are: ")
    for item in qDictList:
        print(item['num'], ": ", item['question'])
    qnum = input("Select the number of any of the above question. ")
    return qnum

def sortByPopularity(data):
    data.sort(key=lambda item: item['Popularity'], reverse = True)
    return data

def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month


def q1(byDateMovieItems):    # "Number of movies released per month in a particular period." (bar chart)
    months = []

    MoviesByMonthList =[]
    current = fDate
    while current.year<lDate.year or (current.year==lDate.year and current.month<=lDate.month):
        MoviesByMonthList.append(0)

        months.append(str(current.month) +"/" +str(current.year))
        current = current + relativedelta(months=1)

    #MoviesByMonthList.remove([]); #some random empty... list in the first index..
    for movie in byDateMovieItems:
        c= datetime.strptime(str(movie['date']), '%Y-%m-%d')
        dif =  diff_month(c,fDate)
        if(dif <= len(MoviesByMonthList)):
            MoviesByMonthList[abs(dif)]+=1


    answ = dict(zip(months,MoviesByMonthList))
    print(answ)

    numbMovies = MoviesByMonthList
    index = np.arange(len(months))

    plt.barh(index, numbMovies, align='center',color = 'green')
    plt.yticks(index,months)
    plt.title("Number of Movies Released Per Month During "+ fDate.__str__() + " and " +lDate.__str__())
    plt.xlabel("Number of Movies")
    plt.ylabel("Months")
    plt.show()

    return "1"

def q2a(byDateMovieItems):

    temp =byDateMovieItems
    finalList =[]
    temp =sortByPopularity(temp)
    size=-1
    if (len(temp) < 20):
        size = len(temp)
    else:
        size = 20
    for i in range(size):
        finalList.append(temp[i])

    index = np.arange(len(finalList))
    popularity =[]
    for m in finalList:
        popularity.append(m['Popularity'])
    titles = []
    for t in finalList:
        titles.append(t['Movie Title'])
    plt.barh(index, popularity, align='center', color='green')
    plt.yticks(index, titles,fontsize=7)
    plt.title("Most Popular Movies During " + fDate.__str__() + " and " + lDate.__str__())
    plt.xlabel("Popularity")
    plt.ylabel("Movies")
    plt.show()
    return "2a"

def q2b(byDateMovieItems):
    langList =["Available languages are:",
                "ab","af","am","ar","ay","bg","bm","bn","bo","bs","ca","cn","cs","cy","da","de","el","en","eo","es","et","eu","fa","fi",
                "fr","fy","gl","he","hi","hr","hu","hy","id","is","it","iu","ja","jv","ka","kk","kn","ko","ku","ky","la","lb","lo","lt",
                "lv","mk","ml","mn","mr","ms","mt","nb","ne","nl","no","pa","pl","ps","pt","qu","ro","ru","rw","sh","si","sk","sl","sm",
                "sq","sr","sv","ta","te","tg","th","tl","tr","uk","ur","uz","vi","wo","xx","zh","zu"]
    for l in langList:
        print(l)
    userLang = input("Type any Language Code from above list: ")
    while userLang not in langList:
        print("Invalid Language Code, Try Again.")
        userLang = input("Type any Language Code above list: ")

    userLangList =[]
    for movie in byDateMovieItems:
        if(userLang == movie['Movie Language']):
            userLangList.append(movie)
    userLangList = sortByPopularity(userLangList)
    finalList=[]
    size=-1
    if (len(userLangList) < 20):
        size = len(userLangList)
    else:
        size = 20
    for i in range(size):
        finalList.append(userLangList[i])

    index = np.arange(len(finalList))
    popularity =[]
    for m in finalList:
        popularity.append(m['Popularity'])
    titles = []
    for t in finalList:
        titles.append(t['Movie Title'])
    plt.barh(index, popularity, align='center', color='green')
    plt.yticks(index, titles,fontsize=7)
    plt.title("Most Popular Movies Released in Language ["+ userLang+"] During " + fDate.__str__() + " and " + lDate.__str__())
    plt.xlabel("Popularity")
    plt.ylabel("Movies")
    plt.show()
    return "2b"



def q2c(byDateMovieItems):
    genreListQ = ["Available genres are:", "Action, ""Adventure", "Animation",
                  "Comedy", "Crime", "Documentary", "Drama", "Family", "Fantasy", "Foreign", "History", "Horror",
                  "Music", "Mystery", "Romance", "Science Fiction", "TV Movie", "Thriller", "War", "Western"]
    for g in genreListQ:
        print(g)
    userGenre = input("Type any genre from above list: ")
    while userGenre not in genreListQ:
        print("Invalid Genre, Try Again.")
        userGenre = input("Type any genre from above list: ")

    userGenreList = []
    for movie in byDateMovieItems:
        if userGenre in movie['Genres']:
            userGenreList.append(movie)
    userGenreList = sortByPopularity(userGenreList)
    finalList=[]
    size=-1
    if (len(userGenreList) < 20):
        size = len(userGenreList)
    else:
        size = 20
    for i in range(size):
        finalList.append(userGenreList[i])


    index = np.arange(len(finalList))
    popularity =[]
    for m in finalList:
        popularity.append(m['Popularity'])
    titles = []
    for t in finalList:
        titles.append(t['Movie Title'])
    plt.barh(index, popularity, align='center', color='green')
    plt.yticks(index, titles,fontsize=7)
    plt.title("Most Popular Movies Released in Genre [" + userGenre+"] During " + fDate.__str__() + " and " + lDate.__str__())
    plt.xlabel("Popularity")
    plt.ylabel("Movies")
    plt.show()
    return "2c"



def q2d(byDateMovieItems):
    countryList = [ "Available countries are:", # sooo much pain
                    "AE","AF","AL","AM","AN","AO","AQ","AR","AT","AU","AW","AZ","BA","BB","BD","BE","BF","BG","BM","BN","BO","BR","BS","BT","BW",
                    "BY","CA","CD","CG","CH","CI","CL","CM","CN","CO","CR","CS","CU","CY","CZ","DE","DK","DO","DZ","EC","EE","EG","ES","ET","FI",
                    "FR","GB","GE","GH","GI","GN","GR","GT","HK","HN","HR","HU","ID","IE","IL","IN","IQ","IR","IS","IT","JM","JO","JP""KE","KG",
                    "KH","KP","KR","KW","KY","KZ","LA","LB","LI","LK","LR","LT","LU","LV","LY","MA","MC","MD","ME","MG","MK","ML","MM","MN","MO",
                    "MQ","MR","MT","MX","MY","NA","NG","NI","NL","NO","NP","NZ","PA","PE","PF","PG","PH","PK","PL","PR","PS","PT","PY","QA","RO",
                    "RS","RU","RW","SA","SE","SG","SI","SK","SN","SO","SU","SV","SY","TD","TF","TH","TJ","TN","TR","TT","TW","TZ","UA","UG","UM",
                    "US","UY","UZ","VE","VN","WS","XC","XG","YU","ZA","ZW"]
    for c in countryList:
        print(c)
    userCountry = input("Type any country code above list: ")
    while userCountry not in countryList:
        print("Invalid Country Code, Try Again.")
        userCountry = input("Type any country code above list: ")

    userCountryList =[]

    for movie in byDateMovieItems:
        if userCountry in movie['Production Countries']:
            userCountryList.append(movie)
    userCountryList = sortByPopularity(userCountryList)
    finalList=[]
    size=-1
    if(len(userCountryList)<20):
        size = len(userCountryList)
    else:
        size = 20
    for i in range(size):
        finalList.append(userCountryList[i])


    index = np.arange(len(finalList))
    popularity =[]
    for m in finalList:
        popularity.append(m['Popularity'])
    titles = []
    for t in finalList:
        titles.append(t['Movie Title'])
    plt.barh(index, popularity, align='center', color='green')
    plt.yticks(index, titles,fontsize=7)
    plt.title("Most Popular Movies Released in Country ["+userCountry+"] During " + fDate.__str__() + " and " + lDate.__str__())
    plt.xlabel("Popularity")
    plt.ylabel("Movies")
    plt.show()
    return "2d"


def q3a(byDateMovieItems):
    temp=byDateMovieItems
    finalList =[]
    temp.sort(key=lambda item: item['Revenue'], reverse = True)
    size=-1
    if (len(temp) < 20):
        size = len(temp)
    else:
        size = 20
    for i in range(size):
        finalList.append(temp[i])

    index = np.arange(len(finalList))
    Revenue =[]
    for m in finalList:
        Revenue.append(m['Revenue'])
    titles = []
    for t in finalList:
        titles.append(t['Movie Title'])
    plt.barh(index, Revenue, align='center', color='green')
    plt.yticks(index, titles,fontsize=7)
    plt.title("Most Earning Movies During " + fDate.__str__() + " and " + lDate.__str__())
    plt.xlabel("Revenue")
    plt.ylabel("Movies")
    plt.show()
    return "3a"

    return finalList


def q3b(byDateMovieItems):
    langList = ["Available languages are:",
                "ab", "af", "am", "ar", "ay", "bg", "bm", "bn", "bo", "bs", "ca", "cn", "cs", "cy", "da", "de", "el",
                "en", "eo", "es", "et", "eu", "fa", "fi",
                "fr", "fy", "gl", "he", "hi", "hr", "hu", "hy", "id", "is", "it", "iu", "ja", "jv", "ka", "kk", "kn",
                "ko", "ku", "ky", "la", "lb", "lo", "lt",
                "lv", "mk", "ml", "mn", "mr", "ms", "mt", "nb", "ne", "nl", "no", "pa", "pl", "ps", "pt", "qu", "ro",
                "ru", "rw", "sh", "si", "sk", "sl", "sm",
                "sq", "sr", "sv", "ta", "te", "tg", "th", "tl", "tr", "uk", "ur", "uz", "vi", "wo", "xx", "zh", "zu"]
    for l in langList:
        print(l)
    userLang = input("Type any Language Code from above list: ")
    while userLang not in langList:
        print("Invalid Language Code, Try Again.")
        userLang = input("Type any Language Code above list: ")

    userLangList = []
    for movie in byDateMovieItems:
        if (userLang == movie['Movie Language']):
            userLangList.append(movie)
    userLangList.sort(key=lambda item: item['Revenue'], reverse = True)
    finalList = []
    size = -1
    if (len(userLangList) < 20):
        size = len(userLangList)
    else:
        size = 20
    for i in range(size):
        finalList.append(userLangList[i])

    index = np.arange(len(finalList))
    Revenue = []
    for m in finalList:
        Revenue.append(m['Revenue'])
    titles = []
    for t in finalList:
        titles.append(t['Movie Title'])
    plt.barh(index, Revenue, align='center', color='green')
    plt.yticks(index, titles, fontsize=7)
    plt.title(
        "Most Earning Movies Released in Language [" + userLang + "] During " + fDate.__str__() + " and " + lDate.__str__())
    plt.xlabel("Revenue")
    plt.ylabel("Movies")
    plt.show()
    return "3b"

def q3c(byDateMovieItem):
    genreListQ = ["Available genres are:", "Action""Adventure", "Animation",
                  "Comedy", "Crime", "Documentary", "Drama", "Family", "Fantasy", "Foreign", "History", "Horror",
                  "Music", "Mystery", "Romance", "Science Fiction", "TV Movie", "Thriller", "War", "Western"]
    for g in genreListQ:
        print(g)
    userGenre = input("Type any genre from above list: ")
    while userGenre not in genreListQ:
        print("Invalid Genre, Try Again.")
        userGenre = input("Type any genre from above list: ")

    userGenreList = []
    for movie in byDateMovieItems:
        if userGenre in movie['Genres']:
            userGenreList.append(movie)
    userGenreList.sort(key=lambda item: item['Revenue'], reverse = True)
    finalList = []
    size = -1
    if (len(userGenreList) < 20):
        size = len(userGenreList)
    else:
        size = 20
    for i in range(size):
        finalList.append(userGenreList[i])

    index = np.arange(len(finalList))
    Revenue = []
    for m in finalList:
        Revenue.append(m['Revenue'])
    titles = []
    for t in finalList:
        titles.append(t['Movie Title'])
    plt.barh(index, Revenue, align='center', color='green')
    plt.yticks(index, titles, fontsize=7)
    plt.title(
        "Most Revenue Movies Released in Genre [" + userGenre + "] During " + fDate.__str__() + " and " + lDate.__str__())
    plt.xlabel("Revenue")
    plt.ylabel("Movies")
    plt.show()
    return "3c"

def q3d(byDateMoviesItem):
    countryList = ["Available countries are:",  # sooo much pain
                   "AE", "AF", "AL", "AM", "AN", "AO", "AQ", "AR", "AT", "AU", "AW", "AZ", "BA", "BB", "BD", "BE", "BF",
                   "BG", "BM", "BN", "BO", "BR", "BS", "BT", "BW",
                   "BY", "CA", "CD", "CG", "CH", "CI", "CL", "CM", "CN", "CO", "CR", "CS", "CU", "CY", "CZ", "DE", "DK",
                   "DO", "DZ", "EC", "EE", "EG", "ES", "ET", "FI",
                   "FR", "GB", "GE", "GH", "GI", "GN", "GR", "GT", "HK", "HN", "HR", "HU", "ID", "IE", "IL", "IN", "IQ",
                   "IR", "IS", "IT", "JM", "JO", "JP""KE", "KG",
                   "KH", "KP", "KR", "KW", "KY", "KZ", "LA", "LB", "LI", "LK", "LR", "LT", "LU", "LV", "LY", "MA", "MC",
                   "MD", "ME", "MG", "MK", "ML", "MM", "MN", "MO",
                   "MQ", "MR", "MT", "MX", "MY", "NA", "NG", "NI", "NL", "NO", "NP", "NZ", "PA", "PE", "PF", "PG", "PH",
                   "PK", "PL", "PR", "PS", "PT", "PY", "QA", "RO",
                   "RS", "RU", "RW", "SA", "SE", "SG", "SI", "SK", "SN", "SO", "SU", "SV", "SY", "TD", "TF", "TH", "TJ",
                   "TN", "TR", "TT", "TW", "TZ", "UA", "UG", "UM",
                   "US", "UY", "UZ", "VE", "VN", "WS", "XC", "XG", "YU", "ZA", "ZW"]
    for c in countryList:
        print(c)
    userCountry = input("Type any country code above list: ")
    while userCountry not in countryList:
        print("Invalid Country Code, Try Again.")
        userCountry = input("Type any country code above list: ")

    userCountryList = []

    for movie in byDateMovieItems:
        if userCountry in movie['Production Countries']:
            userCountryList.append(movie)
    userCountryList.sort(key=lambda item: item['Revenue'], reverse = True)
    finalList = []
    size = -1
    if (len(userCountryList) < 20):
        size = len(userCountryList)
    else:
        size = 20
    for i in range(size):
        finalList.append(userCountryList[i])

    index = np.arange(len(finalList))
    Revenue = []
    for m in finalList:
        Revenue.append(m['Revenue'])
    titles = []
    for t in finalList:
        titles.append(t['Movie Title'])
    plt.barh(index, Revenue, align='center', color='green')
    plt.yticks(index, titles, fontsize=7)
    plt.title(
        "Most Earning Movies Released in Country [" + userCountry + "] During " + fDate.__str__() + " and " + lDate.__str__())
    plt.xlabel("Revenue")
    plt.ylabel("Movies")
    plt.show()
    return "3d"

def q4a(byDateMovieItems):

    moviesLang=[]
    numberMoviesOfLang =[]
    for m in byDateMovieItems:
        if m['Movie Language'] not in moviesLang:
            moviesLang.append((m['Movie Language']))
            numberMoviesOfLang.append(0)
    for m in byDateMovieItems:
        if m['Movie Language'] in moviesLang:
            numberMoviesOfLang[moviesLang.index(m['Movie Language'])]+=1

    answ = dict(zip(moviesLang,numberMoviesOfLang))
    print(answ)

    plt.pie(numberMoviesOfLang,labels=moviesLang)
    plt.axis('equal')
    plt.title("Number of Movies Produced Per Language")
    plt.tight_layout()
    plt.show()

    return "4a"

def q4b(byDateMovieItems): #PROBLEM
    genreList = ["Available genres are:", "Action","Adventure", "Animation",
                  "Comedy", "Crime", "Documentary", "Drama", "Family", "Fantasy", "Foreign", "History", "Horror",
                  "Music", "Mystery", "Romance", "Science Fiction", "TV Movie", "Thriller", "War", "Western"]

    moviesGenre=[]
    numberMoviesOfGenre =[]
    for m in byDateMovieItems:
        for g in getValues(m['Genres']):
            if g in genreList and g not in moviesGenre:
                moviesGenre.append(g)
                numberMoviesOfGenre.append(0)
    for m in byDateMovieItems:
        for g in getValues(m['Genres']):
            if  g in moviesGenre and g in genreList:
                numberMoviesOfGenre[moviesGenre.index(g)]+=1

    answ = dict(zip(moviesGenre,numberMoviesOfGenre))
    print(answ)

    plt.pie(numberMoviesOfGenre,labels=moviesGenre)
    plt.axis('equal')
    plt.title("Number of Movies Produced Per Genre")
    plt.tight_layout()
    plt.show()
    return "4b"


def q4c(byDateMovieItems):  #PROBLEM
    moviesCountry = []
    numberMoviesOfCountry = []
    for m in byDateMovieItems:
        for c in getValues(m['Production Countries']):
            if c not in moviesCountry:
                moviesCountry.append(c)
                numberMoviesOfCountry.append(0)
    for m in byDateMovieItems:
        for c in getValues(m['Production Countries']):
            if c in moviesCountry:
                numberMoviesOfCountry[moviesCountry.index(c)] += 1

    answ = dict(zip(moviesCountry, numberMoviesOfCountry))
    print(answ)

    plt.pie(numberMoviesOfCountry, labels=moviesCountry)
    plt.axis('equal')
    plt.title("Number of Movies Produced Per Country")
    plt.tight_layout()
    plt.show()

    return "4c"

if __name__ == "__main__":
    f_obj = open("movies_metadata_edited.csv", encoding="utf8")
    movieItems = csv_dict_reader(f_obj)
    qDictList = getQuestionDictList()
    print("First date: ", movieItems[0]['date'])
    print("Last date: ", movieItems[-1]['date'])

    contFlag = True
    while contFlag:
        fDate, lDate = userDateInput(movieItems[0]['date'], movieItems[-1]['date'])
        byDateMovieItems = []
        for movies in movieItems:
            if (movies['date']>= fDate and movies['date']<=lDate):
                byDateMovieItems.append(movies)
        if(len(byDateMovieItems)==0):
            print("No movies found within the given date interval.")
        else:##do everything within the else statement.
            questionValid = True
            while questionValid:
                qNum = userQuestionInput(qDictList)
                questionValid = False
                if qNum.__eq__("1"):             ##
                    q1(byDateMovieItems)
                elif qNum.__eq__("2a"):          ##
                    q2a(byDateMovieItems)
                elif qNum.__eq__("2b"):          ##
                    q2b(byDateMovieItems)
                elif qNum.__eq__("2c"):          ##
                    q2c(byDateMovieItems)
                elif qNum.__eq__("2d"):          ##
                    q2d(byDateMovieItems)
                elif qNum.__eq__("3a"):          ##
                    q3a(byDateMovieItems)
                elif qNum.__eq__("3b"):          ##
                    q3b(byDateMovieItems)
                elif qNum.__eq__("3c"):          ##
                    q3c(byDateMovieItems)
                elif qNum.__eq__("3d"):          ##
                    q3d(byDateMovieItems)
                elif qNum.__eq__("4a"):          ##
                    q4a(byDateMovieItems)
                elif qNum.__eq__("4b"):          ##
                    q4b(byDateMovieItems)
                elif qNum.__eq__("4c"):          ##
                    q4c(byDateMovieItems)
                else:
                    print("Wrong Question Input. Try Again.")
                    questionValid = True

        repeat = True
        while(repeat):
            repeat = False
            uChoice: str = input("Enter [Y/N] to continue: ")
            if 'N' in uChoice or 'n' in uChoice:
                print("Thank you. Exiting!!")
                exit()
                contFlag = False
            elif 'Y' in uChoice or 'y' in uChoice:
                pass
            else:
                print("Invalid Input.")
                repeat= True
