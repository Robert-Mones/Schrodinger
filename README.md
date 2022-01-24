# Schrodinger
3D-Printable quadrupedal robot driven by hobby servos.

![image](https://github.com/Robert-Mones/Schrodinger/blob/main/images/renders/isometric-v117.png)
![image](https://github.com/Robert-Mones/Schrodinger/blob/main/images/renders/isometric-standing-v91.png)

## About
Features
- 13 articulating joints with [standard-size hobby servo motors](https://www.sunfounder.com/products/metal-gear-digital-servo)
    - Each leg rotates at the knee and about two axes at the shoulder
    - Articulating neck
- On-board control system based around a [Teensy 4.1 microcontroller](https://www.pjrc.com/store/teensy41.html) operating a main control loop at 100Hz
    - Absolute orientation from a [fusion BNO055 IMU](https://www.adafruit.com/product/2472)
    - Medium-range (50-100ft), medium-bandwidth communication with a [2.4GHz NRFL01-based radio](https://www.amazon.com/gp/product/B00WG9HO6Q)
        - Bandwidth of the radio is fundamentally software-limited as only one 32-byte packet is received during every control loop
    - Servo control is offloaded to a [PCA9685-based servo driver](https://www.sunfounder.com/products/pca9685-servo-driver) and updated on every control loop
- On-board vision processing with a [JeVois vision camera](http://www.jevois.org/) and an [RGBW NeoPixel Ring](https://www.adafruit.com/product/2853) in the head
- On-board camera feed stream over WiFi with a [Raspberry Pi Zero 2 W](https://www.adafruit.com/product/5291)
- Entirely 3D-printed construction (plus some bolts & threaded inserts) 

## Progress
- [x] CAD Modelling
- [ ] Simulation (In progress)
- [ ] Control System Development
- [x] Fabrication & Assembly
- [ ] Electronics Development (In progress)
