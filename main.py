#here We are connecting with properly libraries
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

comments=[]
pos_comms=0
neg_comms=0

def add_comment(comment):
    global pos_comms, neg_comms
    sentiment=SentimentIntensityAnalyzer()
    rate=sentiment.polarity_scores(comment)
    print(f'The rate of Your opinion is: {rate}')
    if rate['neg']>rate['pos'] and rate['neg']>rate['neu']:
        print(f'This comment is negative')
        neg_comms+=1
    else:
        print('This comment is more positive')
        pos_comms+=1
    comments.append(comment)


def check_comments():
    print(f'All of Your comments: ')
    print(comments)

def check_scoring():
    user=input('Do You want to check positive(P) or negative(N) comments?: ')
    if user.upper()=='N':
        print(neg_comms)
    elif user=='P':
        print(pos_comms)
    else:
        print('You have chosen wrong letter, choose N or P')

def main():
    while True:
        user=input('Hi,Please enter Your opinion: ')
        print(f'{add_comment(user)}')
        next=input('Do You want to check comments scoring(s)/comments at all(c) /or add another comment(a)?')
        if next=='c':
            check_comments()
        elif next=='s':
            check_scoring()
        elif next=='a':
            continue
        else:
            print('You have chosen wrong letter, choose s, c, or a')
if __name__=='__main__':
    main()
