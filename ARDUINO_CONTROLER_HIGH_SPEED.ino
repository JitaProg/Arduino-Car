// Definition of Arduino pins
#define IN1 5
#define IN2 8
#define IN3 6
#define IN4 7
#define ENA 9
#define ENB 10

unsigned long startTime = 0; 
bool isMoving = false; 
char currentCommand = 's'; 

void setup() {
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);
  Serial.begin(9600); 

  // Set all motors to high speed
  velocidadAlta();
}

// Define command and the letter
void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    currentCommand = command; 
    startTime = millis(); 
    isMoving = true; 

    if (command == 'f') { 
      avanzar();
    } else if (command == 'b') { 
      retroceder();
    } else if (command == 'l') { 
      izquierda();
    } else if (command == 'r') { 
      derecha();
    } else if (command == 's') { 
      detener();
      isMoving = false; 
      currentCommand = 's'; 
    }
  }

  // Time for L and R movements
  if (isMoving && (currentCommand == 'l' || currentCommand == 'r') && millis() - startTime >= 1500) {
    detener();
    isMoving = false; 
    currentCommand = 's'; 
  }

  // Continue the current movement for forward and backward while the 's' command is not sent
  if (currentCommand == 'f') {
    avanzar();
  } else if (currentCommand == 'b') {
    retroceder();
  }
}

// Functions to control the motors
void velocidadAlta() {
  analogWrite(ENA, 255); // Set ENA to maximum
  analogWrite(ENB, 255); // Set ENB to maximum
}

void avanzar() {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}

void retroceder() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
}

void izquierda() {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
}

void derecha() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}

void detener() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
}
