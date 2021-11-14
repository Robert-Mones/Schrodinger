#include <Arduino.h>
#include "USBHost_t36.h"

USBHost myusb;
USBHIDParser hid1(myusb);
JoystickController joystick(myusb);

int user_axis[64];
uint32_t buttons_prev = 0;

USBDriver *driver = &hid1;
const char *driver_name = "HID1";
bool driver_active = false;

// Lets also look at HID Input devices
USBHIDInput *hiddriver = &joystick;
const char *hid_driver_name = "joystick";
bool hid_driver_active = false;

bool show_changed_only = false;

uint8_t joystick_left_trigger_value = 0;
uint8_t joystick_right_trigger_value = 0;
uint64_t joystick_full_notify_mask = (uint64_t) - 1;

int psAxis[64];

uint32_t tlast = 0;
struct {
  uint16_t touch[2];
  uint16_t buttons;
  uint8_t axes[7];
} payload;

// Helper functions
void PrintDeviceListChanges() {
  if (*driver != driver_active) {
    driver_active = !driver_active;
  }

  if (*hiddriver != hid_driver_active) {
    hid_driver_active = !hid_driver_active;
  }
}

// Main fnuctions
void setup() {
  Serial1.begin(2000000);
  
  Serial.println("\n\nUSB Host Joystick Testing");
  myusb.begin();
}

void loop() {
  myusb.Task();
  PrintDeviceListChanges();

  if(joystick.available()) {
    // Have joystick data to read, package, and transmit
    uint32_t t1 = micros();

    uint32_t buttons = joystick.getButtons();

    // Pack axes
    payload.axes[0] = joystick.getAxis(0);
    payload.axes[1] = joystick.getAxis(1);
    payload.axes[2] = joystick.getAxis(2);
    payload.axes[3] = joystick.getAxis(5);
    payload.axes[4] = joystick.getAxis(3);
    payload.axes[5] = joystick.getAxis(4);
    payload.axes[6] = joystick.getAxis(9);

    // Pack buttons
    payload.buttons = buttons & 0x0fffffff;
    payload.buttons |= (1-(joystick.getAxis(35) >> 7)) << 14;

    // Pack touch inputs
    payload.touch[0] = ((joystick.getAxis(37) & 0x0f) << 8)
      | joystick.getAxis(36);
    payload.touch[1] = joystick.getAxis(38) << 4
      | ((joystick.getAxis(37) & 0xf0) >> 4);

    joystick.joystickDataClear();

    // TODO: Transmit payload via radio

    uint32_t t2 = micros();

    Serial.printf("Axes: %d, %d | %d, %d | %d, %d | %d\n",
      payload.axes[0], payload.axes[1], payload.axes[2], 
      payload.axes[3], payload.axes[4], payload.axes[5],
      payload.axes[6]);
    Serial.printf("Buttons: ");
    for(int i = 0; i < 16; i++) {
      uint32_t k = (payload.buttons >> (15-i)) & 1;
      Serial.printf("%d", k);
    }
    Serial.printf("\n");
    Serial.printf("Touch: %d, %d\n",
      payload.touch[0], payload.touch[1]);
    Serial.printf("Time: %d, %d\n\n", t2-t1, t2-tlast);
    tlast = t2;
  }
}
