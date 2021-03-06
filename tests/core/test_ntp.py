# Distributed under the MIT software license, see the accompanying
# file LICENSE or http://www.opensource.org/licenses/mit-license.php.
from unittest import TestCase

import ntplib

from qrl.core import logger, ntp
from qrl.core.ntp import getNTP, get_ntp_response, setDrift, getTime

logger.initialize_default(force_console_output=True)


class TestNTP(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestNTP, self).__init__(*args, **kwargs)

    def test_getNTP(self):
        ntp = getNTP()
        self.assertIsNotNone(ntp)
        self.assertNotEqual(0, ntp)

    def test_get_ntp_response(self):
        response = get_ntp_response()
        self.assertTrue(isinstance(response, ntplib.NTPStats))

    def test_set_drift(self):
        ntp.drift = 0
        setDrift()
        print(ntp.drift)
        self.assertNotEqual(0, ntp.drift)

    def test_getTime(self):
        setDrift()
        time = getTime()
        self.assertIsNotNone(time)
