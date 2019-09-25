from confluent_kafka import Consumer

if __name__ == '__main__':

	conf = {
		'bootstrap.servers': '',
		'security.protocol': 'SASL_PLAINTEXT',
		'group.id': 'john_group',
		'sasl.mechanism': 'SCRAM-SHA-256',
		'sasl.username': '',
		'sasl.password': '',
		'auto.offset.reset': 'earliest'
	}

	consumer = Consumer(**conf)

	consumer.subscribe([''])

	# while True:
	for i in range(100):
		msg = consumer.poll(1.0)

		if msg is None:
			continue
		if msg.error():
			print("Consumer error: {}".format(msg.error()))
			continue

		print('%s [%d] at offset %d with key %s: %s\n' % (msg.topic(), msg.partition(), msg.offset(), str(msg.key()), msg.value().decode('utf-8')))
		# print('Received message: {}'.format(msg.value().decode('utf-8')))

	consumer.close()
