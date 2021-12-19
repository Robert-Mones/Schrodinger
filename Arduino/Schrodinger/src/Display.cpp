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

    needsUpdate = true;
    lastUpdate = 0;
}

void Display_::loop() {
    uint32_t t = millis();
    if(needsUpdate && (((t - lastUpdate) >= DISPLAY_TIME) || t < lastUpdate)) {
        // If display needs updating, update display
        writeDisplay();
        
        lastUpdate = t;
        Serial.printf("Display update time: %d\n", millis() - t);
    }
}

void Display_::updateDisplay(int i, const char *s, bool append) {
    // append is false by default
    if(append) {
        int8_t len = DISPLAY_WIDTH - strlen(displayData[i]);
        strncat(displayData[i], s, len);
    } else {
        strncpy(displayData[i], s, DISPLAY_WIDTH);
        displayData[i][DISPLAY_WIDTH] = 0;
    }
    needsUpdate = true;
}

void Display_::writeDisplay() {
    display.clearDisplay();
    for (int i = 0; i < 6; i++) {
        display.setCursor(0, 1+(11*i));
        display.write(displayData[i]);
    }
    display.display();

    needsUpdate = false;
}
