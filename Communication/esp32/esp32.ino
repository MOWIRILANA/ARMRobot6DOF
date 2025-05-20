#include <WiFi.h>

const char *ssid = "ARMTECH";
const char *password = "inverse6";

const int ledPin = 2;

WiFiServer server(80);

void setup() {
  Serial.begin(115200);
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());
  server.begin();
}

void loop() {
  WiFiClient client = server.available();

  if (client) {
    Serial.println("Client connected.");

    String request = client.readStringUntil('\r');
    client.flush();

    if (request.indexOf("ON") != -1) {
      digitalWrite(ledPin, HIGH);
      Serial.println("Received signal to turn ON LED.");
    }

    // client.println("HTTP/1.1 200 OK");
    // client.println("Content-Type: text/html");
    // client.println();
    // client.println("OK");

    // delay(1000); 
    // digitalWrite(ledPin, LOW);
    // Serial.println("Turned OFF LED.");

    // client.stop();
    // Serial.println("Client disconnected.");
  }

  // Kode loop jika diperlukan
}
