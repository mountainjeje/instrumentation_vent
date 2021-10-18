int i=0;


void setup() {
  Serial.begin(9600);
  Serial.println("Un message va etre envoye toutes les deux secondes des maintenant !");
  pinMode(13, OUTPUT);
}

void loop() {
  Serial.println("Message #" + String(i));
  digitalWrite(13, HIGH);
  delay(500);
  digitalWrite(13, LOW);
  delay(2000);
  i++;
}
