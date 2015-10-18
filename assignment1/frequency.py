import sys
import json

def main():
    tweet_file = open(sys.argv[1])

    count_words = {}
    total_words = 0
    for line in tweet_file:
        tweet = json.loads(line)
        if 'text' in tweet:
            words = tweet['text'].split()
            for word in words:
                total_words += 1
                if word in count_words:
                    count_words[word] += 1
                else:
                    count_words[word] = 1

    for key,value in count_words.items():
        print key, float(value)/float(total_words)

if __name__ == '__main__':
    main()
