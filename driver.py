import msgParser
import carState
import carControl
import keyboard
from csv import writer
import pickle

class Driver(object):
    '''
    A driver object for the SCRC
    '''

    def __init__(self, stage):
        '''Constructor'''
        self.WARM_UP = 0
        self.QUALIFYING = 1
        self.RACE = 2
        self.UNKNOWN = 3
        self.stage = stage
        
        self.parser = msgParser.MsgParser()
        
        self.state = carState.CarState()
        
        self.control = carControl.CarControl()
        
        self.steer_lock = 0.785398
        self.max_speed = 100
        self.prev_rpm = None
        # Addition to the driver class
        file = open('DecisionTreeRegressionModel', 'rb')
        self.model = pickle.load(file)
        file.close()
    
    def init(self):
        '''Return init string with rangefinder angles'''
        self.angles = [0 for x in range(19)]
        
        for i in range(5):
            self.angles[i] = -90 + i * 15
            self.angles[18 - i] = 90 - i * 15
        
        for i in range(5, 9):
            self.angles[i] = -20 + (i-5) * 5
            self.angles[18 - i] = 20 - (i-5) * 5
        
        return self.parser.stringify({'init': self.angles})
    
    def drive(self, msg):
        self.state.setFromMsg(msg)
        
        #self.steer()
        
        #self.gear()
        
        #self.speed()
        
        #self.brake()
        
        #with open('sensors.csv', 'a', newline='') as f_obj:
        #    writer_obj = writer(f_obj)
        li = [[self.state.sensors['angle'][0], self.state.sensors['curLapTime'][0], self.state.sensors['distFromStart'][0], self.state.sensors['distRaced'][0], self.state.sensors['focus'][0], self.state.sensors['gear'][0], self.state.sensors['lastLapTime'][0], self.state.sensors['opponents'][0], self.state.sensors['racePos'][0], self.state.sensors['rpm'][0], self.state.sensors['speedX'][0], self.state.sensors['speedY'][0], self.state.sensors['speedZ'][0], self.state.sensors['track'][0], self.state.sensors['trackPos'][0], self.state.sensors['wheelSpinVel'][0], self.state.sensors['z'][0]]]
        values = self.model.predict(li)
        self.control.setAccel(values[0][0])
        self.control.setBrake(values[0][1])
        self.control.setGear(values[0][2])
        self.control.setSteer(values[0][3])
        #    writer_obj.writerow(li)
        #    f_obj.close()
        
        return self.control.toMsg()
    
    def steer(self):
        angle = self.state.angle
        dist = self.state.trackPos
        if keyboard.is_pressed('left'): self.control.setSteer(0.5/self.steer_lock)#(angle - dist*0.5)/self.steer_lock)
        elif keyboard.is_pressed('right'): self.control.setSteer(-0.5/self.steer_lock)#(angle - dist*0.5)/self.steer_lock)
        else: self.control.setSteer(0)
        #self.control.setSteer((angle - dist*0.5)/self.steer_lock)
    
    def brake(self):
        brake = self.control.getBrake()
        if keyboard.is_pressed('down') and self.control.getGear() >= 1: # soft break
            brake += 0.1
            if brake > 0.5:
                brake = 0.5
        elif self.control.getGear() == -1 and keyboard.is_pressed('up'):
            brake = 1.0
        elif keyboard.is_pressed('space'):
            brake = 1.0
        else:
            brake = 0.0
        self.control.setBrake(brake);
        
    
    def gear(self):
        rpm = self.state.getRpm()
        gear = self.state.getGear()
        speed = self.state.getSpeedX()
        
        if self.prev_rpm == None:
            up = True
        else:
            if (self.prev_rpm - rpm) < 0:
                up = True
            else:
                up = False
        self.prev_rpm = rpm
        if rpm > 7000 and gear < 6:
            gear = gear + 1
        if rpm < 3000 and gear >= 2:
            gear = gear - 1
        if keyboard.is_pressed('n'):
            gear = 0
        if keyboard.is_pressed('s'):
            gear = -1
        #Failsafe keys for when gears fluctuate
        if keyboard.is_pressed('q'):
            gear = 1
        if keyboard.is_pressed('w'):
            gear = 2
        if keyboard.is_pressed('e'):
            gear = 3
        if keyboard.is_pressed('r'):
            gear = 4
        if keyboard.is_pressed('t'):
            gear = 5
        if keyboard.is_pressed('y'):
            gear = 6
        
        self.control.setGear(round(gear))
    
    def speed(self):
        speed = self.state.getSpeedX()
        accel = self.control.getAccel()
        
        if keyboard.is_pressed('up'): #speed < self.max_speed and
            if self.control.getGear() <= -1 and speed == 0:
                self.control.setGear(1)
            #accel += 0.1
            #if accel > 1:
            #    accel = 1.0
            accel = 1.0
        elif keyboard.is_pressed('down'):
            accel = -1.0
            if self.control.getGear() <= 1:
                self.control.setGear(-1)
                accel = 1.0
        else:
            accel = 0
        
        self.control.setAccel(accel)
            
        
    def onShutDown(self):
        pass
    
    def onRestart(self):
        pass
        