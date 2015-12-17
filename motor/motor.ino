/* 
This is a test sketch for the Adafruit assembled Motor Shield for Arduino v2
It won't work with v1.x motor shields! Only for the v2's with built in PWM
control

For use with the Adafruit Motor Shield v2 
---->	http://www.adafruit.com/products/1438

cd Desktop/Wear_Smart
python MainScreen.py

*/


#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_PWMServoDriver.h"
#include <Servo.h>
// Create the motor shield object with the default I2C address
Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 
// Or, create it with a different I2C address (say for stacking)
// Adafruit_MotorShield AFMS = Adafruit_MotorShield(0x61); 

// Connect a stepper motor with 200 steps per revolution (1.8 degree)
// to motor port #2 (M3 and M4)
Adafruit_StepperMotor *myMotor = AFMS.getStepper(200, 2);


char user_input;
char user_input1;
bool lastdir;
int pos=0;
const int IR0 = A3;
const int IR1 = A2;
const int IR2 = A1;
const int IR3 = A0;

//check and save current position
int count=0; 
int sensorValue = 0;
int outputValue = 0;
int previousValue0=0; 
int previousValue1=0; //set initial value of default ir sensor as 90 to prevent 
                       //ir sensor to check the item is taken off  even though it is not
int irsensor_releasetime=0;
bool Itemonhanger=true;
long previousMillis=0;

void setup() {
  Serial.begin(9600);           // set up Serial library at 9600 bps
  AFMS.begin();  // create with the default frequency 1.6KHz
  //AFMS.begin(1000);  // OR with a different frequency, say 1KHz
  myMotor->setSpeed(20);  // 30 rpm

  
  //Print function list for user selection
    //Serial.println("Enter number for control option:");
//  Serial.println("0. GO back to default position");
//  Serial.println("1. Go to 1state// check ir sensor// going back");
//  Serial.println("2. Go to 2state// check ir sensor// going back");
//  Serial.println("3. Go to 3state// check ir sensor// going back");
//  Serial.println("4. Go to position with turning disk 288 degrees turn.");
//  Serial.println();
//  Serial.println("5. Go  to 1 state without coming back");
//  Serial.println("6. Go  to 2 state without coming back");
//  Serial.println("7. Go  to 3 state without coming back");
//  Serial.println("8. Go  to 4 state without coming back");
//  Serial.println();   
}

