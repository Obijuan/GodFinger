//--------------------------------------------------------------
//-- FingerServer: Controlling the servos from the PC
//--------------------------------------------------------------
//-- (c) Juan Gonzalez-Gomez (Obijuan), May-2013
//-- GPL license
//--------------------------------------------------------------
#include <Servo.h> 

//-- Only needed for the skymega board
//-- If using arduino, it can be commented
#include <skymega.h>

//----------------------------------------------------------------
//-- The communication with the PC is by the serial port (115200 bauds)
//-- The FRAMES contains only ascii characters. The format is the 
//-- following:
//--
//--   :sPa  , where 
//--
//--  : is the frame header
//--  s is the servo number (1 - 8)
//--  P is the position command
//--  a is the angle (between -90 and 90)
//--
//-- The frame should finish one of the following characters:
//--   space, cr or lf
//--
//--  Example:    :1P40   --> Move the servo 1 to 40 degrees
//--              :2P-30  --> Move the servo 2 to -40 degrees
//-----------------------------------------------------------------

//-- Definitions for the frames
#define FRAME_HEADER ':'
#define FRAME_POS    'P'     //-- Position command


//---------- Global variables
Servo s[8];     //-- Servos
char s_index=0; //-- Servo index
int ang = 0;    //-- Servo angle

//-- For reading the serial input
char serial_char;

//-- Buffer for storing the received commands
#define BUFSIZE 8
char buffer[BUFSIZE+1];
int buflen = 0;

bool cmd_ready=false; 

void setup() 
{ 
  // Configure the skymega led
  pinMode(LED, OUTPUT);
  
  //-- Configure the serial port
  Serial.begin(115200);
  
  //-- Configure the servos
  //-- For arduino just write the pin number instead of the
  //-- labels SERVOx
  s[0].attach(SERVO1);
  s[1].attach(SERVO2);
  s[2].attach(SERVO3);
  s[3].attach(SERVO4);
  
  //-- Initial servo pos
  for (int i=0; i<4; i++)
    s[i].write(0 + 90);
  
  //-- Turn on the led
  digitalWrite(LED, OFF);
  
  Serial.print("Ready!\n");
} 
 


void read_frame()
{
  if (Serial.available() && buflen < BUFSIZE) {
    
    //-- Read the car
    serial_char = Serial.read();
    
    //-- Detect blank caracters. They are interpreted as the end of a command    
    if (serial_char == ' ' || serial_char == '\r' || serial_char == '\n') {
      //Serial.print("Blank\n");
      
      //-- Store the end of string
      buffer[buflen]=0;
      
      //-- Now there is a command ready to be processed!
      if (buflen>0)
        cmd_ready = true;
    }
      
    //-- Normal character: store it in the buffer  
    else {
      buffer[buflen]=serial_char;
      buflen++;
      //Serial.print("OK\n");
    }
  }
}

void process_cmd()
{
  //-- Parse the command
  //-- First check if the header is ok
  if (buffer[0] != FRAME_HEADER)
    return;  //-- of the Jedi
  
  //-- Read the servo number
  s_index = buffer[1] - '0' -1;
  if (s_index < 0  ||  s_index > 8)
    return;  //-- of the Jedi
  
  //-- Pos command
  if (buffer[2] != FRAME_POS)
    return;  //-- of the Jedi
  
  //-- Get the angular value
  ang = strtol(&buffer[3],NULL,10);
   
  //-- Pos the servo 
  s[s_index].write(ang + 90);

  
  /*if (s_index == 2) 
    digitalWrite(LED, ON);
  else
    digitalWrite(LED, OFF);
    */
  
  //-- Debug...
  Serial.print("CMD: ");
  Serial.print(buffer);
  Serial.print("---\n");
}



void loop() 
{ 
  
  //-- Task: Read the information from the serial port
  read_frame();
  
  //-- If there is a command ready or the buffer is full
  //-- process the command!!
  if (cmd_ready || buflen==BUFSIZE) {
    
    //-- Process the command
    process_cmd();
    
    //-- Command processed!
    cmd_ready=false;
    buflen=0;
  }
  
} 



