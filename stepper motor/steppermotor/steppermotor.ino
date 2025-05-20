#include <Stepper.h>

// Konfigurasi pin
const int stepPin = 33;
const int dirPin = 32;

// Konfigurasi motor stepper (misalnya, 200 steps per putaran)
const int stepsPerRevolution = 650;
Stepper myStepper(stepsPerRevolution, stepPin, dirPin);

void setup() {
  // Nothing here
}

void loop() {
  // Mengatur kecepatan motor (ditentukan dalam mikrodetik)
  myStepper.setSpeed(300); // Sesuaikan kecepatan sesuai kebutuhan
  
  // Menggerakkan motor searah jarum jam
  myStepper.step(stepsPerRevolution);
  delay(1000); // Memberi jeda 1 detik
  
  // Menggerakkan motor berlawanan arah jarum jam
  myStepper.step(-stepsPerRevolution);
  delay(1000); // Memberi jeda 1 detik
}