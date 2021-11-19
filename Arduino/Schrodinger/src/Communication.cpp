#include "Arduino.h"
#include "Communication.h"

Communication_ Communication;

void Communication_::setup() {
    Serial.begin(115200);

    if(!radio.begin()) {
        Display.updateDisplay(5, "Radio Error");
    } else {
        Display.updateDisplay(5, "Radio Working");
        radio.setPALevel(RF24_PA_MAX);
        radio.setPayloadSize(sizeof(outpayload));
        //radio.setAddressWidth(3);
        //radio.openWritingPipe(outaddr);
        //radio.openReadingPipe(1, inaddr);
        radio.openWritingPipe(address[1]);
        radio.openReadingPipe(1, address[0]);
        radio.startListening();

        connected = radio.isChipConnected();
        Display.updateDisplay(2, connected ? "Radio Enabled" : "Radio Disabled");
    }

    Display.updateDisplay(3, "No Packets Recieved");
}

void Communication_::loop() {
    bool connectedNow = radio.isChipConnected();
    if(connectedNow != connected) {
        connected = connectedNow;
        Display.updateDisplay(2, connected ? "Radio Enabled" : "Radio Disabled");
    }

    uint8_t pipe;
    if(radio.available(&pipe)) {
        inpayload inBuf;
        uint8_t bytes = radio.getPayloadSize();
        radio.read(&inBuf, bytes);
        
        char buf[DISPLAY_WIDTH+1];
        snprintf(buf, DISPLAY_WIDTH+1, "0x%x", inBuf.buttons);
        Display.updateDisplay(3, "Recieved: ");
        Display.updateDisplay(3, buf, true);
    }
}

bool Communication_::getConnected() {
    return connected;
}
