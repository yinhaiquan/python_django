#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 测试python国际化（局部国际化）

import gettext
# 相对路径 语言包路径，且语言文件目录必须加上LC_MESSAGES目录，并将资源文件存放于此
local_path = './locale/'
# 注意messages就是语言文件名
zh_trans = gettext.translation('messages',local_path,languages=['zh_CN'])
# en_trans = gettext.translation('messages',local_path,languages=['en_US'])

print "-----------中文-----------"
zh_trans.install(unicode=True)

print _("text1")
print _("text2")

print "-----------英文-----------"
# en_trans.install(unicode=True)

# print _("text1")
# print _("text2")

class I18NUtils:
    @staticmethod
    def init(domain,language):
        gettext.translation(domain,local_path,languages=[language]).install(unicode=True)

    @staticmethod
    def geText(message):
        return _(message)

# I18NUtils.init('messages','zh_CN')
# print I18NUtils.geText("text1")

