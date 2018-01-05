#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import ConfigParser

# 解析配置文件类似java 属性文件
import os

config = ConfigParser.ConfigParser();
config.read({'test.conf','../logging_config.conf'})
print config.sections()

print config.get("game0","ip")
print config.items("game0")
print config.options("game0")
