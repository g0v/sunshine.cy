from django.conf.urls import include, url

from rest_framework import routers

from . import views as cy_views
from api import views as api_views

#--> rest framework url
router = routers.DefaultRouter()
router.register(r'journals',api_views.JournalsViewSet)
router.register(r'reports',api_views.ReportsViewSet)
router.register(r'property_car',api_views.CarViewSet)
router.register(r'property_aircraft',api_views.AircraftViewSet)
router.register(r'property_boat',api_views.BoatViewSet)
router.register(r'property_stock',api_views.StockViewSet)
router.register(r'property_land',api_views.LandViewSet)
router.register(r'property_building',api_views.BuildingViewSet)
router.register(r'property_cash',api_views.CashViewSet)
router.register(r'property_deposit',api_views.DepositViewSet)
router.register(r'property_bonds',api_views.BondsViewSet)
router.register(r'property_fund',api_views.FundViewSet)
router.register(r'property_otherbonds',api_views.OtherBondsViewSet)
router.register(r'property_antique',api_views.AntiqueViewSet)
router.register(r'property_insurance',api_views.InsuranceViewSet)
router.register(r'property_claim',api_views.ClaimViewSet)
router.register(r'property_debt',api_views.DebtViewSet)
router.register(r'property_investment',api_views.InvestmentViewSet)
#<--

urlpatterns = [
    url(r'^$', cy_views.home, name='home'),
    url(r'^people/', include('people.urls', namespace="people")),
    url(r'^ranking/', include('ranking.urls', namespace="ranking")),
    url(r'^about/$', cy_views.about, name='about'),
    url(r'^reference/$', cy_views.reference, name='reference'),
    url(r'^api/', include(router.urls)),
]
