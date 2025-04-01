import pika

def on_message_received(ch, method, properties, body):
    print(f"firstconsumer - received new message: {body}")

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='pubsub', exchange_type='fanout')

queue = channel.queue_declare(queue='', exclusive=True)# once connection is closed , the queue can be deleted. also no name is given to the queue.

channel.queue_bind(exchange='pubsub', queue=queue.method.queue) # binding the queue to the consumer. If the queue is not bound to the consumer then no message will be received by the consumer since it wont have any queue to reference to.

channel.basic_consume(queue=queue.method.queue, auto_ack=True,
    on_message_callback=on_message_received)

print("Starting Consuming")

channel.start_consuming()