"""
@author wex
send evidence gathering request to each compute node
adopt AQMP in python use pika
receive the results those compute nodes response
"""
#!/usr/bin/python
import pika

class Controller(object):
	def __init__(self):
		self.connection = pika.BlockingConnection(pika.ConnectionParameters(host="172.21.5.34"))
		self.channel=self.connection.channel()
		
		"define the exchange"		
		self.channel.exchange_declare(exchange="network_evidence",type="fanout")

		"define the queue of getting responses"
		result=self.channel.queue_declare(exclusive=True)
		self.callback_queue=result.method.queue
		print self.callback_queue
		self.channel.basic_consume(self.on_response,no_ack=True,queue=self.callback_queue)

	def on_response(self,ch,method,props,body):
		"deal with the response messages"
		self.response=body

	def request(self,message):
		self.response=None
		
		"send the request"
		self.channel.basic_publish(exchange="network_evidence",routing_key="",properties=pika.BasicProperties(reply_to=self.callback_queue,),body=message)
		print "[x] sent gathering request:",message
		"receive the response data"
		while self.response is None:
			self.connection.process_data_events()
	#	self.connection.close()
		return self.response
	
