from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers='qq2.ddnss.de:9092')
topic = 'logging'
serviceName = '1_Django_1'

def log(operation, message):
    loggingMessage = { "service_name": serviceName, "operation": operation, "message": message }
    producer.send(topic, json.dumps(loggingMessage).encode('utf-8'))