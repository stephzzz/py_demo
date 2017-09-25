import uuid


'''
uuid:通用唯一识别码
共5种算法：
1、在分布式global的分布式计算环境下最好用uuid1
2、若有名字的唯一性要求最好用uuid3或uuid5
'''
def get_uuid():
    str_uuid = str(uuid.uuid1())
    return ''.join(str_uuid.split('-'))

