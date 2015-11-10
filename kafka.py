from kafka import SimpleProducer, KafkaClient
import json
import time
kafka = KafkaClient('kafka:9092')
producer = SimpleProducer(kafka)
some_new_listing = {'title': 'Used MacbookAir 13"', 'description': 'This is a used Macbook Air in great condition', 'id':42}
try:
	producer.send_messages(b'new-listings-topic', json.dumps(some_new_listing).encode('utf-8'))
except:
	time.sleep(5)
	producer.send_messages(b'new-listings-topic', json.dumps(some_new_listing).encode('utf-8'))