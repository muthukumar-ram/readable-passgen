# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 13:17:54 2022

@author: inmkumar10
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 12:34:41 2022

@author: inmkumar10
"""

from random_word import RandomWords
import pandas as pd
r=RandomWords()
#r.get_random_words()
#r.get_random_words(hasDictionaryDef="true", includePartOfSpeech="noun,verb", minCorpusCount=1, maxCorpusCount=10, minDictionaryCount=1, maxDictionaryCount=10, minLength=5, maxLength=10, sortBy="alpha", sortOrder="asc", limit=15)
import random
def genPass():
    word_lists=r.get_random_words(hasDictionaryDef="true", includePartOfSpeech="noun,verb", 
                                  minCorpusCount=1, maxCorpusCount=10, minDictionaryCount=1, 
                                  maxDictionaryCount=10, minLength=5, maxLength=10, sortBy="alpha", 
                                  sortOrder="asc", limit=15)
    #print(random.choice(word_lists))
    word=random.choice(word_lists)
    color_lengths=[5,8,10]
    color_length=random.choice(color_lengths)
    
    color_df=pd.read_csv(r'https://raw.githubusercontent.com/muthukumar-ram/readable-passgen/main/colors_list.csv',header='infer')
    filtered_colors=color_df[color_df['colors'].str.len() == color_length]
    random_color=filtered_colors['colors'][random.choice(list(filtered_colors.index))]
    
    allowed_special_char='_!@#$%^&*.-'
    random_special_char=random.choice(allowed_special_char)
    
    
    random_number=random.randint(1,998)
    the_final_word=None
    the_final_word=random_color+word.capitalize()+random_special_char+str(random_number)
    if len(the_final_word) < 14:
        genPass()
    return the_final_word

if __name__ == '__main__':
    the_password=genPass()
    print(the_password)