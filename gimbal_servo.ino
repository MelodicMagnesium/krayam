#include <Servo.h>

Servo myservo_direction;
Servo myservo_pitch;// create servo object to control a servo
// twelve servo objects can be created on most boards

int pos_direction = 0;
int pos_pitch = 0;// variable to store the servo position

void setup() {
  myservo_direction.attach(9);
  myservo_pitch.attach(10);// attaches the servo on pin 9 to the servo object
}

void loop() {
  clock_here(210,45);
}

void clock_here(int direction_to_go, int pitch_to_go){
  if(direction_to_go > 180){
    int direction = 360 - direction_to_go;
	myservo_direction.write(direction);
    //pitch varies from 0-90
    myservo_pitch.write(pitch_to_go);
  }
  if(direction_to_go > 0 && direction_to_go < 180){
    int direction = 180 - direction_to_go;
	myservo_direction.write(direction);
    //turn pitch to opposite side
    //pitch varies from 90-180
    int pitch = 180 - pitch_to_go;
    myservo_pitch.write(pitch);
  }
}
