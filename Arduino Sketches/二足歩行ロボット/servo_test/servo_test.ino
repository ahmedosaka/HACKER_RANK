#include <Wire.h>
#include <PololuMaestro.h>  //ライブラリの読み込み

#ifdef SERIAL_PORT_HARDWARE_OPEN
  #define maestroSerial SERIAL_PORT_HARDWARE_OPEN
#else
  #include <SoftwareSerial.h>
  SoftwareSerial maestroSerial(0, 1);
#endif

MicroMaestro maestro(maestroSerial);

void setup()
{
  maestroSerial.begin(9600);
  
  maestro.setSpeed(0, 20);  //サーボモータの回転速度を決定　左がモータ番号（【channel 0】＝0）　右は動作速度（0だと制限なし）
  maestro.setAcceleration(0, 5);  //サーボモータの回転加速度を決定　左がモータ番号（【channel 0】＝0）　右は動作加速度（0だと制限なし）

  maestro.setTarget(0, 6016);
  
  maestro.setSpeed(1, 20);
  maestro.setAcceleration(1, 5);

  maestro.setTarget(1, 6016);

  
  maestro.setSpeed(2, 20);
  maestro.setAcceleration(2, 5);

  maestro.setTarget(2, 6016);

  
  maestro.setSpeed(3, 20);
  maestro.setAcceleration(3, 5);

  maestro.setTarget(3, 6016);

  maestro.setSpeed(4, 20);
  maestro.setAcceleration(4, 5);

  maestro.setTarget(4, 5402);

    //左がモータ番号（【channel 0】＝0）　右はパルス幅（単位【μs】、入力したいパルス幅×4の値を入れる）
  delay(1000);

  /*
  maestro.setSpeed(0, 0);
  maestro.setAcceleration(0, 0);
  maestro.setSpeed(0, 0);
  maestro.setAcceleration(0, 0);
  */
}

void loop()
{
  //left bending

  
  maestro.setSpeed(0, 20);  //サーボモータの回転速度を決定　左がモータ番号（【channel 0】＝0）　右は動作速度（0だと制限なし）
  maestro.setAcceleration(0, 5);  //サーボモータの回転加速度を決定　左がモータ番号（【channel 0】＝0）　右は動作加速度（0だと制限なし）
  
  maestro.setTarget(0, 4789);
  
  maestro.setSpeed(1, 20);
  maestro.setAcceleration(1, 5);
  
  maestro.setTarget(1, 6629);
  
  maestro.setSpeed(2, 20);
  maestro.setAcceleration(2, 5);

  maestro.setTarget(2, 6016);
  
  maestro.setSpeed(3, 20);
  maestro.setAcceleration(3, 5);

  maestro.setTarget(3, 6016);
  
  maestro.setSpeed(4, 20);
  maestro.setAcceleration(4, 5);

  maestro.setTarget(4, 4935);
  

  delay(1000);
  // right bending
  maestro.setTarget(0, 6016);
  maestro.setTarget(1, 6016);
  maestro.setTarget(2, 7943);
  maestro.setTarget(3, 5198);
  maestro.setTarget(4, 6400);
  delay(1000);
}
