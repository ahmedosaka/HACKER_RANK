#include <Wire.h>
#include <PololuMaestro.h>  //ライブラリの読み込み
#ifdef SERIAL_PORT_HARDWARE_OPEN
  #define maestroSerial SERIAL_PORT_HARDWARE_OPEN
#else
  #include <SoftwareSerial.h>
  SoftwareSerial maestroSerial(0, 1);
#endif
MiniMaestro maestro(maestroSerial);
void setup()
{
  maestroSerial.begin(9600);
  maestro.setSpeed(0, 20);  
  maestro.setAcceleration(0, 5); 
  maestro.setSpeed(1, 20);  
  maestro.setAcceleration(1, 5);
  maestro.setSpeed(2, 20);  
  maestro.setAcceleration(2, 5);
  maestro.setSpeed(3, 20);  
  maestro.setAcceleration(3, 5);  
  maestro.setSpeed(4, 20);  
  maestro.setAcceleration(4, 10); 
  maestro.setSpeed(5, 20);  
  maestro.setAcceleration(5, 5); 
  maestro.setTarget(5, 5400);
  maestro.setSpeed(6, 20);  
  maestro.setAcceleration(6, 5); 
  maestro.setTarget(6, 5400);
  delay(1000);
}
void loop()
{ 
  
  maestro.setSpeed(0, 20);  
  maestro.setAcceleration(0, 5); 
  maestro.setSpeed(1, 20);  
  maestro.setAcceleration(1, 5);
  maestro.setSpeed(2, 20);  
  maestro.setAcceleration(2, 5);
  maestro.setSpeed(3, 20);  
  maestro.setAcceleration(3, 5);  
  maestro.setSpeed(4, 20);  
  maestro.setAcceleration(4, 10); 
  maestro.setSpeed(5, 20);  
  maestro.setAcceleration(5, 5); 
  maestro.setSpeed(6, 20);  
  maestro.setAcceleration(6, 5); 


  maestro.setTarget(4, 5500);
  maestro.setTarget(0, 6000); 
  maestro.setTarget(1, 6000); 
  maestro.setTarget(2, 6000); 
  maestro.setTarget(3, 6000);

  delay(500);  
  maestro.setTarget(4, 5300);
  maestro.setTarget(0, 5000);
  maestro.setTarget(1, 6500);
  maestro.setTarget(2, 6800);
  maestro.setTarget(3, 7000);
 
  delay(500);
  
  maestro.setTarget(0, 7000); 
  maestro.setTarget(1, 6000); 

  delay(500); 
  
  maestro.setTarget(4, 5500);
  maestro.setTarget(0, 6000); 
  maestro.setTarget(1, 6000); 
  maestro.setTarget(2, 6000);
  maestro.setTarget(3, 6000);

  delay(500);  
  maestro.setTarget(4, 5700);
  maestro.setTarget(0, 5000);
  maestro.setTarget(1, 4800);
  maestro.setTarget(2, 6500);
  maestro.setTarget(3, 4700);

  delay(500);
  
  maestro.setTarget(2, 6000); 
  maestro.setTarget(3, 6000); 
  
  delay(500);
}
