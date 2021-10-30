#include "Arduino.h"
#include "Communication.h"

Communication_ Communication;

void Communication_::setup() {
    Serial.begin(115200);
}

void Communication_::loop() {
    Display.updateDisplay(2, "IP Addr: 192.168.0.12");
}
