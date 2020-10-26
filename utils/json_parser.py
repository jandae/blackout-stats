import json
import urllib.request
import csv 
from datetime import datetime
from dateutil import parser

def urlToJson(url):
    items = {}

    with urllib.request.urlopen(url) as response:            
        items = json.loads(response.read())            
    
    posts = items[0]["posts"]

    with open('posts.json', 'w') as outfile:            
        json.dump(posts, outfile)    
        
    return formatPosts(posts)

def formatPosts(posts):
    for post in posts:                
        post["id"] = extractID(post['postUrl'])
        post["datetime"] = datetime.strptime(post['postDate'], "%Y-%m-%dT%H:%M:%S.%fZ")

        comments = post['postComments']['comments']        
        post["category"] = parseCategory(post)
        post["date"] = ""
        post["start_time"] = ""
        post["end_time"] = ""
        if post["category"] != "uncategorized":
            post_meta = parsePostMeta(post["postText"])
            post["date"] = post_meta["date"]
            post["start_time"] = post_meta["start_time"]
            post["end_time"] = post_meta["end_time"]

        post["text"] = post["postText"]
        post["ali_comment"] = findAliComment(comments)        
    return posts

def findAliComment(comments):
    ali_comment = ""

    for comment in comments:
        if comment["name"] == 'Ronald Ali Mangaliag':
            ali_comment = comment["text"]
            break     

    return ali_comment

def parseCategory(post):
    category_keywords = {
        "unscheduled":"\nUnscheduled ", 
        "scheduled":"\nScheduled", 
        "emergency":"\nEmergency",        
    }
    text = post["postText"]
    post_category = 'uncategorized'
    for category, keyword in category_keywords.items():
        if keyword in text:
            post_category = category
            break    
    
    return post_category

def parsePostMeta(text):
    date = ""
    start_time = ""
    end_time = ""

    keywords = [
        {
            "key": 1, 
            "text": "\nDATE:",
            "start_keyword": "\nTIME STARTED:",
            "end_keyword": "\nTIME RESTORED:"
        }, 
        {
            "key": 2, 
            "text": "\nDATE :",
            "start_keyword": "\nTIME STARTED:",
            "end_keyword": "\nTIME RESTORED:"
        },   
        {
            "key": 3, 
            "text": "\nDATE AND TIME STARTED:",
            "start_keyword": ""
        },          
        {
            "key": 4, 
            "text": "\nDATE/TIME:",
            "start_keyword": ""
        }                       
    ]

    for keyword in keywords:        
        if keyword["text"] in text:            
            if keyword["key"] in [1,2]:
                date = text.split(keyword["text"])[1]
                date = date.split("\n")[0].strip().upper()                      
                start_time = text.split(keyword["start_keyword"])[1]
                start_time = start_time.split("\n")[0].strip().upper() 
                end_time_arr = text.split(keyword["end_keyword"])
                if len(end_time_arr) > 1:
                    end_time = end_time_arr[1]
                    end_time = end_time.split("\n")[0].strip().upper()                 
            elif keyword["key"] == 3:
                date = text.split(keyword["text"])[1]
                date = date.split("\n")[0].strip().upper()
                date_arr = date.split(" ")                
                am_pm = date_arr.pop(len(date_arr)-1)
                time = date_arr.pop(len(date_arr)-1)
                date = " ".join(date_arr)
                start_time = time + ' ' + am_pm             
                end_time = ""                   
            elif keyword["key"] == 4:                
                date = text.split(keyword["text"])[1]
                date = date.split("\n")[0].upper()

                if " FROM " in date:
                    date_arr = date.split(" FROM ")                                    
                    date = date_arr[0].strip()
                    
                    start_time = date_arr[1].split(" TO ")[0]
                    end_time = date_arr[1].split(" TO ")[1].split("\n")[0]
                

        if type(date) is str and date:            
            date = parser.parse(date) #str to date
            date = date.date() #remove time                    
    return {
        "date": date,
        "start_time": cleanTime(start_time),
        "end_time": cleanTime(end_time)
    }

def cleanTime(time):
    ampm = ""    
    if "NN" in time:
        time = time.replace("NN", "PM")
        ampm = "PM"
    elif "AM" in time: 
        ampm = "AM"
    elif "PM" in time:
        ampm = "PM"
    else:
        return time
    
    time = time.split(ampm)[0].strip()
    return time + ' ' + ampm        

def fileToJson():    
    with open('posts.json') as f:
        posts = json.load(f)    
    return formatPosts(posts)

def extractID(url):
    story_string = "https://www.facebook.com/permalink.php?story_fbid="
    video_string = "https://www.facebook.com/benguetelectric/videos/"
    id_string = "&id=793198510733155"
    id = 0

    if story_string in url:
        url = url.replace(story_string, "")
        id = url.replace(id_string, "")        
    else:
        url = url.replace(video_string, "")
        url = url.split("/")
        id = url[1]

    return id

def writeCSV(posts):
    data_file = open('posts.csv', 'w')
    # create the csv writer object 
    csv_writer = csv.writer(data_file) 
    
    # Counter variable used for writing  
    # headers to the CSV file 
    count = 0

    for post in posts: 
        if count == 0:   
            # Writing headers of CSV file 
            header = post.keys() 
            csv_writer.writerow(header) 
            count += 1
    
        # Writing data of CSV file 
        csv_writer.writerow(post.values()) 
  
    data_file.close() 
    return 'done'

posts = urlToJson('https://api.apify.com/v2/datasets/ikL25KWvX0VkI3bgR/items?format=json')
# posts = fileToJson()
writeCSV(posts)
