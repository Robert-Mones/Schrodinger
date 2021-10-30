#include "Arduino.h"
#include "Communication.h"

Communication_ Communication;

void Communication_::setup() {
    Serial.begin(115200);
}

void Communication_::loop() {

}
