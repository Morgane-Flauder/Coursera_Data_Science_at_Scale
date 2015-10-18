import sys
import json

def main():
    tweet_file = open(sys.argv[1])

    dico_hashtags = {}
    for line in tweet_file:
        tweet = json.loads(line)
        if 'entities' in tweet and tweet['entities'] != None:
            if 'hashtags' in tweet['entities'] and len(tweet['entities']['hashtags']) != 0:
                list_hashtags = tweet['entities']['hashtags']
                for hashtag in list_hashtags:
                    if hashtag['text'] in dico_hashtags:
                        dico_hashtags[hashtag['text']] += 1
                    else:
                        dico_hashtags[hashtag['text']] = 1

    list_hashtags_total = list(dico_hashtags.items())
    list_sorted = sorted(list_hashtags_total, key=lambda col: col[1])
    top_ten = list_sorted[0:10]
    for i in top_ten:
        print i[0], i[1]

if __name__ == '__main__':
    main()
