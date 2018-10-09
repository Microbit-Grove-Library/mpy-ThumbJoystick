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


if __name__ == '__main__':
    joystick = Joystick(pin0, pin1)

    x = 2
    y = 2
    now = 0

    while True:
        now = joystick.read()
        if now == 1:    
            # up
            y -= 1
        elif now == 2:
            y += 1
        elif now == 3:
            x -= 1
        elif now == 4:
            x += 1
        elif now == 5:
            x -= 1
            y -= 1
        elif now == 6:
            x -= 1
            y += 1
        elif now == 7:
            x += 1
            y -= 1
        elif now == 8:
            x += 1
            y += 1
        
        if x == -1:
            x = 0
        elif x == 5:
            x = 4
        
        if y == -1:
            y = 0
        elif y == 5:
            y = 4

        line = ["00000:","00000:","00000:","00000:","00000:"]
        if x == 0:
            line[y] = '90000:'
        elif x == 1:
            line[y] = '09000:'
        elif x == 2:
            line[y] = '00900:'
        elif x == 3:
            line[y] = '00090:'
        elif x == 4:
            line[y] = '00009:'
        
        display.show(Image(line[0]+line[1]+line[2]+line[3]+line[4]))
        sleep(100)