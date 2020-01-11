#include <Servo.h>

Servo s1, s2, s3, s4, s5, s6, s7, s8;
  int INITIAL_VALUE_HIP = 85;
  int INITIAL_VALUE_KNEE = 25;
  int FINAL_VALUE_KNEE = 40;

void setup() {

  s1.attach(13);
  s2.attach(12);
  s3.attach(11);
  s4.attach(10);
  s5.attach(9);
  s6.attach(8);
  s7.attach(7);
  s8.attach(6);
  
    delay(1000);
  
  s1.write(INITIAL_VALUE_HIP);
  s3.write(INITIAL_VALUE_HIP);
  s5.write(INITIAL_VALUE_HIP);
  s7.write(INITIAL_VALUE_HIP);

  s2.write(INITIAL_VALUE_KNEE);
  s4.write(INITIAL_VALUE_KNEE);
  s6.write(INITIAL_VALUE_KNEE);
  s8.write(INITIAL_VALUE_KNEE);



}

void loop() {
  
    delay(5000);
  
  s2.write(FINAL_VALUE_KNEE);
  s4.write(FINAL_VALUE_KNEE);
  s6.write(FINAL_VALUE_KNEE);
  s8.write(FINAL_VALUE_KNEE);



  delay(5000);
  

  s2.write(INITIAL_VALUE_KNEE);
  s4.write(INITIAL_VALUE_KNEE);
  s6.write(INITIAL_VALUE_KNEE);
  s8.write(INITIAL_VALUE_KNEE);
  


}
