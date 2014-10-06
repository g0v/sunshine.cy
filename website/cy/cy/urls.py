from django.conf.urls import patterns, include, url
from rest_framework import routers
from api import views

#--> rest framework url
router = routers.DefaultRouter()
router.register(r'journals', views.JournalsViewSet)
router.register(r'reports', views.ReportsViewSet)
router.register(r'property_car', views.CarViewSet)
router.register(r'property_aircraft', views.AircraftViewSet)
router.register(r'property_boat', views.BoatViewSet)
router.register(r'property_stock', views.StockViewSet)
router.register(r'property_land', views.LandViewSet)
router.register(r'property_building', views.BuildingViewSet)
router.register(r'property_cash', views.CashViewSet)
router.register(r'property_deposit', views.DepositViewSet)
router.register(r'property_bonds', views.BondsViewSet)
router.register(r'property_fund', views.FundViewSet)
router.register(r'property_otherbonds', views.OtherBondsViewSet)
router.register(r'property_antique', views.AntiqueViewSet)
router.register(r'property_insurance', views.InsuranceViewSet)
router.register(r'property_claim', views.ClaimViewSet)
router.register(r'property_debt', views.DebtViewSet)
router.register(r'property_investment', views.InvestmentViewSet)
#<--

urlpatterns = patterns('',
    url(r'^people/', include('people.urls', namespace="people")),
    url(r'^ranking/', include('ranking.urls', namespace="ranking")),
    url(r'^about/$', 'cy.views.about', name='about'),
    url(r'^reference/$', 'cy.views.reference', name='reference'),
    url(r'^api/', include(router.urls)),
    url(r'', 'cy.views.home', name='home'),
)
