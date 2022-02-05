#include <Arduino.h>

// Display
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <Fonts/FreeMonoBold9pt7b.h>

Adafruit_SSD1306 display = Adafruit_SSD1306(128, 64, &Wire2, -1, 400000L, 400000L);

void writeDisplay() {
  uint32_t t1 = 0, t2 = 0, t3 = 0, t4 = 0;

  t1 = micros();
  char buf[50];
  sprintf(buf, "Test %lu", millis());

  t2 = micros();
  display.clearDisplay();
  for(int i = 0; i < 6; i++) {
    display.setCursor(0, 1 + (11*i));
    display.write(buf);
  }

  t3 = micros();
  display.display();
  t4 = micros();

  Serial.printf("Timing\t%lu\t%lu\t%lu\n", t2-t1, t3-t2, t4-t3);
}

/*  Results:
 *    100kHz w/ 2kO:   99kHz actual   100700us
 *    400kHz:         338kHz actual    29600us
 *    400kHz w/ 2kO:  375kHz actual    26700us
 *    800kHz w/ 2kO:  375kHz actual    26700us
 *    800kHz w/ 1kO:  375kHz actual    26700us
 *    400kHz w/ 330O: 400kHz actual    25000us
 *    800kHz w/ 330O: 400kHz actual    25000us -- definitely software limited by SSD1306 chip
 */

void setup() {
  if(display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    display.setTextSize(1);
    display.setTextColor(SSD1306_WHITE);
    display.setFont();

    display.clearDisplay();
    display.display();
  } else {
    Serial.printf("Display initialization failed.\n");
  }

  delay(3000);
}

void loop() {
  writeDisplay();

  delay(3000);
}