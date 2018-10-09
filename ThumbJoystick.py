from microbit import *

class Joystick:
    # xpin and ypin should only be P0, P1, P2
    def __init__(self, xpin, ypin):
        self.xPin = xpin;
        self.yPin = ypin;

    def read(self):
        xdata = self.xPin.read_analog()
        ydata = self.yPin.read_analog()
        result = 0
        # press
        if xdata > 1000:
            result = 9
        elif xdata > 600:
            if ydata > 600: 
                # upper right
                result = 7
            elif ydata < 400:
                # lower right
                result = 8
            else: 
                # right
                result = 4
        elif xdata < 400:
            if ydata > 600:
                # upper left
                result = 5
            elif ydata < 400:
                # lower left
                result = 6
            else: 
                # left
                result = 3
        else:
            if ydata > 600:
                # up
                result = 1
            elif ydata < 400:
                # down
                result = 2
            else:
                result = 0
            
        return result