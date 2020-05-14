import RoomMath as rm

limit = rm.chooser()

code = '''
int grn = 11;
int red = 8;
int us1[] = {6,5};//[trig, echo]1
int us2[] = {3,2};
int trig = 6;
int echo = 5;
int limit = ''' + str(limit) + ''';
int button = 13;
int calibration1;
int calibration2;
int counter;
double soundSpeed = 0.0343;
long dist;
long pulse;

int Counter(int d1 = getDistance(us1[0], us1[1]), int d2 = getDistance(us2[0], us2[1])){
  delay(1000);
  
  int diff;
  
  if(d1 < (calibration1-10) || d2 < (calibration2-10)){
    delay(100);
    diff = d1 - d2;
    if(diff < 0){
      return -1;
    }
    else if(diff > 0){
      return 1;
    }
    else{
      return 0;
    }
  }return 0;
}

void calibrate(){
  if(buttonPressed(button) == true){
    calibration1 = getDistance(us1[0], us1[1]);
    calibration2 = getDistance(us2[0], us2[1]);
  }
  else{
    return;
  }
}

double getDistance(int trig, int echo){
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);
  pulse = pulseIn(echo, HIGH);
  dist = pulse * soundSpeed/2;
  return dist;
}

void blink(int light)
{
    digitalWrite(light, HIGH);
    delay(150);
    digitalWrite(light,LOW);
    delay(150);
}

bool buttonPressed(int sensor){
  if (digitalRead(sensor) == HIGH){
    return true;
  }
  else if(digitalRead(sensor) == LOW){
    return false;
  }
}
void setup(){
  pinMode(grn, OUTPUT);
  pinMode(red, OUTPUT);
  pinMode(us1[0], OUTPUT);
  pinMode(us1[1], INPUT);
  pinMode(us2[0], OUTPUT);
  pinMode(us2[1], INPUT);
  pinMode(button, INPUT);
  Serial.begin(9600);
}

int tally(){
  counter += Counter();
  digitalWrite(red, LOW);
  digitalWrite(grn, HIGH);
  if(counter > limit){
    digitalWrite(grn, LOW);
    digitalWrite(red, HIGH);
  }
  return counter;
}

void loop(){
  calibrate();
  Serial.println("Counter");
  Serial.println(Counter());
  Serial.println("tally");
  Serial.println(tally());
}
'''
with open("../tally/tally.ino", "w") as file:
    file.write(code)