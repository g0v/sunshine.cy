#from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . import fields
from journals.models import Journals
from reports.models import Reports
from property.models import Stock, Land, Building, Car, Cash, Deposit, Aircraft, Boat, Bonds, Fund, OtherBonds, Antique, Insurance, Claim, Debt, Investment


class JournalsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Journals

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

class ReportsSerializer(serializers.HyperlinkedModelSerializer):
    land_set = LandSerializer(many=True, read_only=True)
    building_set = BuildingSerializer(many=True, read_only=True)
    boat_set = BoatSerializer(many=True, read_only=True)
    car_set = CarSerializer(many=True, read_only=True)
    aircraft_set = AircraftSerializer(many=True, read_only=True)
    cash_set = CashSerializer(many=True, read_only=True)
    deposit_set = DepositSerializer(many=True, read_only=True)
    bonds_set = BondsSerializer(many=True, read_only=True)
    fund_set = FundSerializer(many=True, read_only=True)
    otherbonds_set = OtherBondsSerializer(many=True, read_only=True)
    antique_set = AntiqueSerializer(many=True, read_only=True)
    insurance_set = InsuranceSerializer(many=True, read_only=True)
    claim_set = ClaimSerializer(many=True, read_only=True)
    debt_set = DebtSerializer(many=True, read_only=True)
    investment_set = InvestmentSerializer(many=True, read_only=True)
    class Meta:
        model = Reports
