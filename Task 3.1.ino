// C++ code
// 
#include "Timer.h"
int btn = 0;
unsigned long prev=0;
const long intgreen =120000;
const long intwhite1 =300000;
const long intwhite2 =480000;
Timer t;
void setup()
{
  pinMode(13, OUTPUT);
  t.pulse(pin, 10 * 60 * 1000UL, HIGH); 
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(2, INPUT);
}

void loop()
{ 
  unsigned long crnt =millis();
  btn=digitalRead(2);
  if(btn==HIGH){
      t.update();
    if((crnt-prev)>=intgreen){
      prev =crnt;
      digitalWrite(11,HIGH);
      delay(5000);
    }
      if(crnt==intwhite1||crnt==intwhite2){
       digitalWrite(12,HIGH);
        delay(10000);
      }
    }
  else {
  digitalWrite(13,LOW);
  digitalWrite(12,LOW);
  digitalWrite(11,LOW);
  }
}