void loop() {
  while(Serial.available()){
      user_input = Serial.read(); //Read user input and trigger appropriate function
      
      if (user_input =='0')
      {
         //Serial.println("Go to default position according to the current sate ");
         
         if (lastdir)//Forward true
         {
            //Serial.println("Going Backward");
            StepBackward_state(count);         
         }
         else
         {
            StepForward_state(count);
            //Serial.println("Going Forward");
         }
         count=0; //reset count after going backto default position
         delay(2000);
      }
      
      else if (user_input =='1')
      {
         //Serial.println("Moving forward one state => 72 degrees for the disk, 140 steps for the motor.");
         StepForward_state(1);
         count+=1; //use count to check current state
         Itemonhanger=true;
         //function to check the change in the distance sensor(compare absolute sensorvalue and difference of the sensor value)
         //Serial.println("press x to exit from IR sensor manually");
         while (Itemonhanger)
         {
            Check_irsensor(IR0);
         }
          // maybe we should use release() function 
         delay(2000); // wait after user take off their item
         StepBackward_state(1);
         count=0;
         delay(2000);//wait before the stepper motor release
         Serial.println("check temp");
         
         
      }
      else if(user_input =='2')
      {
        //Serial.println("Moving forward two states => 144 degrees for the disk, 280degrees for the motor.");
        StepForward_state(2);
        count+=2;
        Itemonhanger=true;
         //function to check the change in the distance sensor(compare absolute sensorvalue and difference of the sensor value)
        
        while (Itemonhanger)
        {
           Check_irsensor(IR1);
        }
          
        delay(2000); // wait after user take off their item
        StepBackward_state(2);
        count=0;
        delay(2000);
        Serial.println("check temp");
                   
      }
      else if(user_input =='3')
      {
        //Serial.println("Moving forward three states- => 216 degrees for the disk, 420degrees for the motor.");
        StepBackward_state(2);
        count+=3;
        Itemonhanger=true;
         //function to check the change in the distance sensor(compare absolute sensorvalue and difference of the sensor value)
        
        while (Itemonhanger)
        {
           Check_irsensor(IR2);
        }
          
        delay(2000); // wait after user take off their item
        StepForward_state(2);
        count=0;
        delay(2000); //wait 1second before release the stepper motor
        //Serial.println("c"); 
      }
      else if(user_input =='4')
      {
        //Serial.println("Moving forward four states- => 288 degrees for the disk, 560degrees for the motor.");
        StepBackward_state(1);
        count+=4;
        Itemonhanger=true;
         //function to check the change in the distance sensor(compare absolute sensorvalue and difference of the sensor value)
        
        while (Itemonhanger)
        {
           Check_irsensor(IR3);
        }
          
        delay(2000); // wait after user take off their item
        StepForward_state(1);
        count=0;
        delay(2000);
        //Serial.println("d");
      }
      else if(user_input =='5')
      {
        //Serial.println("Only Moving to 1 state not coming back");
        StepForward_state(1);
        count+=1;  //state is 1
        lastdir=true; //last direction is true(Forwarrd)
        delay(2000); // wait after user take off their item               
      }
      else if(user_input =='6')
      {
        //Serial.println("Only Moving to 2 state not coming back");
        StepForward_state(2);
        count+=2;  //state is 2
        lastdir=true; //last direction is true(Forwarrd)
        delay(2000); // wait after user take off their item               
      }
      else if(user_input =='7')
      {
       // Serial.println("Only Moving forward 3 state not coming back");
        StepBackward_state(2);
        count+=2;  //turn 2
        lastdir=false; //last direction is false(Backward)
        delay(2000); // wait after user take off their item               
      }
      else if(user_input =='8')
      {
        //Serial.println("Only Moving forward 4 state not coming back");
        StepBackward_state(1);
        count+=1;  //turn1
        lastdir=false; //last direction is false(backward)
        delay(2000); // wait after user take off their item               
      }
      else
      {
       // Serial.println("Invalid option entered.");
        
      }
  }
  myMotor->release();//release coil to prevent motor overheating
  previousValue0=0;
  previousValue1=0; 
  irsensor_releasetime=0;// reset the values
  //however it makes motor to spin freely if someone touches it(Okay?)
  //Serial.println("Release coils");  
}

void Check_irsensor(const int state)
{
  user_input1 = Serial.read(); //Read user input and trigger appropriate function
  unsigned long currentMillis=millis();
  if (user_input1 =='x') //press x to stop IR sensor checking
    {
       Itemonhanger=false;
    }
    
  if (currentMillis-previousMillis>300)
  {
    previousMillis=currentMillis;
    Itemonhanger=true;
    sensorValue= analogRead(state);
    outputValue=map(sensorValue, 0, 1023,0,255);
    
   // Serial.print("output = ");
   // Serial.print(outputValue);
    //Serial.print("\t difference= ");
   // Serial.println(previousValue0-outputValue);
    if ((previousValue0 !=0) && (abs(previousValue0-outputValue)>40))// if the item is taken off, turn it back
    {
      Itemonhanger=false;
    }
  
    if (irsensor_releasetime > 120)// if irsensor time lasts longer that 1minute release motor to prevent overheating
    {
      Itemonhanger=false; //if the item is not taken off after the interval, turn it back
    }
    
    irsensor_releasetime+=1;
    previousValue0=previousValue1; 
    previousValue1=outputValue;
  }
  
  
}

void StepForward_state(int state_num)
{
  
  myMotor->step(140*state_num, FORWARD, DOUBLE); 
}


void StepBackward_state(int state_num)
{
  
  myMotor->step(140*state_num, BACKWARD, DOUBLE); 
}



