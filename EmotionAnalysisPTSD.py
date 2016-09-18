
"""
Stress Radar -
Uses emotion analysis (by Alchemy) of Yelp reviews, and open crime data to identify places that might trigger PTSD.
Needs an api key to run Alchemy

Author     : Shamya Karumbaiah
Date       : 09/16/2016
Venue      : Hack The North, 2016, University of Waterloo
Dataset    : https://www.yelp.com/dataset_challenge
Publish at : http://devpost.com/software/hackthenorth2016-3xg5le

"""

import json, csv
from watson_developer_cloud import AlchemyLanguageV1 #use Alchemy from Watson Developer Cloud
alchemy_language = AlchemyLanguageV1(api_key='API_KEY') #Needs an api key to run Alchemy

yelp_data= []

#download dataset - yelp.com/dataset_challenge
#read yelp business data that gives the information about 85539 businesses
#has one record for most of the business referenced in the review 
for line in open('yelp_academic_dataset_business.json', 'r'):
     yelp_data.append(json.loads(line))
        
yelp_biz= []

#pick a subset of the business 
#condition used - city "Las Vegas", neighborhood "The Strip" and minimum review count > 50
for line in yelp_data:
    if line['city'] == 'Las Vegas' and 'The Strip' in line['neighborhoods'] and line['review_count'] > 50:
         yelp_biz.append(line)

#output the data out into a json if needed
'''
with open("biz_vegas.json", 'w') as f:
    for js in yelp_biz:
        f.write(json.dumps(js))
        f.write('\n')
'''    
print('Number of business',len(yelp_biz))  

#Yelp reviews - total of around 2M user reviews
#combines different user reviews of a single business into one string
yelp_review = {}
for line in open('yelp_academic_dataset_review.json', 'r'):
    js_line = json.loads(line)
    if js_line["business_id"] not in yelp_review:
        yelp_review[js_line["business_id"]] = js_line["text"]
    else:
        yelp_review[js_line["business_id"]] = yelp_review[js_line["business_id"]] + ' ' + js_line["text"]

print('Number of combined reviews',len(yelp_biz))  

#for each business find the emotion        
for biz_entry in yelp_biz:  
    #call alchemy's emotion analysis API 
    #documentation - http://www.ibm.com/watson/developercloud/alchemy-language/api/v1/#emotion_analysis
    d = alchemy_language.emotion(yelp_review[biz_entry['business_id']])
    biz_entry['fear'] = d['docEmotions']['fear'] #the most important feature for PTSD trigger
    biz_entry['anger'] = d['docEmotions']['anger']
    biz_entry['disgust'] = d['docEmotions']['disgust']
    biz_entry['joy'] = d['docEmotions']['joy']
    biz_entry['sadness'] = d['docEmotions']['sadness']
    
#output data to a json file to be confused to plot in a google map
with open("biz_score_alchemy_vegas.json", 'w') as f:
    for js in yelp_biz:
        f.write(json.dumps(js))
        f.write('\n')