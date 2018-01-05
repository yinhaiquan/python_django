#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# redis集群连接操作
import rediscluster

def redisCluster():
    redis_nodes = [
        {'host': '192.168.9.71', 'port': 20006},
        {'host': '192.168.9.71', 'port': 20007},
        {'host': '192.168.9.71', 'port': 20008},
        {'host': '192.168.9.71', 'port': 20009},
        {'host': '192.168.9.71', 'port': 20010},
        {'host': '192.168.9.71', 'port': 20011}
    ]
    try:
        conn = rediscluster.StrictRedisCluster(startup_nodes=redis_nodes);
    except Exception as e:
        print e.message
    print conn.info()
    conn.set("fk:fk",123)
    print conn.get("fk:fk")

redisCluster()