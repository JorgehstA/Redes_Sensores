// Import required libraries
#include "WiFi.h"
#include "ESPAsyncWebServer.h"
#include "SPIFFS.h"
#include "ESP32Time.h"

//ESP32Time rtc;
ESP32Time rtc(0);

// Replace with your network credentials
const char* ssid = "ONOA3690";
const char* password = "fXH6Zvm7ppNV";

// Stores LED state
String timeState;

const char* ntpServer = "pool.ntp.org";
const long  gmtOffset_sec = 3600;
const int   daylightOffset_sec = 3600;

String current_hour = "";
String current_min = "";
String current_sec = "";
boolean a = true;

// Create AsyncWebServer object on port 80
AsyncWebServer server(80);


String resetTime(const String& var)
{
  if(var == "TIME"){
    struct tm timeinfo;
    if(!getLocalTime(&timeinfo)){
      Serial.println("Failed to obtain time");
    }
    rtc.setTime(-1,00,-1,10,9,2022);
    current_hour = timeinfo.tm_hour;
    current_min = timeinfo.tm_min;
    current_sec = timeinfo.tm_sec;
    timeState = current_hour + ':' + current_min + ':' + current_sec;
    //ledState = current_hour;
    Serial.println(timeState);
    return timeState;
  }
  return String();
}

String printLocalTime(const String& var)
{
  if(var == "TIME"){
    struct tm timeinfo;
    if(!getLocalTime(&timeinfo)){
      Serial.println("Failed to obtain time");
    }
    current_hour = timeinfo.tm_hour;
    current_min = timeinfo.tm_min;
    current_sec = timeinfo.tm_sec;
    timeState = current_hour + ':' + current_min + ':' + current_sec;
    //ledState = current_hour;
    Serial.println(timeState);
    return timeState;
  }
  return String();
}
 
void setup(){
  // Serial port for debugging purposes
  Serial.begin(115200);

  // Initialize SPIFFS
  if(!SPIFFS.begin(true)){
    Serial.println("An Error has occurred while mounting SPIFFS");
    return;
  }

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }

  // Print ESP32 Local IP Address
  Serial.println(WiFi.localIP());

  // Route for root / web page
  server.on("/", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send(SPIFFS, "/index.html", String(), false, printLocalTime);
  });

    server.on("/", HTTP_GET, [](AsyncWebServerRequest *request){
      while(a == true){
        request->send(SPIFFS, "/index.html", String(), false, printLocalTime);
      }
    });
  
  // Route to load style.css file
  server.on("/style.css", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send(SPIFFS, "/style.css", "text/css");
  });
  configTime(gmtOffset_sec, daylightOffset_sec, ntpServer);
  

  // Route to set GPIO to HIGH
  server.on("/reset", HTTP_GET, [](AsyncWebServerRequest *request){   
    request->send(SPIFFS, "/index.html", String(), false, resetTime);
  });

  // Route to set GPIO to HIGH
  server.on("/clock", HTTP_GET, [](AsyncWebServerRequest *request){   
    request->send(SPIFFS, "/index.html", String(), false, printLocalTime);
  });
  

  // Start server
  server.begin();
}
 
void loop(){
}
