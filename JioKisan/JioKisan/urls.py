from django.contrib import admin
from django.urls import include, path
from . import views
from . import voice
from . import mandi
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls, name='admin_page'),
    path('paytm/', include('paytm.urls')),
    path('new_reg/',views.new_registration, name='NewRegistrations'),
    path('otp_check/',views.otp_check, name='CheckingOTP'),
    path('login/',views.login, name='NewRegistrations'),
    path('login_check/',views.login_check, name='CheckingOTP'),
    path('',views.ResponsePage,name='Response Page'),
    path('trade/',include('trade.urls')),
    path('stt/',views.speechtotext, name='Speech to Text'),
    path('upload/',views.voice_input, name='upload'),
    path('get_prod_list/',views.getProduceList,name='getProduceList'),
    path('get_ftool_list/',views.getFToolList,name='getFToolList'),
    path('get_driver_info', views.getDriverInfo, name='getDriverInfo'),
    path('get_driver_path', views.getDriverPath, name='getDriverPath'),
    path('get_req_list/',views.getReqList,name='getReqList'),
    path('get_ft_buy_list/',views.getFTBuyList,name='getFTBuyList'),
    path('get_hired',views.getHired,name='getHired'),
    path('get_req_list/',views.getReqList,name='getReqList'),
    path('list_farmEnitity/',views.list_farmEnitity,name="list_farmEnitity"),
    path('list_farmTool/',views.list_farmTool,name="list_farmTool"),
    path('update_status',views.updateDeliveryStatus,name="updateDeliveryStatus"),
    path('add_f_m_consignment/',views.addFtoMConsignment,name='addFtoMConsignment'),
    path('add_fts_f_consignment/',views.addFTStoFConsignment,name='addFTStoFConsignment'),
    path('get_past_consignments/',views.getPastConsignment,name='getPastConsignment')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
