from django.contrib import admin

from .models import Tptest
from .models import Tptestnew
from .models import Appointment
from .models import CurrentUser
from creds.models import Credential

admin.site.register(Tptest)
admin.site.register(Tptestnew)
admin.site.register(Appointment)
admin.site.register(CurrentUser)
