from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import TacoStandFinancialData
from .serializers import TacoStandFinancialDataSerializer, TacoStandFinancialDataListSerializer
from .middleware import IsAuthenticatedOrReadOnly, CustomPagination

# For caching
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

# ViewSet for TacoStandFinancialData model
class TacoStandFinancialDataViewSet(viewsets.ModelViewSet):
    # retrieve all records from TacoStandFinancialData model
    queryset = TacoStandFinancialData.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['date', 'daily_customers']
    ordering_fields = ['date', 'daily_revenue']
    search_fields = ['date', 'daily_revenue', 'daily_customers']
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Denotes use of list action or non list for total records
    def get_serializer_class(self):
        if self.action == 'list':
            return TacoStandFinancialDataListSerializer
        return TacoStandFinancialDataSerializer

    # Apply caching to the list view
    # Cache the list view for 15 minutes
    @method_decorator(cache_page(60*15), name='list')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)