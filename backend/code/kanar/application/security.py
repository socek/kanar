from pyramid.security import Allow
from pyramid.security import Authenticated
from pyramid.security import Everyone


class KanarFactory(object):
    __acl__ = [
        (Allow, Everyone, 'view'),
        (Allow, Authenticated, 'create'),
        (Allow, Authenticated, 'edit'), ]

    def __init__(self, request):
        pass
