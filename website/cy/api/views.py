#from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import filters
from .serializers import *
from journals.models import Journals
from reports.models import Reports
from property.models import Stock, Land, Building, Car, Cash, Deposit, Aircraft, Boat
from property.models import Stock, Land, Building, Car, Cash, Deposit, Aircraft, Boat, Bonds, Fund, OtherBonds, Antique, Insurance, Claim, Debt, Investment


class JournalsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Journals.objects.all()
    serializer_class = JournalsSerializer
    filter_fields = ('name', 'date')

class ReportsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializer
    filter_fields = ('journal', 'category', 'name', 'department', 'title', 'report_at', 'report_type', 'spouse', 'at_page', 'file_id')

class StockViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_fields = ('report', 'name', 'symbol', 'owner', 'quantity', 'face_value', 'currency', 'total')

class LandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Land.objects.all()
    serializer_class = LandSerializer
    filter_fields = ('report', 'name', 'area', 'share_portion', 'portion', 'owner', 'register_date', 'register_reason', 'acquire_value', 'total')

class BuildingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    filter_fields = ('report', 'name', 'area', 'share_portion', 'portion', 'owner', 'register_date', 'register_reason', 'acquire_value', 'total')

class CarViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_fields = ('report', 'name', 'capacity', 'owner', 'register_date', 'register_reason', 'acquire_value')

class CashViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cash.objects.all()
    serializer_class = CashSerializer
    filter_fields = ('report', 'currency', 'owner', 'total')

class DepositViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer
    filter_fields = ('report', 'bank', 'deposit_type', 'currency', 'owner', 'total')

class AircraftViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer
    filter_fields = ('report', 'name', 'maker', 'number', 'owner', 'register_date', 'register_reason', 'acquire_value')

class BoatViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Boat.objects.all()
    serializer_class = BoatSerializer
    filter_fields = ('report', 'name', 'tonnage', 'homeport', 'owner', 'register_date', 'register_reason', 'acquire_value')

class BondsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bonds.objects.all()
    serializer_class = BondsSerializer
    filter_fields = ('report', 'name', 'symbol', 'owner', 'dealer', 'quantity', 'face_value', 'market_value', 'currency', 'total', 'total_value')

class FundViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Fund.objects.all()
    serializer_class = FundSerializer
    filter_fields = ('report', 'name', 'owner', 'dealer', 'quantity', 'face_value', 'market_value', 'currency', 'total', 'total_value')

class OtherBondsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OtherBonds.objects.all()
    serializer_class = OtherBondsSerializer
    filter_fields = ('report', 'name', 'owner', 'quantity', 'face_value', 'market_value', 'currency', 'total', 'total_value')

class AntiqueViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Antique.objects.all()
    serializer_class = AntiqueSerializer
    filter_fields = ('report', 'name', 'owner', 'quantity', 'total')

class InsuranceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
    filter_fields = ('report', 'name', 'company', 'owner')

class ClaimViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer
    filter_fields = ('report', 'species', 'debtor', 'owner', 'register_date', 'register_reason', 'total')

class DebtViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer
    filter_fields = ('report', 'species', 'debtor', 'owner', 'register_date', 'register_reason', 'total')

class InvestmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer
    filter_fields = ('report', 'owner', 'company', 'address', 'register_date', 'register_reason', 'total')
