# -*- coding: utf-8 -*-

from schemer import Schema

class Article(object):
    """ 文章类 """

    def __init__(self, **kwargs):
        """
        :param author:  作者
        :param title:   标题
        :param content: 内容
        :param label:   标签
        """

        param_schema = Schema({
            'no': {'type': basestring, 'required': True},
            'author': {'type': basestring, 'required': True},
            'title': {'type': basestring, 'required': True},
            'content': {'type': basestring, 'required': True},
            'category': {'type': basestring, 'required': True},
            'views': {'type': basestring, 'required': True},
            'modified': {'type': basestring, 'required': True},

        })

        param_schema.validate(kwargs)  # 检测不通过直接抛异常
        param_schema.apply_defaults(kwargs)  # attach 默认值

        self.no = kwargs.get('no')
        self.author = kwargs.get('author')
        self.title = kwargs.get('title')
        self.content = kwargs.get('content')
        self.category = kwargs.get('category')
        self.views = kwargs.get('views')
        self.modified = kwargs.get('modified')

    def dictify(self):
        d = dict(filter(lambda x: isinstance(x[1], (str, float, int, unicode)), self.__dict__.items()))
        return d