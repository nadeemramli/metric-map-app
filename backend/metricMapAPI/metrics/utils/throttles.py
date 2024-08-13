from rest_framework.throttling import UserRateThrottle

class ComputationTriggerThrottle(UserRateThrottle):
    rate = '1/minute'
