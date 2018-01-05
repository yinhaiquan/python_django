#!/usr/bin/env python
# coding:utf-8

# python 枚举使用

from enum import Enum

Animal = Enum("dog", "animal")
Animal2 = Enum("Animal2", "123456")

print Animal.__getitem__(0)
print Animal.__getitem__(1)

# 自定义枚举
class StatusEnum(Enum):
    YES = {'desc': 'yes', 'code': 0}
    NO = {'desc': 'no', 'code': 1}

    # 获取枚举详细内容
    @staticmethod
    def getInstance(code):
        for item in StatusEnum.__dict__.items():
            if isinstance(item.__getitem__(1), dict):
                dic = eval(str(item.__getitem__(1)))
                if code == dic['code']:
                    return item
        return None


print (isinstance(StatusEnum.NO, int))
print (isinstance(StatusEnum.NO, dict))
print StatusEnum.NO.__getitem__('desc')
print StatusEnum.NO.__getitem__('code')
print StatusEnum.__dict__.items()
print StatusEnum.getInstance(1)



