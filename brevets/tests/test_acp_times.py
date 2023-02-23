"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""
from acp_times import open_time, close_time
import nose    # Testing framework
import logging
import arrow
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

def test_brevet1():
    brevet_dist = 200.0
    brevet_start_time = arrow.get("2023-02-17 00:00", "YYYY-MM-DD HH:mm")
    checkpoints = {
            0: (brevet_start_time, brevet_start_time.shift(hours=0.0)),
            50: (brevet_start_time.shift(hours=0.0, minutes=0), brevet_start_time.shift(hours=0.0)),
#            100: (brevet_start_time.shift(hours=0.0, minutes=0), brevet_start_time.shift(hours=0.0)),
#            175: (brevet_start_time.shift(hours=0.0, minutes=0), brevet_start_time.shift(hours=0.0)),
#            200: (brevet_start_time.shift(hours=0.0, minutes=0), brevet_start_time.shift(hours=0.0)),
            }
    for km, times in checkpoints.items():
        start_time, end_time = times
        assert open_time(km, brevet_dist, brevet_start_time) == start_time
#        assert close_time(km, brevet_dist, brevet_start_time) == end_time, ""

#def test_brevet2():
#    brevet_dist = 300.0
#    brevet_start_time = arrow.get("2023-02-17 00:00", "YYYY-MM-DD HH:mm")
#    checkpoints = {
#            0: (brevet_start_time, brevet_start_time.shift(hours=1.0)),
#            50: (brevet_start_time.shift(hours=1.0, minutes= 12), brevet_start_time.shift(hours =2.0)),
#            100: (brevet_start_time.shift(hours= 1.0, minutes= 12), brevet_start_time.shift(hours=2.0)),
#            175: (brevet_start_time.shift(hours = 1.0, minutes = 12), brevet_start_time.shift(hours=2.0)),
#            200: (brevet_start_time.shift(hours = 1.0 , minutes = 12), brevet_start_time.shift(hours=2.0)),
#            300: (brevet_start_time.shift(hours=1.0, minutes=12), brevet_start_time.shift(hours=2.0)),
#            340: (brevet_start_time.shift(hours=1.0, minutes=12), brevet_start_time.shift(hours= 2.0)),
#            }
#    for km, times in checkpoints.items():
#        start_time, end_time = times
#        assert open_time(km, brevet_dist, brevet_start_time) == start_time
#        assert close_time(km, brevet_dist, brevet_start_time) == end_time

#def test_brevet3():
#    brevet_dist = 400.0
#    brevet_start_time = arrow.get("2023-02-17 00:00", "YYYY-MM-DD HH:mm")
#    checkpoints = {
#            0: (brevet_start_time, brevet_start_time.shift(hours=1.0)),
#            250: (brevet_start_time.shift(hours= 11.0, minutes=3), brevet_start_time.shift(hours=3.0)),
#            380: (brevet_start_time.shift(hours=11.0, minutes=3), brevet_start_time.shift(hours=3.0)),
#            400: (brevet_start_time.shift(hours=11.0, minutes=3), brevet_start_time.shift(hours=3.0)),
#            480: (brevet_start_time.shift(hours=11.0, minutes=3), brevet_start_time.shift(hours=3.0)),
#            }
#    for km, times in checkpoints.items():
#        start_time, end_time = times
#        #assert open_time(km, brevet_dist, brevet_start_time) == start_time
#        assert close_time(km, brevet_dist, brevet_start_time) == end_time

#def test_brevet4():
#    brevet_dist = 600.0
#    brevet_start_time = arrow.get("2023-02-17 00:00", "YYYY-MM-DD HH:mm")
#    checkpoints = {
#            0: (brevet_start_time, brevet_start_time.shift(hours=1.0)),
#            200: (brevet_start_time.shift(hours= 5.0, minutes=1), brevet_start_time.shift(hours=1.0)),
#            450: (brevet_start_time.shift(hours =5.0, minutes=1), brevet_start_time.shift(hours=1.0)),
#            600: (brevet_start_time.shift(hours= 5.0, minutes=1), brevet_start_time.shift(hours=1.0)),
#            720: (brevet_start_time.shift(hours = 5.0, minutes=1), brevet_start_time.shift(hours=1.0)),
#            }
#    for km, times in checkpoints.items():
#        start_time, end_time = times
#        assert open_time(km, brevet_dist, brevet_start_time) == start_time
#        assert close_time(km, brevet_dist, brevet_start_time) == end_time

#def test_brevet5():
#    brevet_dist = 1000.0
#    brevet_start_time = arrow.get("2023-02-17 00:00", "YYYY-MM-DD HH:mm")
#    checkpoints = {
#            0: (brevet_start_time, brevet_start_time.shift(hours=8.0)),
#            500: (brevet_start_time.shift(hours=20.00, minutes = 52), brevet_start_time.shift(hours=8.0)),
#            999: (brevet_start_time.shift(hours=20.0, minutes=52), brevet_start_time.shift(hours=8.0)),
#            1000: (brevet_start_time.shift(hours=20.0, minutes=52), brevet_start_time.shift(hours=8.0)),
#            1200: (brevet_start_time.shift(hours=20.00, minutes=52), brevet_start_time.shift(hours=8.0)),
#            }
#    for km, times in checkpoints.items():
#        start_time, end_time = times
#        assert open_time(km, brevet_dist, brevet_start_time) == start_time
        #assert close_time(km, brevet_dist, brevet_start_time) == end_time

#def test_brevet6():
#    brevet_dist = 1200.0 #invalid
#    brevet_start_time = arrow.get("2023-02-17 00:00", "YYYY-MM-DD HH:mm")
#    checkpoints = {
#            0: (brevet_start_time, brevet_start_time.shift(hours=1.0)),
#            50: (brevet_start_time.shift(hours, minutes), brevet_start_time.shift(hours)),
#            100: (brevet_start_time.shift(hours, minutes), brevet_start_time.shift(hours)),
#            175: (brevet_start_time.shift(hours, minutes), brevet_start_time.shift(hours)),
#            200: (brevet_start_time.shift(hours, minutes), brevet_start_time.shift(hours)),
#            }
#    for km, times in checkpoints.items():
#        start_time, end_time = times
#        assert open_time(km, brevet_dist, brevet_start_time) == start_time
#        assert close_time(km, brevet_dist, brevet_start_time) == end_time, ""

#def test_brevet7():
#    brevet_dist = 400.0
#    brevet_start_time = arrow.get("2023-02-17 00:00", "YYYY-MM-DD HH:mm")
#    checkpoints = {
#            0: (brevet_start_time, brevet_start_time.shift(hours=1.0)),
#            50: (brevet_start_time.shift(hours, minutes), brevet_start_time.shift(hours)),
#            400: (brevet_start_time.shift(hours, minutes), brevet_start_time.shift(hours)),
#            480: (brevet_start_time.shift(hours, minutes), brevet_start_time.shift(hours)),
#            500: (brevet_start_time.shift(hours, minutes), brevet_start_time.shift(hours)),
#            }
#    for km, times in checkpoints.items():
#        if km < 500:
#            start_time, end_time = times
#            assert open_time(km, brevet_dist, brevet_start_time) == start_time
#            assert close_time(km, brevet_dist, brevet_start_time) == end_time, ""
#        else:
#            assert open_time(km, brevet_dist, brevet_start_time) == 403
#            assert close_time(km, brevet_dist, brevet_start_time) == 403
