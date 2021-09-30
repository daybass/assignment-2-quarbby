import pandas as pd
import numpy as np
import json
from tqdm import tqdm

before_twitter = r'C:\Users\lynne\Documents\data\linguistic_data\data_linguistic_output\Twitter_week_before_election_10_27_through_11_02.json'
after_twitter = r'C:\Users\lynne\Documents\data\linguistic_data\data_linguistic_output\Twitter_week_after_election_11_03_through_11_09.json'

before_twitter_processed = r'C:\Users\lynne\Documents\data\linguistic_data\data_linguistic_output\Twitter_week_before_election_10_27_through_11_02_processed.json'
after_twitter_processed = r'C:\Users\lynne\Documents\data\linguistic_data\data_linguistic_output\Twitter_week_after_election_11_03_through_11_09_processed.json'

bt_fh = open(before_twitter_processed, 'w')
at_fh = open(after_twitter_processed, 'w')

def sort_file(filename, filehandler):
    with open(filename) as f:
        for line in tqdm(f): 
            line_json = json.loads(line)

            data_obj = {}
            data_obj['id'] = line_json['id']
            data_obj['created_at'] = line_json['created_at']
            data_obj['text'] = line_json['text']
            data_obj['author_id'] = line_json['author_id']

            try:
                data_obj['emotion.joy'] = line_json['emotion_values']['joy']
            except:
                data_obj['emotion.joy'] = 0
            try:
                data_obj['emotion.anger'] = line_json['emotion_values']['anger']
            except:
                data_obj['emotion.anger'] = 0
            try:
                data_obj['emotion.sadness'] = line_json['emotion_values']['sadness']
            except:
                data_obj['emotion.sadness'] = 0
            try:
                data_obj['emotion.disgust'] = line_json['emotion_values']['disgust']
            except:
                data_obj['emotion.disgust'] = 0
            try:
                data_obj['emotion.fear'] = line_json['emotion_values']['fear']
            except:
                data_obj['emotion.fear'] = 0


            # time
            try:
                data_obj['liwc.focuspast'] = line_json['liwc']['categories_norm']['focuspast']
            except:
                data_obj['liwc.focuspast'] = 0
            try:
                data_obj['liwc.focuspresent'] = line_json['liwc']['categories_norm']['focuspresent']
            except:
                data_obj['liwc.focuspresent'] = 0
            try:
                data_obj['liwc.focusfuture'] = line_json['liwc']['categories_norm']['focusfuture']
            except:
                data_obj['liwc.focusfuture'] = 0

            # affective process
            try:
                data_obj['liwc.posemo'] = line_json['liwc']['categories_norm']['posemo']
            except:
                data_obj['liwc.posemo'] = 0
            try:
                data_obj['liwc.negemo'] = line_json['liwc']['categories_norm']['negemo']
            except:
                data_obj['liwc.negemo'] = 0
            try:
                data_obj['liwc.anx'] = line_json['liwc']['categories_norm']['anx']
            except:
                data_obj['liwc.anx'] = 0
            try:
                data_obj['liwc.anger'] = line_json['liwc']['categories_norm']['anger']
            except:
                data_obj['liwc.anger'] = 0
            try:
                data_obj['liwc.sad'] = line_json['liwc']['categories_norm']['sad']
            except:
                data_obj['liwc.sad'] = 0

            # social processes
            try:
                data_obj['liwc.family'] = line_json['liwc']['categories_norm']['family']
            except:
                data_obj['liwc.family'] = 0
            try:
                data_obj['liwc.friend'] = line_json['liwc']['categories_norm']['friend']
            except:
                data_obj['liwc.friend'] = 0
            try:
                data_obj['liwc.female'] = line_json['liwc']['categories_norm']['female']
            except:
                data_obj['liwc.female'] = 0
            try:
                data_obj['liwc.male'] = line_json['liwc']['categories_norm']['male']
            except:
                data_obj['liwc.male'] = 0
            try:
                data_obj['liwc.social'] = line_json['liwc']['categories_norm']['social']
            except:
                data_obj['liwc.social'] = 0         

            # drives processes
            try:
                data_obj['liwc.affliation'] = line_json['liwc']['categories_norm']['affliation']
            except:
                data_obj['liwc.affliation'] = 0
            try:
                data_obj['liwc.achieve'] = line_json['liwc']['categories_norm']['achieve']
            except:
                data_obj['liwc.achieve'] = 0
            try:
                data_obj['liwc.power'] = line_json['liwc']['categories_norm']['power']
            except:
                data_obj['liwc.power'] = 0
            try:
                data_obj['liwc.reward'] = line_json['liwc']['categories_norm']['reward']
            except:
                data_obj['liwc.reward'] = 0
            try:
                data_obj['liwc.risk'] = line_json['liwc']['categories_norm']['risk']
            except:
                data_obj['liwc.risk'] = 0 

            # Moral values
            try:
                data_obj['moral_values.FUTURE'] = line_json['liwc']['moral_values']['FUTURE']
            except:
                data_obj['moral_values.FUTURE'] = 0                      
            try:
                data_obj['moral_values.ORDER'] = line_json['liwc']['moral_values']['ORDER']
            except:
                data_obj['moral_values.ORDER'] = 0 
            try:
                data_obj['moral_values.JUSTICE'] = line_json['liwc']['moral_values']['JUSTICE']
            except:
                data_obj['moral_values.JUSTICE'] = 0 
            try:
                data_obj['moral_values.SECURITY'] = line_json['liwc']['moral_values']['SECURITY']
            except:
                data_obj['moral_values.SECURITY'] = 0 
            try:
                data_obj['moral_values.ACHIEVEMENT'] = line_json['liwc']['moral_values']['ACHIEVEMENT']
            except:
                data_obj['moral_values.ACHIEVEMENT'] = 0 
            try:
                data_obj['moral_values.FEELING-GOOD'] = line_json['liwc']['moral_values']['FEELING-GOOD']
            except:
                data_obj['moral_values.FEELING-GOOD'] = 0 
            try:
                data_obj['moral_values.FORGIVING'] = line_json['liwc']['moral_values']['FORGIVING']
            except:
                data_obj['moral_values.FORGIVING'] = 0 
            try:
                data_obj['moral_values.ACCEPTING-OTHERS'] = line_json['liwc']['moral_values']['ACCEPTING-OTHERS']
            except:
                data_obj['moral_values.ACCEPTING-OTHERS'] = 0 
            try:
                data_obj['moral_values.GRATITUDE'] = line_json['liwc']['moral_values']['GRATITUDE']
            except:
                data_obj['moral_values.GRATITUDE'] = 0 
            try:
                data_obj['moral_values.OPTIMISM'] = line_json['liwc']['moral_values']['OPTIMISM']
            except:
                data_obj['moral_values.OPTIMISM'] = 0 
            try:
                data_obj['moral_values.HONESTY'] = line_json['liwc']['moral_values']['HONESTY']
            except:
                data_obj['moral_values.HONESTY'] = 0                 
            try:
                data_obj['moral_values.SOCIETY'] = line_json['liwc']['moral_values']['SOCIETY']
            except:
                data_obj['moral_values.SOCIETY'] = 0        
            try:
                data_obj['moral_values.RESPECT'] = line_json['liwc']['moral_values']['RESPECT']
            except:
                data_obj['moral_values.RESPECT'] = 0        
            try:
                data_obj['moral_values.LIFE'] = line_json['liwc']['moral_values']['LIFE']
            except:
                data_obj['moral_values.LIFE'] = 0  

            json.dump(data_obj, filehandler)
            filehandler.write('\n')

sort_file(before_twitter, bt_fh)
sort_file(after_twitter, at_fh)

bt_fh.close()
at_fh.close()