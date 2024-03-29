from django.db import models
from Coins_club_owner.models import *
from Coins_trader.models import *
from Jockey_club_owner.models import *
from Audio_Jockey.models import *
from User.models import *
from master.models import*

from django.utils.timezone import now

class Admin_to_Coins_club_owner(models.Model):
    Coins_Club_Owner_Id = models.ForeignKey(Coins_club_owner,on_delete=models.CASCADE)
    numcoin = models.PositiveIntegerField(blank=False)
    created_date = models.DateTimeField(default=now)


class Coins_club_owner_to_Coins_trader(models.Model):
    from_owner = models.ForeignKey(Coins_club_owner, on_delete=models.CASCADE)
    to_trader = models.ForeignKey(Coins_trader, on_delete=models.PROTECT)
    amount = models.PositiveIntegerField()
    created_date = models.DateTimeField(default=now)


class Coins_trader_to_Jockey_club_owner(models.Model):
    from_trader = models.ForeignKey(Coins_trader, on_delete=models.CASCADE)
    to_Jockey_club_owner = models.ForeignKey(Jockey_club_owner, on_delete=models.PROTECT)
    amount = models.PositiveIntegerField()
    created_date = models.DateTimeField(default=now)


class Coins_trader_to_User(models.Model):
    from_trader = models.ForeignKey(Coins_trader, on_delete=models.CASCADE)
    to_User = models.ForeignKey(User, on_delete=models.PROTECT)
    amount = models.PositiveIntegerField()
    created_date = models.DateTimeField(default=now)

class User_to_Audio_Jockey(models.Model):
    from_User = models.ForeignKey(User, on_delete=models.PROTECT)
    to_Audio_Jockey = models.ForeignKey(Audio_Jockey, on_delete=models.PROTECT)
    amount = models.PositiveIntegerField()
    created_date = models.DateTimeField(default=now)


# class Top_Fan_list(models.Model):
#     receiver = models.ForeignKey(Common, on_delete=models.PROTECT, related_name='received_transactions')
#     amount = models.PositiveIntegerField()
#     created_date = models.DateTimeField(default=now)
########################
class Vipram(models.Model):
    # profile_pictures = models.JSONField(default=list, blank=True, null=True)
    profile_pictureVip1 = models.CharField(max_length=2000, default='', blank=True, null=True)

    def save(self, *args, **kwargs):
        # Ensure data is stored only once if no profile picture fields are filled
        if not self.id and not self.profile_pictureVip1:
            super().save(*args, **kwargs)

    def __str__(self):
        return f"VipUser {self.id}"