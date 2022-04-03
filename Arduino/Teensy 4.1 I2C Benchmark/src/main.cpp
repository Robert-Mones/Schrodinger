#include <Arduino.h>
#include <Wire.h>

// Display
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <Fonts/FreeMonoBold9pt7b.h>

// IMU
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

// Servos
#include <Adafruit_PWMServoDriver.h>

// Current Sensor
#include <Adafruit_INA260.h>

// Threading
#include <TeensyThreads.h>

/* Adafruit_SSD1306 display = Adafruit_SSD1306(128, 64, &Wire2, -1, 400000L, 400000L);

void displaySetup() {
  if(display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    display.setTextSize(1);
    display.setTextColor(SSD1306_WHITE);
    display.setFont();

    display.clearDisplay();
    display.display();
  } else {
    Serial.printf("Display initialization failed.\n");
  }
}

void displayLoop() {
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

  //Serial.printf("Timing\t%lu\t%lu\t%lu\n", t2-t1, t3-t2, t4-t3);
} */

/* Adafruit_BNO055 bno = Adafruit_BNO055(55, 40U, &Wire);

void IMUSetup() {
  if(bno.begin()) {
    bno.setExtCrystalUse(true);
    Wire.setClock(400000);
  } else {
    Serial.printf("IMU begin failed\n");
  }
}

void IMULoop() {
  uint32_t t1 = 0, t2 = 0;

  t1 = micros();
  sensors_event_t event; 
  bno.getEvent(&event);
  t2 = micros();
  
  // Display the floating point data
  Serial.printf("X: %.4f\tY: %.4f\tZ: %.4f\tt: %lu\n",
    event.orientation.x, event.orientation.y, event.orientation.z, t2-t1);
} */

/* Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(64U, Wire1);

void servoSetup() {
  pwm.begin();
  pwm.setOscillatorFrequency(27000000);
  pwm.setPWMFreq(50);
  Wire1.setClock(400000);
}

void servoLoop() {
  uint32_t t1, t2;

  t1 = micros();
  for(int i = 0; i < 16; i++) {
    pwm.setPWM(i, 0, 117 + 
      (int)((120.0 * t1)/1000000.0) % 360);
  }
  t2 = micros();

  Serial.printf("Servo time: %lu\n", t2-t1);
} */

/* Adafruit_INA260 ina260 = Adafruit_INA260();

void currentSetup() {
  if(ina260.begin(64U, &Wire1)) {
    Wire1.setClock(400000);
  } else {
    Serial.printf("Couldn't find current sensor.\n");
  }
}

void currentLoop() {
  float current, voltage, power;
  uint32_t t1, t2;

  t1 = micros();
  current = ina260.readCurrent();
  voltage = ina260.readBusVoltage();
  power = ina260.readPower();
  t2 = micros();

  Serial.printf("Power: %.2f\t%.2f\t%.2f\t%lu\n", current, voltage, power, t2-t1);
} */

/*  Unthreaded SSD1306:
 *    100kHz w/ 2kO:   99kHz actual   100700us
 *    400kHz:         338kHz actual    29600us
 *    400kHz w/ 2kO:  375kHz actual    26700us
 *    800kHz w/ 2kO:  375kHz actual    26700us
 *    800kHz w/ 1kO:  375kHz actual    26700us
 *    400kHz w/ 330O: 400kHz actual    25000us
 *    800kHz w/ 330O: 400kHz actual    25000us -- definitely software limited by SSD1306 chip
 */

/*  Unthreaded BNO055:
 *    100kHz w/ 2kO:   98kHz actual   1000-2000us
 *    400kHz w/ 2kO:  370kHz actual   300-2000us
 */

/*  Unthreaded PCA9685:
 *    100kHz w/ 1kO:  100kHz actual   1700us
 *    400kHz w/ 1kO:  400kHz actual   500us
 */

/*  Unthreaded INA260:
 *    100kHz w/ 0kO:   94kHz actual   1500us
 *    100kHz w/ 1kO:  100kHz actual   1500us
 *    400kHz w/ 1kO:  387kHz actual    400us
 *    800kHz w/ 1kO:  387kHz actual    400us
 */

void setup() {
  // displaySetup();
  // IMUSetup();
  // servoSetup();
  // currentSetup();

  delay(3000);
}

void loop() {
  // displayLoop();
  // IMULoop();
  // servoLoop();
  // currentLoop();

  delay(100);
}