#from django_trading_platform.settings import iq_option_api
import datetime
import time
# Create your views here.
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
import logging
logging.basicConfig(format='%(asctime)s %(message)s')


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        print()
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Central", "Eastside", "Westside"]

    def get_data(self):
        """Return 3 datasets to plot."""
        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]


def get_line_view():
    #print(iq_option_api.get_all_actives())
    return TemplateView.as_view(template_name='line_chart.html')


def get_LineChartJSONView():
    #print('Your current blance is: {:.2f}'.format(iq_option_api.get_balance()))
    print("emmm***********************************")
    return LineChartJSONView.as_view()


line_chart = get_line_view()
line_chart_json = get_LineChartJSONView()