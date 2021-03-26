print("Total number of articles:")
print(len(articles_list)-1)

print("Total number of columns:")
print(len(articles_list[0]), end='\n\n')




for article in articles_dict:
    
    words = article['description'].split()
    word_count = len(words)
    
    article['word_count'] = word_count

print(article[0])



