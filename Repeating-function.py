import sched
import time

i_repeat = 5


countdown = sched.scheduler(time.time, time.sleep)


# The function to be repeated.
# Incirments 'i_repeat' to limit the amount of repeats

def repeater():
    global i_repeat
    if i_repeat > 0:
        print(i_repeat)
        i_repeat = i_repeat - 1
        countdown.enter(1, 1, repeater)

countdown.enter(1, 1, repeater)
countdown.run()


