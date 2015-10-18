import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)

    for line in tweet_file:
        tweet = json.loads(line)
        score_tweet = 0
        if 'text' in tweet:
            words = tweet['text'].split()
            for word in words:
                if word in scores:
                    score_tweet += scores[word]
        print score_tweet

    #hw()
    #lines(sent_file)
    #lines(tweet_file)



if __name__ == '__main__':
    main()
