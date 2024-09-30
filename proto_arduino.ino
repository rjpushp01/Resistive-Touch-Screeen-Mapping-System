const int switchPin1 = 8; // Pin connected to switch for sin(x)
const int switchPin2 = 9; // Pin connected to switch for cos(x)
const int switchPin3 = 10; // Pin connected to switch for x^2
const int switchPin4 = 11; // Pin connected to switch for circle x^2 + y^2 = 5
const int switchPin5 = 12; // Pin connected to switch for y^2 = 4ax

void setup() {
  Serial.begin(9600);
  pinMode(switchPin1, INPUT);
  pinMode(switchPin2, INPUT);
  pinMode(switchPin3, INPUT);
  pinMode(switchPin4, INPUT);
  pinMode(switchPin5, INPUT);
}

void loop() {
  if (digitalRead(switchPin1) == HIGH) {
    Serial.println("sin(x)");
  } else if (digitalRead(switchPin2) == HIGH) {
    Serial.println("cos(x)");
  } else if (digitalRead(switchPin3) == HIGH) {
    Serial.println("x^2");
  } else if (digitalRead(switchPin4) == HIGH) {
    Serial.println("circle");
  } else if (digitalRead(switchPin5) == HIGH) {
    Serial.println("y^2=4ax");
  }


  delay(1000); // Delay before checking the switch again
}

