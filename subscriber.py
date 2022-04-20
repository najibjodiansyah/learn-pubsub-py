import os
from google.cloud import pubsub_v1

credential_path = '/Users/najibjodiansyah/Documents/pubsubpy/still-sensor-private-key.still-sensor-private-key.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


timeout = 10.0

subscriber = pubsub_v1.SubscriberClient()
subscription_path = 'projects/still-sensor-339610/subscriptions/Testing-PubSub-Py-sub'

def callback(message):
    print('Recevied message:'+{message})
    print('data: '+ {message.data})
    message.ack()

streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print('listening for message on' + subscription_path)

with subscriber:
    try:
        streaming_pull_future.result()
    except TimeoutError:
        streaming_pull_future.cancel()
        streaming_pull_future.result()