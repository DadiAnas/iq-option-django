#!/usr/bin/env python
import os
import sys
import time

from pyiqoptionapi import IQOption

try:
    from credentials import *
except ImportError:
    pass


class Trade:
    def __init__(self, email=None, password=None):
        email = email or os.environ['IQ_OPTIONS_API_EMAIL']
        password = password or os.environ['IQ_OPTIONS_API_PASSWORD']
        self.option = IQOption(email, password)
        _, reason = self.option.connect()  # connect to iq option
        if reason:
            raise ConnectionRefusedError(reason)

    def start(self, name, active, _type, buffersize=10, run_time=10):
        print("_____________subscribe_live_deal_______________")
        self.option.subscribe_live_deal(name, active, _type, buffersize)
        start_t = time.time()
        while True:
            # data size is below buffer size
            # data[0] is the last data
            data = self.option.get_live_deal(name, active, _type).cr_await
            print(f"Data: {data}")
            time.sleep(1)
            if time.time() - start_t > run_time:
                break
        print("_____________unsubscribe_live_deal_______________")
        self.option.unscribe_live_deal(name, active, _type)
