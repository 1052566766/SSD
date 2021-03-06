# coding:utf8
'''
File: config.py
Project: chapter6-实战指南
File Created: Sunday, 3rd June 2018 2:38:47 pm
Author: xiaofeng (sxf1052566766@163.com)
-----
Last Modified: Monday, 30th July 2018 11:12:59 am
Modified By: xiaofeng (sxf1052566766@163.com>)
-----
Copyright 2018.06 - 2018 onion Math, onion Math
'''

import warnings


class DefaultConfig(object):
    env             = 'default'  # visdom 环境
    model           = 'ResNet34'  # 使用的模型，名字必须与models/__init__.py中的名字一致

    train_data_root = './data/train.txt'  # 训练集存放路径
    test_data_root  = './data/val.txt'  # 测试集存放路径
    load_model_path = './saved_model/yolov3.pth'  # 加载预训练的模型的路径，为None代表不加载
    model_json_path = './saved_model/yolov3_layers.json'
    log_file        = './log.txt'
    batch_size      = 32  # batch size
    use_gpu         = True  # user GPU or not
    num_workers     = 4  # how many workers for loading data
    print_freq      = 20  # print info every N batch

    debug_file      = '/tmp/debug'  # if os.path.exists(debug_file): enter ipdb
    result_file     = 'result.csv'

    max_epoch       = 1e+10
    lr              = 0.001  # initial learning rate
    lr_decay        = 0.5  # when val_loss increase, lr            = lr*lr_decay
    weight_decay    = 0e-5  # 损失函数
    end_adjust_acc  = 0.96

def parse(self, kwargs):
    '''
    根据字典kwargs 更新 config参数
    '''
    for k, v in kwargs.items():
        if not hasattr(self, k):
            warnings.warn("Warning: opt has not attribut %s" % k)
        setattr(self, k, v)

    print('user config:')
    for k, v in self.__class__.__dict__.items():
        if not k.startswith('__'):
            print(k, getattr(self, k))


DefaultConfig.parse = parse
opt = DefaultConfig()
# opt.parse = parse
