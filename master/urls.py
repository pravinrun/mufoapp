from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('follow/<uuid:follow>/', FollowUser.as_view(), name='follow-user'),
    path('follow/<uuid:follow>/<str:date>', FollowUser.as_view(), name='follow-user'),

    path('followers/', FollowerList.as_view(), name='follower-list'),
    path('following/', FollowingList.as_view(), name='following-list'),
    path('getUser/<uuid:Userid>/', GetUser.as_view(), name='getUser'),
    path('getUserData/', GetUserdata.as_view(), name="GetUserdata"),
    path('Searchalluser/', Searchalluser.as_view(), name="userview"),
    path('allcommonuser/', Alluser.as_view(), name="userview"),
    path('gift-transfer/', GiftTransfer.as_view(), name='coin-transfer'),
    path('user-spent-time/', UserSpentTimeList.as_view(), name='user-spent-time-list'),
    path('topfanlist/', Top_fans_listing_View.as_view(), name='topfanlist'),
    path('globaleTopfanlistall/', GlobaleTopFanListAll.as_view(), name='globaleTopfanlistall'),
    #path('adminAlluser/', Approved_by_admin_Alluser.as_view(), name='approved_by_admin_Alluser'),
    path('adminAlluser/', ApprovedByAdminAllUser.as_view(), name='ApprovedByAdminAllUser'),
    path('Top_fans/',Top_fans.as_view(), name='Top_fans'),
    path('ApprovedByAdmin/',ApprovedByAdmin.as_view(), name='ApprovedByAdmin'),
    path('Notification/',Notification.as_view(), name='Notification'),
    

]
