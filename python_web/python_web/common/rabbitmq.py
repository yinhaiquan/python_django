#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# python rabbitmq 消息中间件使用

import pika

# 消息生产者 p2p
def provider():
    credentials = pika.PlainCredentials("guest", "guest")
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost", 5672, '/', credentials))
    channel = connection.channel()
    channel.queue_declare(queue="hq_3")
    channel.basic_publish(exchange='', routing_key='hq_3', body="fuck 008!!!")
    print "发送消息完毕!"
    channel.close()
    connection.close()
# 消费者
def consumer():
    # 连接到rabbitmq服务器
    credentials = pika.PlainCredentials("guest", "guest")
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost", 5672, '/', credentials))
    channel = connection.channel()
    # 声明消息队列，消息将在这个队列中进行传递。如果队列不存在，则创建
    channel.queue_declare(queue="hq_3")
    # 告诉rabbitmq使用callback来接收信息
    # no_ack=True表示在回调函数中不需要发送确认标识
    channel.basic_consume(call_back,queue="hq_3",no_ack=True)
    print "waiting for message......"
    # 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理。
    channel.start_consuming()

# 定义一个回调函数来处理，这边的回调函数就是将信息打印出来。
def call_back(ch,method,properties,body):
    print "received : %s" % body

consumer()