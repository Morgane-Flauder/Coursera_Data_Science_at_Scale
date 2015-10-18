import sys
import json

def tweet_sentiment(sent_file, tweet_file):
    states = {
        'AK': {'score': 0, 'nb_tweet': 0},
        'AL': {'score': 0, 'nb_tweet': 0},
        'AR': {'score': 0, 'nb_tweet': 0},
        'AS': {'score': 0, 'nb_tweet': 0},
        'AZ': {'score': 0, 'nb_tweet': 0},
        'CA': {'score': 0, 'nb_tweet': 0},
        'CO': {'score': 0, 'nb_tweet': 0},
        'CT': {'score': 0, 'nb_tweet': 0},
        'DC': {'score': 0, 'nb_tweet': 0},
        'DE': {'score': 0, 'nb_tweet': 0},
        'FL': {'score': 0, 'nb_tweet': 0},
        'GA': {'score': 0, 'nb_tweet': 0},
        'GU': {'score': 0, 'nb_tweet': 0},
        'HI': {'score': 0, 'nb_tweet': 0},
        'IA': {'score': 0, 'nb_tweet': 0},
        'ID': {'score': 0, 'nb_tweet': 0},
        'IL': {'score': 0, 'nb_tweet': 0},
        'IN': {'score': 0, 'nb_tweet': 0},
        'KS': {'score': 0, 'nb_tweet': 0},
        'KY': {'score': 0, 'nb_tweet': 0},
        'LA': {'score': 0, 'nb_tweet': 0},
        'MA': {'score': 0, 'nb_tweet': 0},
        'MD': {'score': 0, 'nb_tweet': 0},
        'ME': {'score': 0, 'nb_tweet': 0},
        'MI': {'score': 0, 'nb_tweet': 0},
        'MN': {'score': 0, 'nb_tweet': 0},
        'MO': {'score': 0, 'nb_tweet': 0},
        'MP': {'score': 0, 'nb_tweet': 0},
        'MS': {'score': 0, 'nb_tweet': 0},
        'MT': {'score': 0, 'nb_tweet': 0},
        'NA': {'score': 0, 'nb_tweet': 0},
        'NC': {'score': 0, 'nb_tweet': 0},
        'ND': {'score': 0, 'nb_tweet': 0},
        'NE': {'score': 0, 'nb_tweet': 0},
        'NH': {'score': 0, 'nb_tweet': 0},
        'NJ': {'score': 0, 'nb_tweet': 0},
        'NM': {'score': 0, 'nb_tweet': 0},
        'NV': {'score': 0, 'nb_tweet': 0},
        'NY': {'score': 0, 'nb_tweet': 0},
        'OH': {'score': 0, 'nb_tweet': 0},
        'OK': {'score': 0, 'nb_tweet': 0},
        'OR': {'score': 0, 'nb_tweet': 0},
        'PA': {'score': 0, 'nb_tweet': 0},
        'PR': {'score': 0, 'nb_tweet': 0},
        'RI': {'score': 0, 'nb_tweet': 0},
        'SC': {'score': 0, 'nb_tweet': 0},
        'SD': {'score': 0, 'nb_tweet': 0},
        'TN': {'score': 0, 'nb_tweet': 0},
        'TX': {'score': 0, 'nb_tweet': 0},
        'UT': {'score': 0, 'nb_tweet': 0},
        'VA': {'score': 0, 'nb_tweet': 0},
        'VI': {'score': 0, 'nb_tweet': 0},
        'VT': {'score': 0, 'nb_tweet': 0},
        'WA': {'score': 0, 'nb_tweet': 0},
        'WI': {'score': 0, 'nb_tweet': 0},
        'WV': {'score': 0, 'nb_tweet': 0},
        'WY': {'score': 0, 'nb_tweet': 0},
        }

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
            if 'place' in tweet and tweet['place'] != None:
                if 'country_code' in tweet['place'] and tweet['place']['country_code'] != None :
                    if tweet['place']['country_code'] == 'US':
                        state_code = tweet['place']['full_name'].split()[-1]
                        if state_code in states:
                            states[state_code]['score'] += score_tweet
                            states[state_code]['nb_tweet'] += 1

    mean_max = 0
    happier_state = ""
    for state_code,id_state in states.items():
        if id_state['nb_tweet'] == 0:
            id_state['mean_sentiment'] = 0
        else:
            id_state['mean_sentiment'] = float(id_state['score']) / float(id_state['nb_tweet'])
        if id_state['mean_sentiment'] > mean_max:
            mean_max = id_state['mean_sentiment']
            happier_state = state_code

    print happier_state
    for i,k in states.items():
        print i, k['mean_sentiment']


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    tweet_sentiment(sent_file, tweet_file)

if __name__ == '__main__':
    main()
