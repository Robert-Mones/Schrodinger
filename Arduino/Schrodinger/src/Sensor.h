// File to manage reading and processing data from the IMU, JeVois, and other sensors on the robot.
#ifndef Sensor_h
#define Sensor_h

#include "Arduino.h"
#include <Bounce2.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#include <Adafruit_INA260.h>
#include <TeensyThreads.h>

#include "Display.h"

#define ENABLE_BUTTON 30

#define IMU_SAMPLE_DELAY 10000 // us between IMU samples
#define POWER_SAMPLE_DELAY 10000 // us between power sensor samples

#define POWER_SENSOR_ENABLE true

class Sensor_ {
    public:
        void setup();
        void loop();
    
        Button enableButton;
        float battVoltage;
        float battCurrent;
    
    private:
        Adafruit_BNO055 bno = Adafruit_BNO055(55, 0x28);
        Adafruit_INA260 ina260 = Adafruit_INA260();

        volatile bool enabled;
        volatile uint32_t lastReadTime;
        Threads::Mutex IMUdataLock;
        Threads::Mutex IMUreadLock;
        float x, y, z;
        uint8_t syscal, gyrocal, accelcal, magcal;

        uint32_t lastPowerReadTime;

        static void IMUloop(void *t);
};
extern Sensor_ Sensor;

#endif
