#include "Arduino.h"
#include "Display.h"

Display_ Display;

void Display_::setup() {
    if(display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
        display.setTextSize(1);
        display.setTextColor(SSD1306_WHITE);
        display.setFont();
    } else {
        Serial.printf("Display initialization failed.\n");
    }

    writingNow = false;
    needsUpdate = true;
    lastUpdate = 0;
}

void Display_::loop() {
    uint32_t t = millis();
    if(needsUpdate && t >= lastUpdate + DISPLAY_TIME) {
        if(displayWriteLock.try_lock()) {
            // If display needs updating, first copy the data into a buffer
            displayDataLock.lock();
            for(int i = 0; i < 6; i++) {
                strncpy(displayBuffer[i], displayData[i], DISPLAY_WIDTH);
            }
            displayDataLock.unlock();

            // Then write to the display in a thread,
            //   unless we already have a thread working on it
            // threads.addThread(writeDisplay, this);
            for(int i = 0; i < 6; i++) {
                Serial.printf("%s\n", displayData[i]);
            }
        }

        lastUpdate = t;
    }
}

void Display_::updateDisplay(int i, const char *s, bool append) {
    // append is false by default
    uint32_t t1 = micros();
    displayDataLock.lock();

    if(append) {
        int8_t len = DISPLAY_WIDTH - strlen(displayData[i]);
        strncat(displayData[i], s, len);
    } else {
        strncpy(displayData[i], s, DISPLAY_WIDTH);
        displayData[i][DISPLAY_WIDTH] = 0;
    }
    displayDataLock.unlock();
    needsUpdate = true;

    uint32_t t2 = micros();
    if(t2 - t1 > 2) Serial.printf("Long display update: %d us", t2-t1);
}

void Display_::writeDisplay(void *t) {
    Display_ *this_ = (Display_*) t;
    // ~123 us
    this_->display.clearDisplay();
    for (int i = 0; i < 6; i++) {
        this_->display.setCursor(0, 1+(11*i));
        this_->display.write(this_->displayBuffer[i]);
    }

    // ~25600 us
    this_->display.display();

    this_->needsUpdate = false;
    this_->displayWriteLock.unlock();
}
