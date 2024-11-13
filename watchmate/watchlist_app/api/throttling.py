from rest_framework.throttling import UserRateThrottle

class ReviewCreateThrottle(UserRateThrottle):
    scope = 'review_create'


class ReviewListThrottel(UserRateThrottle):
    scope = 'review_list'