from rest_framework.pagination import PageNumberPagination


class WatchListPagination(PageNumberPagination):
    page_size = 10  # Number of items per page
    page_query_param = 'page'  # Query parameter for specifying the page number
    page_size_query_param = 'page_size'  # Query parameter for specifying the page size
    max_page_size = 15  # Maximum number of items per page
    last_page_strings = ('last', 'end')  # Custom strings for the last page link