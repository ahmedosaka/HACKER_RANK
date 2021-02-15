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
//  maestro.setSpeed(4, 20);  
//  maestro.setAcceleration(4, 10);
//  maestro.setTarget(4, 5500);
//  maestro.setSpeed(5, 20);  
//  maestro.setAcceleration(0, 5);
//  maestro.setSpeed(6, 20);  
//  maestro.setAcceleration(0, 5);
//  maestro.setTarget(5, 3008);
//  maestro.setTarget(6, 9024);
//  delay(3000);
//  
//  maestro.setSpeed(5, 20);  
//  maestro.setAcceleration(0, 5);
//  maestro.setSpeed(6, 20);  
//  maestro.setAcceleration(0, 5);
//  maestro.setTarget(5, 8994);
//  maestro.setTarget(6,3191 );
//  delay(3000);
  
  
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

//zero position 
  maestro.setTarget(0, 6366); 
  maestro.setTarget(1, 5636); 
  maestro.setTarget(2, 5227); 
  maestro.setTarget(3, 6045);
  maestro.setTarget(4, 5753);
  delay(500);


//right forward step 1
  maestro.setTarget(0, 6366); 
  maestro.setTarget(1, 5636); 
  maestro.setTarget(2, 4380); 
  maestro.setTarget(3, 6045);
  maestro.setTarget(4, 6200);
  delay(500);

//right forward step 2
  maestro.setTarget(0, 5461); 
  maestro.setTarget(1, 5636); 
  maestro.setTarget(2, 5227); 
  maestro.setTarget(3, 6045);
  maestro.setTarget(4, 5607);
  delay(500);


//left forward step 1
  maestro.setTarget(0, 7709); 
  maestro.setTarget(1, 5636); 
  maestro.setTarget(2, 5461); 
  maestro.setTarget(3, 6045);
  maestro.setTarget(4, 5400);
  delay(500);


//right forward step 2
  maestro.setTarget(0, 7709); 
  maestro.setTarget(1, 5636); 
  maestro.setTarget(2, 5461); 
  maestro.setTarget(3, 6045);
  maestro.setTarget(4, 5928);
  delay(500);
}
