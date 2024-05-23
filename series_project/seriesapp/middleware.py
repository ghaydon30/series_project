from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

# Custom pagination class defaulting to 20 pages
class CustomPagination(PageNumberPagination):
    page_size = 20 
    # Allow clients to set the page size with a query parameter
    page_size_query_param = 'page_size'
    max_page_size = 100

"""
Custom permission to allow unauthenticated users to read-only access,
and authenticated users to have full access.
"""
class IsAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # SAFE_METHODS includes GET, HEAD, and OPTIONS requests
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated

# Custom exception handler to provide consistent error responses
def custom_exception_handler(exc, context):
    # DRF default exception handler
    response = exception_handler(exc, context)

    # Checks for DRF has generated a response
    if response is not None:
        custom_response_data = {
            'error': {
                'status_code': response.status_code,
                'message': response.data
            }
        }
        response.data = custom_response_data

    return response