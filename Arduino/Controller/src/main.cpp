/* PS4/RF24 Controller for Schrodinger
 * Some code taken from examples available in RF24 and USBHost_t36.h libraries
*/
#include <Arduino.h>
#include "USBHost_t36.h"
#include "RF24.h"

// #define DEBUG
#define SERIAL

// Joystick globals
USBHost myusb;
USBHIDParser hid1(myusb);
JoystickController joystick(myusb);

USBDriver *driver = &hid1;
const char *driver_name = "HID1";
bool driver_active = false;

USBHIDInput *hiddriver = &joystick;
const char *hid_driver_name = "joystick";
bool hid_driver_active = false;

uint32_t tlast = 0;
struct {
  uint16_t touch[2];
  uint16_t buttons;
  int16_t accel[3];
  uint8_t axes[7];
} payload; // 19 bytes, 20 actual

// Radio globals
RF24 radio(7, 8); // CE, CSN

const uint8_t *inaddr = (const uint8_t*) "CIRO0";  // Controller in, robot out
const uint8_t *outaddr = (const uint8_t*) "CORI0"; // Controller out, robot in

// Main functions
void setup() {
  Serial.begin(1000000);
  Serial1.begin(2000000);

  Serial.printf("Schrodinger Controller\n");
  Serial.printf("Payload size: %d bytes\n", sizeof(payload));

  // Setup USB
  myusb.begin();

  // Setup radio
  digitalWrite(0, LOW);
  if(!radio.begin()) {
    Serial.printf("Radio not connected\n");
    while(true) {}
  }
  radio.setPALevel(RF24_PA_MAX);
  radio.setPayloadSize(sizeof(payload));
  radio.setRetries(5, 15);

  radio.openWritingPipe(outaddr);
  radio.openReadingPipe(1, inaddr);
  radio.stopListening();
}

void loop() {
  myusb.Task();
  
  // Process joystick connection changes
  if (*driver != driver_active)
    driver_active = !driver_active;
  if (*hiddriver != hid_driver_active)
    hid_driver_active = !hid_driver_active;

  if(joystick.available()) {
    // Have joystick data to read, package, and transmit
    uint32_t t1 = micros();

    uint32_t buttons = joystick.getButtons();

    // Pack the accel inputs
    payload.accel[0] = (int16_t)(joystick.getAxis(20) << 8) | joystick.getAxis(19);
    payload.accel[1] = (int16_t)(joystick.getAxis(22) << 8) | joystick.getAxis(21);
    payload.accel[2] = (int16_t)(joystick.getAxis(24) << 8) | joystick.getAxis(23);

    // Pack touch inputs
    payload.touch[0] = ((joystick.getAxis(37) & 0x0f) << 8)
      | joystick.getAxis(36);
    payload.touch[1] = joystick.getAxis(38) << 4
      | ((joystick.getAxis(37) & 0xf0) >> 4);

    // Pack buttons
    payload.buttons = buttons & 0x0fffffff;
    payload.buttons |= (1-(joystick.getAxis(35) >> 7)) << 14;

    // Pack axes
    payload.axes[0] = joystick.getAxis(0);
    payload.axes[1] = 255 - joystick.getAxis(1);
    payload.axes[2] = joystick.getAxis(2);
    payload.axes[3] = 255 - joystick.getAxis(5);
    payload.axes[4] = joystick.getAxis(3);
    payload.axes[5] = joystick.getAxis(4);
    payload.axes[6] = joystick.getAxis(9);

    joystick.joystickDataClear();

    // Transmit payload via radio
    bool trans = radio.write(&payload, sizeof(payload));
    (void)trans;

    #ifdef SERIAL
    Serial.printf("%d,%d,%d,%d,%d,",
      payload.accel[0], payload.accel[1], payload.accel[2],
      payload.touch[0], payload.touch[1]);
    for(int i = 0; i < 16; i++) {
      uint32_t k = (payload.buttons >> (15-i)) & 1;
      Serial.printf("%d", k);
    }
    Serial.printf(",%d,%d,%d,%d,%d,%d,%d\n",
      payload.axes[0], payload.axes[1], payload.axes[2], payload.axes[3],
      payload.axes[4], payload.axes[5], payload.axes[6]);
    #endif

    #ifdef DEBUG
    // Wrap up and print the result if DEBUG is on
    uint32_t t2 = micros();
    
    Serial.printf("Pitch: %d,\t%d,\t%d\n", payload.accel[0], payload.accel[1], payload.accel[2]);
    Serial.printf("Touch: %d, %d\n", payload.touch[0], payload.touch[1]);
    Serial.printf("Time: %d, %d\n", t2-t1, t2-tlast);
    Serial.printf("Buttons: ");
    for(int i = 0; i < 16; i++) {
      uint32_t k = (payload.buttons >> (15-i)) & 1;
      Serial.printf("%d", k);
    }
    Serial.printf("\n");
    Serial.printf("Axes: %d, %d | %d, %d | %d, %d | %d\n",
      payload.axes[0], payload.axes[1], payload.axes[2], 
      payload.axes[3], payload.axes[4], payload.axes[5],
      payload.axes[6]);
    if(trans) Serial.printf("Transmission successful.\n\n");
    else Serial.printf("Transmission failed.\n\n");
    
    tlast = t2;
    #endif
  }
}
