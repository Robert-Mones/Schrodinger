#include "Arduino.h"
#include "Sensor.h"

Sensor_ Sensor;

void Sensor_::setup() {
    enableButton = Button();
    
    enableButton.attach(ENABLE_BUTTON, INPUT_PULLUP);
    enableButton.interval(10);
    enableButton.setPressedState(LOW);

    enabled = bno.begin();
    if(!enabled) Display.updateDisplay(3, "IMU Disabled");
    bno.setExtCrystalUse(true);

    if(!ina260.begin(64, &Wire1)) {
        Serial.printf("Couldn't find current sensor.\n");
    }

    lastReadTime = 0;
    x = 0.0;
    y = 0.0;
    z = 0.0;
    syscal = 0;
    gyrocal = 0;
    accelcal = 0;
    magcal = 0;
    
    battVoltage = 0.0;
    lastPowerReadTime = 0;
    
    Display.updateDisplay(1, "Batt Voltage: --"); // Example

    //threads.addThread(IMUloop, this);
}

void Sensor_::loop() {
    uint32_t t = micros();
    enableButton.update();

    if(POWER_SENSOR_ENABLE && t >= lastPowerReadTime + POWER_SAMPLE_DELAY) {
        battVoltage = ina260.readBusVoltage();
        battCurrent = ina260.readCurrent();

        char buf[DISPLAY_WIDTH+1];
        snprintf(buf, DISPLAY_WIDTH+1, "Batt Voltage: %.2f V",
            battVoltage/1000.0);
        Display.updateDisplay(1, buf);
        lastPowerReadTime = t;
    }

    if(t >= lastReadTime + IMU_SAMPLE_DELAY) {
        sensors_event_t evt;
        uint8_t sys = 0, gyro = 0, accel = 0, mag = 0;
        lastReadTime = t;
        

        IMUreadLock.lock();
        bno.getEvent(&evt);
        bno.getCalibration(&sys, &gyro, &accel, &mag);
        IMUreadLock.unlock();


        IMUdataLock.lock();
        x = evt.orientation.x;
        y = evt.orientation.y;
        z = evt.orientation.z;

        syscal = sys;
        gyrocal = gyro;
        accelcal = accel;
        magcal = mag;
        IMUdataLock.unlock();
    }
    
    /*Display.updateDisplay(3, "IMU Enabled");
    char buf[DISPLAY_WIDTH+1];
    snprintf(buf, DISPLAY_WIDTH+1, " (%d/%d/%d/%d)",
        syscal, gyrocal, accelcal, magcal);
    Display.updateDisplay(3, buf, true);*/
}

void Sensor_::IMUloop(void *t) {
    Sensor_ *this_ = (Sensor_*) t;

    while(true) {
        if(this_->enabled) {
            uint32_t t = micros();
            if(t >= this_->lastReadTime + IMU_SAMPLE_DELAY) {
                sensors_event_t evt;
                uint8_t sys = 0, gyro = 0, accel = 0, mag = 0;
                this_->lastReadTime = t;
                

                this_->IMUreadLock.lock();
                this_->bno.getEvent(&evt);
                this_->bno.getCalibration(&sys, &gyro, &accel, &mag);
                this_->IMUreadLock.unlock();


                this_->IMUdataLock.lock();
                this_->x = evt.orientation.x;
                this_->y = evt.orientation.y;
                this_->z = evt.orientation.z;

                this_->syscal = sys;
                this_->gyrocal = gyro;
                this_->accelcal = accel;
                this_->magcal = mag;
                this_->IMUdataLock.unlock();
            }
        }

        threads.delay(1);
    }
}
