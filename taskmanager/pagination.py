from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

from collections import OrderedDict
from rest_framework.response import Response



class BasePageNumberPagination(PageNumberPagination):
    """Pagination class"""
    page_size = 5
    page_query_param = "page"
    max_page_size = 1000
    page_size_query_param = "page_size"


class BaseLimitOffsetPagination(LimitOffsetPagination):
    """Pagination class."""
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = None


    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.count),
            ('results', data)
        ]))