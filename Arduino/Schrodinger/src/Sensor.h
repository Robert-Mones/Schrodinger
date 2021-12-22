// File to manage reading and processing data from the IMU, JeVois, and other sensors on the robot.
#ifndef Sensor_h
#define Sensor_h

#include "Arduino.h"
#include <Bounce2.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#include <TeensyThreads.h>

#include "Display.h"

#define ENABLE_BUTTON 31

#define IMU_SAMPLE_DELAY 10000 // us between IMU samples

class Sensor_ {
    public:
        void setup();
        void loop();
    
        Button enableButton;
    
    private:
        Adafruit_BNO055 bno = Adafruit_BNO055(55, 0x28);

        bool enabled;
        uint32_t lastReadTime;
        Threads::Mutex IMUdataLock;
        Threads::Mutex IMUreadLock;
        float x, y, z;
        uint8_t syscal, gyrocal, accelcal, magcal;

        void IMUloop(void *t);
};
extern Sensor_ Sensor;

#endif
