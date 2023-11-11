from monitor.models import Store, StoreStatusLog, StoreStatus , StoreReport , ReportStatus
from django.utils import timezone 
from pytz import timezone as pytz_timezone
import datetime


from monitor.models import Store
stores = Store.objects.all()[:50]
from monitor.helper import trigger_report_combined
report = StoreReport.objects.create(status=ReportStatus.PENDING)
trigger_report_combined(report)
