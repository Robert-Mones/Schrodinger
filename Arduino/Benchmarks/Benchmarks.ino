void setup() {
  Serial.begin(115200);
  delay(500);

  Serial.println("Hi");

  int x;
  long t1, t2;

  x = random(1000);
  t1 = micros();
  for(int i = 0; i < 1000; i++) {
    x += 1;
    x *= 2;
    x -= 2;
    x /= 2;
  }
  t2 = micros();

  Serial.print("1000x +*-/ :\t");
  Serial.println(t2 - t1);
}

void loop() {
  delay(1);
}
