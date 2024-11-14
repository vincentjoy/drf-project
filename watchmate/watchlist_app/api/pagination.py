from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class WatchListPagination(PageNumberPagination):
    page_size = 10  # Number of items per page
    page_query_param = 'page'  # Query parameter for specifying the page number
    page_size_query_param = 'page_size'  # Query parameter for specifying the page size
    max_page_size = 15  # Maximum number of items per page
    last_page_strings = ('last', 'end')  # Custom strings for the last page link


class WatchListLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10  # Default number of items per page
    max_limit = 15
    limit_query_param = 'limit'  # Query parameter for specifying the page size
    offset_query_param = 'start'  # Query parameter for specifying the offset


class WatchListCursorPagination(CursorPagination):
    page_size = 10  # Number of items per page
    ordering = '-created'  # Order items by created date in descending order
