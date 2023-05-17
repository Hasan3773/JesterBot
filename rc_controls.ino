const int motors_left_pin_1 = 2; 
const int motors_left_pin_2 = 3;

const int motors_right_pin_1 = 4; 
const int motors_right_pin_2 = 5;

const int dio_buzzer_pin = 7;


void setup() {
  Serial.begin(9600);
  pinMode(motors_left_pin_1, OUTPUT);
  pinMode(motors_left_pin_2, OUTPUT);
  pinMode(motors_right_pin_1, OUTPUT);
  pinMode(motors_right_pin_2, OUTPUT);
}

void loop() {
  digitalWrite(dio_buzzer_pin, HIGH);
 //Check to see if anything is available in the serial receive buffer
 if (Serial.available() > 0)
 {
   char inByte = Serial.read();
   // R
   if (inByte == 'r') {
    Serial.println("r pushed");
    digitalWrite(motors_left_pin_1, HIGH); 
    digitalWrite(motors_right_pin_1, LOW); 
    digitalWrite(motors_left_pin_2, LOW); 
    digitalWrite(motors_right_pin_2, LOW);
   }
   // L
   if (inByte == 'l') {
    Serial.println("l pushed");
    digitalWrite(motors_left_pin_1, LOW); 
    digitalWrite(motors_right_pin_1, HIGH); 
    digitalWrite(motors_left_pin_2, LOW); 
    digitalWrite(motors_right_pin_2, LOW);
   }
   // F
   if (inByte == 'f') {
    Serial.println("f pushed");
    digitalWrite(motors_left_pin_1, HIGH); 
    digitalWrite(motors_right_pin_1, HIGH); 
    digitalWrite(motors_left_pin_2, LOW); 
    digitalWrite(motors_right_pin_2, LOW);
   }
   // S
   if (inByte == 's') {
    Serial.println("s pushed");
    digitalWrite(motors_left_pin_1, LOW); 
    digitalWrite(motors_right_pin_1, LOW); 
    digitalWrite(motors_left_pin_2, LOW); 
    digitalWrite(motors_right_pin_2, LOW);
   }
   if (inByte == 'b') {
     Serial.println("b pushed");
     digitalWrite(motors_left_pin_1, LOW); 
     digitalWrite(motors_right_pin_1, LOW); 
     digitalWrite(motors_left_pin_2, HIGH); 
     digitalWrite(motors_right_pin_2, HIGH);
   }
 }
}