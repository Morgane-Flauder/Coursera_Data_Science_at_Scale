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

    ns_words = {}
    for line in tweet_file:
        tweet = json.loads(line)
        score_tweet = 0
        if 'text' in tweet:
            words = tweet['text'].split()
            for word in words:
                if word in scores:
                    score_tweet += scores[word]
                else:
                    ns_words[word] = 0
            for word in words:
                if word not in scores:
                    ns_words[word] += score_tweet / len(words)

    for key,value in ns_words.items():
        print key,value




    #hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
