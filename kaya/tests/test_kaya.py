from unittest import TestCase

import kaya

class TestKaya(TestCase):
    def test_kaya_equ(self):
        res = kaya.cal_kaya(82.4, 44, 5, 0.05)
        real_res = 0.0
        self.assertAlmostEqual(res, real_res)
