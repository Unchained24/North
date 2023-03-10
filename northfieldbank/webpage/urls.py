from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('checking/', views.checking, name='checking'),
    path('location&hours/', views.locationandhours, name='location&hours'),
    path('terms and conditions/', views.termsandcondition, name='terms'),
    path('Rates.aspx.html/', views.rates, name='rates'),
    path('savings.aspx.html/', views.savings, name='savings'),
    path('health-saving.aspx.html/', views.healthsaving, name='healthsaving'),
    path('CD-IRA.aspx.html', views.cdira, name='cdira'),
    path('Personal-Loan.aspx.html', views.personalLoan, name='personalLoan'),
    path('AdditionalServices.aspx.html', views.AdditionalServices, name='AdditionalServices'),
    path('OnlineEducation.aspx.html', views.OnlineEducation, name='OnlineEducation'),
    path('ATM-Debit-Cards.aspx.html', views.atm, name='atm'),
    path('Business-Checking.aspx.html', views.BusinessChecking, name='BusinessChecking'),
    path('Business-Savings.aspx.html', views.BusinessSavings, name='BusinessSavings'),
    path('Business-CDs.aspx.html', views.cds, name='cds'),
    path('Business-Loans.aspx.html', views.BusinessLoan, name='BusinessLoan'),
    path('Land-Trust.aspx.html', views.LandTrust, name='LandTrust'),
    path('$04-Page not found', views.notfound, name='404'),
    path('About-Us.aspx.html', views.aboutus, name='aboutus'),
    path('Team.aspx.html', views.team, name='team'),
    path('News.aspx.html', views.news, name='news'),
    path('Contact-Us.aspx.html', views.contactus, name='contactus'),
    path('customer-content.aspx.html?name=Media', views.customercontent, name='customercontent'),
    path('Frequently-Asked-Questions.aspx.html?', views.faqs, name='faqs'),
    path('Privacy-Policy.aspx.html?', views.privacy, name='privacy'),
    path('disclousure.aspx.html?', views.disclousure, name='disclousure'),
    path('Accessibility.aspx.html?', views.Accessibility, name='Accessibility'),
    path('Online-Security.aspx.html?', views.security, name='security'),
    path('Resources.aspx.html?', views.resources, name='resources'),
]