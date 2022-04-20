import os
from google.cloud import pubsub_v1

credential_path = '/Users/najibjodiansyah/Documents/pubsubpy/still-sensor-private-key.still-sensor-private-key.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


publisher = pubsub_v1.PublisherClient()
topic_path = 'projects/still-sensor-339610/topics/Testing-PubSub-Py'


data = 'Ini data untuk dikirim ke pubsub testing'
data = data.encode('utf-8')

future = publisher.publish(topic_path, data)
# print(f'published message id {future.result()}')
print('published message id '+ future.result())