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
  maestro.setTarget(0, 1591.50*4); 
  maestro.setTarget(1, 1409.00*4); 
  maestro.setTarget(2, 1343.25*4); 
  maestro.setTarget(3, 1511.25*4); 
  maestro.setTarget(4, 1511.25*4); 
  delay(500);


//right forward step 1
  maestro.setTarget(0, 1591.50   *4); 
  maestro.setTarget(1, 1409.00   *4); 
  maestro.setTarget(2, 1343.25   *4); 
  maestro.setTarget(3, 1511.25   *4);
  maestro.setTarget(4, 1450.00   *4);
  delay(500);

//right forward step 2
  maestro.setTarget(0, 1591.50   *4); 
  maestro.setTarget(1, 1723.00   *4); 
  maestro.setTarget(2, 1343.25  *4); 
  maestro.setTarget(3, 1511.25   *4);
  maestro.setTarget(4, 1450.00   *4);
  delay(500);

//right forward step 3
  maestro.setTarget(0, 1657.25   *4); 
  maestro.setTarget(1, 1679.00   *4); 
  maestro.setTarget(2, 1306.75   *4); 
  maestro.setTarget(3, 1511.25   *4);
  maestro.setTarget(4, 1450.00   *4);
  delay(500);

//try changing the servo 4 to 1518.50
//right forward step 4
  maestro.setTarget(0, 1657.25   *4); 
  maestro.setTarget(1, 1679.00   *4); 
  maestro.setTarget(2, 1569.50   *4); 
  maestro.setTarget(3, 1328.75   *4);
  maestro.setTarget(4, 1518.50   *4);
  delay(500);


//zero position 
  maestro.setTarget(0, 1591.50      *4); 
  maestro.setTarget(1, 1409.00      *4); 
  maestro.setTarget(2, 1306.75      *4); 
  maestro.setTarget(3, 1511.25      *4);
  maestro.setTarget(4, 1511.25      *4);
  delay(500);

  
//left forward step 1
  maestro.setTarget(0, 1591.50   *4); 
  maestro.setTarget(1, 1409.00   *4); 
  maestro.setTarget(2, 1306.75   *4); 
  maestro.setTarget(3, 1511.25   *4);
  maestro.setTarget(4, 1642.50   *4);
  delay(500);


//left forward step 2
  maestro.setTarget(0, 1591.50   *4); 
  maestro.setTarget(1, 1409.00   *4); 
  maestro.setTarget(2, 1241.00   *4); 
  maestro.setTarget(3, 1292.25   *4);
  maestro.setTarget(4, 1642.50   *4);
  delay(500);


//left forward step 4
  maestro.setTarget(0, 1416.25   *4); 
  maestro.setTarget(1, 1591.50   *4); 
  maestro.setTarget(2, 1241.00   *4); 
  maestro.setTarget(3, 1292.25   *4);
  maestro.setTarget(4, 1642.50   *4);
  delay(500);

//left forward step 5
  maestro.setTarget(0, 1416.25   *4); 
  maestro.setTarget(1, 1591.50   *4); 
  maestro.setTarget(2, 1241.00   *4); 
  maestro.setTarget(3, 1292.25   *4);
  maestro.setTarget(4, 1642.50   *4);
  delay(500);
}
