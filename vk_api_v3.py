# -*- coding: utf-8 -*-
"""
Чтобы получить access_token, посмотри видео по ссылке:
https://youtu.be/nbqRFxSw_RI?list=PLPRsICSqu9Fp8v5Os1UU8QcSuRaN5efGf
Вставь access_token в кавычки переменную ниже
"""
access_token = ''
# ID сообщества идет в переменную ниже, как его узнать, можно посмотреть
# в видео на канале. Вставлять нужно со знаком дефиса
owner_id = '-143503361'


import requests #for sending requests to api
import time # for making delays in requests
import datetime # to convert the date from timestamp
import csv # to export the information to csv

def getjson(url, data = None):
    response = requests.get(url, params = data)
    print(response.url, '\n')
    return response.json()

def get_all_posts (access_token, owner_id, count = 100, offset=0):
    """takes access_token, owner_id (group_id), count (default=100), offset
    (default=0) and returns all posts from vk group in a list of dictionaries
    and the number of posts in second variable"""
    all_posts = []
    
    while True:
        time.sleep(1)
        wall = getjson("https://api.vk.com/method/wall.get", {
            'owner_id' : owner_id, 
            'count' : count,
            'access_token' : access_token,
            'offset' : offset,
            'v' : '5.65'
            })
        
        count_posts = wall['response']['count']
        posts = wall['response']['items']
        
        all_posts.extend(posts)
        
        if len(all_posts) >= count_posts:
            break
        else:
            offset += 100
    return all_posts, count_posts

def make_posts(all_posts):
    """Takes in a list of dictionaries with posts, converts the data in 
    a new structure and returns a new list of dictionaries with the posts"""
    filtered_data = []
    for post in all_posts:
        
        try:
            id = post['id']
        except:
            id = 0
            
        try:
            owner_id = str(post['owner_id'])[1:]
        except:
            owner_id = ''
            
        try:
            link = 'https://vk.com/wall-{owner_id}_{id}'.format(owner_id = owner_id, id = id)
        except:
            link = ''
            
        try:
            date = datetime.datetime.fromtimestamp(int(post['date'])).strftime('%d-%m-%Y')
        except:
            date = ''
        
        try:
            day = datetime.datetime.fromtimestamp(int(post['date'])).strftime('%d')
        except:
            day = ''
        try:
            month = datetime.datetime.fromtimestamp(int(post['date'])).strftime('%B')
        except:
            month = ''
            
        try:
            year = datetime.datetime.fromtimestamp(int(post['date'])).strftime('%Y')
        except:
            year = ''

        try:
            weekday = datetime.datetime.fromtimestamp(int(post['date'])).strftime('%A')
        except:
            weekday = ''

        try:
            time = datetime.datetime.fromtimestamp(int(post['date'])).strftime('%H')
        except:
            time = ''
            
#        try:
#            timestamp = post['date']
#        except:
#            timestamp = ''
            
        try:
            likes = post['likes']['count']
        except:
            likes = 0
            
        try:
            reposts = post['reposts']['count']
        except:
            reposts = 0
            
        try:
            comments = post['comments']['count']
        except:
            comments = 0
            
        try:
            views = post['views']['count']
        except:
            views = 0
            
        try:
            text = post['text']
        except:
            text = ''
        
        photos = []
        videos = []
        docs = []
        
        try:
            attachments = post['attachments']
            
            if attachments:
                
                for att in attachments:
                    if att['type'] == 'video':
                        video_title = att['video']['title']
                        video_owner_id = str(att['video']['owner_id'])[1:]
                        video_id = att['video']['id']
                        video_url ='https://vk.com/video-{}_{}'.format(video_owner_id, video_id)
                        videos.append({video_title : video_url})

                    if att['type'] == 'photo':
                        photo_id = att['photo']['id']
                        photo_owner_id = str(att['photo']['owner_id'])[1:]
                        photo_url = 'https://vk.com/photo-{}_{}'.format(photo_owner_id, photo_id)
                        photos.append(photo_url)
                        
                    if att['type'] == 'doc':
                        doc_url = att['doc']['url']
                        doc_title = att['doc']['title']
                        docs.append({doc_title : doc_url})

        except:
            attachments = ''
            
        if len(photos) == 0:
            photos = ''
        if len(videos) == 0:
            videos = ''
        if len(docs) == 0:
            docs = ''
            
        filtered_post = {
                'id' : id,
                'date' : date,
                'year' : year,
                'month' : month,
                'day' : day,
                'weekday' : weekday,
                'time' : time,
#                'timestamp' : timestamp,
                'likes' : likes,
                'reposts' : reposts,
                'comments' : comments,
                'views' : views, 
                'text' : str(text),
                'photos' : photos,
                'videos' : videos,
                'docs' : docs,
                'link' : link,
                'group_id' : owner_id,
                }
        
        
        filtered_data.append(filtered_post)
    
    return filtered_data
    

def write_csv(data, encoding = 'utf-8'):
    """Recieves data as list of dictionaries, the file name as a string ('*.csv'),
    encoding (default = utf-8), returns csv file
    """
    owner_id = data[0]['group_id']
    filename = '{owner_id}-{datetime}.csv'.format(owner_id = owner_id, datetime= str(datetime.datetime.now())[:10] )
    with open(filename, 'w', newline = '', encoding = encoding) as csvfile:
        fieldnames = ['id','date','year','month','day', 'weekday', 'time',
                      'likes', 'reposts', 'views', 'comments', 'text', 
                      'photos', 'videos', 'docs', 'link']
        
        writer = csv.DictWriter(csvfile, delimiter = ';', fieldnames = fieldnames, extrasaction = 'ignore')
        writer.writeheader()
        writer.writerows(data)
        
        print ('Data written to csv', filename)
    csvfile.close

all_posts, count_posts = get_all_posts (access_token, owner_id)

pposts = make_posts(all_posts)

write_csv(pposts)


































