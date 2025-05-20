#include <WiFi.h>

const char *ssid = "ARMTECH";
const char *password = "inverse6";
const char *serverIP = "192.168.43.232";
const int serverPort = 80;

const int buttonPin = 0;

void setup() {
  Serial.begin(115200);
  pinMode(buttonPin, INPUT_PULLUP);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
}

void loop() {
  int buttonState = digitalRead(buttonPin);

  if (buttonState == LOW) {
    sendSignal();
    delay(1000); 
  }

  delay(10);
}

void sendSignal() {
  WiFiClient client;

  if (client.connect(serverIP, serverPort)) {
    Serial.println("Sending signal to ESP32...");
    client.print("ON");
    // client.stop();
  } else {
    Serial.println("Connection failed.");
  }
}
