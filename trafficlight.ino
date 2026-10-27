int red = 5;
int yellow = 6;
int green = 7;
void setup(){
  pinMode(red,OUTPUT);
  pinMode(yellow,OUTPUT);
  pinMode(green,OUTPUT);
}
void loop(){
  digitalWrite(red,HIGH);
  delay(3000);
  
  digitalWrite(red,LOW);
  digitalWrite(yellow,HIGH);
  delay(1000);

  digitalWrite(yellow,LOW);
  digitalWrite(green,HIGH);
  delay(3000);

  digitalWrite(green,LOW);
  
  
}
i havent upload anything in github just gimme structure so that i coul paste it
