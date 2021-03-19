import os
import json
import queue #from multiprocessing import Process, Queue
from kafka import KafkaConsumer
#from processing import *

def main():
    consumer_tweets = KafkaConsumer(
        os.getenv('KAFKA_TOPIC', 'tweets'),
        bootstrap_servers=os.getenv('KAFKA_BOOTSTRAP_SERVER', 'kafka:9092'),
        group_id=None,
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        api_version=(2, 3, 0),
        consumer_timeout_ms=5000,
        auto_offset_reset='latest',
        enable_auto_commit=True)

    #q = queue.Queue()
    #proc = Process(target=sentiment_analysis, args=(q,))
    #proc.start()
    i = 0
    for msg in consumer_tweets:
        tweet_full = msg.value

        i += 1

        if tweet_full['lang'] not in ['de', 'en', 'es', 'fr', 'it', 'pt'] and tweet_full['lang'] is not None:
            continue

        print(i, tweet_full['text'])
        #process_tweet(tweet_full, q)

    #proc.join()


if __name__ == "__main__":
    main()