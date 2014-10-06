#from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . import fields
from journals.models import Journals
from reports.models import Reports
from property.models import Stock, Land, Building, Car, Cash, Deposit, Aircraft, Boat, Bonds, Fund, OtherBonds, Antique, Insurance, Claim, Debt, Investment


class JournalsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Journals

class ReportsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reports

class StockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stock

class LandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Land

class BuildingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Building

class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car

class CashSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cash

class DepositSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Deposit

class AircraftSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aircraft

class BoatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Boat

class BondsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bonds

class FundSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fund

class OtherBondsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OtherBonds

class AntiqueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Antique

class InsuranceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Insurance

class ClaimSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Claim

class DebtSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Debt

class InvestmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Investment
