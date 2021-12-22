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

    lastReadTime = 0;
    x = 0.0;
    y = 0.0;
    z = 0.0;
    syscal = 0;
    gyrocal = 0;
    accelcal = 0;
    magcal = 0;
    
    Display.updateDisplay(1, "Batt Voltage: 13.56V"); // Example

    //threads.addThread()
}

void Sensor_::loop() {
    enableButton.update();
    
    // Read IMU data
    uint32_t t = micros();
    if(enabled && t >= lastReadTime + IMU_SAMPLE_DELAY) {
        sensors_event_t evt;
        bno.getEvent(&evt);
        x = evt.orientation.x;
        y = evt.orientation.y;
        z = evt.orientation.z;

        uint32_t t2 = micros();

        uint8_t sys = 0, gyro = 0, accel = 0, mag = 0;
        bno.getCalibration(&sys, &gyro, &accel, &mag);
        syscal = sys;
        gyrocal = gyro;
        accelcal = accel;
        magcal = mag;

        uint32_t t3 = micros();

        Display.updateDisplay(3, "IMU Enabled");
        char buf[DISPLAY_WIDTH+1];
        snprintf(buf, DISPLAY_WIDTH+1, " (%d/%d/%d/%d)",
            syscal, gyrocal, accelcal, magcal);
        Display.updateDisplay(3, buf, true);

        //Serial.printf("IMU: %f %f %f [%d/%d/%d/%d] (%d/%d/%d us)\n", x, y, z, syscal, gyrocal, accelcal, magcal, t2-t, t3-t2, micros()-t3);
        lastReadTime = t;
    }
}

/*
void Sensor_::IMUloop(void *t) {
    Sensor_ *this_ = (Sensor_*) t;

    while(true) {
        if(enabled) {
            uint32_t t = micros();
            if(t >= lastReadTime + IMU_SAMPLE_DELAY) {
                sensors_event_t evt;
                bno.getEvent(&evt);
                x = evt.orientation.x;
                y = evt.orientation.y;
                z = evt.orientation.z;

                uint32_t t2 = micros();

                uint8_t sys = 0, gyro = 0, accel = 0, mag = 0;
                bno.getCalibration(&sys, &gyro, &accel, &mag);
                syscal = sys;
                gyrocal = gyro;
                accelcal = accel;
                magcal = mag;

                uint32_t t3 = micros();

                Display.updateDisplay(3, "IMU Enabled");
                char buf[DISPLAY_WIDTH+1];
                snprintf(buf, DISPLAY_WIDTH+1, " (%d/%d/%d/%d)",
                    syscal, gyrocal, accelcal, magcal);
                Display.updateDisplay(3, buf, true);

                //Serial.printf("IMU: %f %f %f [%d/%d/%d/%d] (%d/%d/%d us)\n", x, y, z, syscal, gyrocal, accelcal, magcal, t2-t, t3-t2, micros()-t3);
                lastReadTime = t;
            }
        }
    }
}
*/