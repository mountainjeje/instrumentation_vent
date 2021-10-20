/*int entree1 = A0;
int tension1 = 0;
int entree2 = A1;
int tension2 = 0;
int chaine[7];*/
int tension[7];
int entree[7] = {0, A0, A1, A2, A3, A4, A5};
int compte = 0;
int i=0;


void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  
}

void loop() {
  /*tension1 = analogRead(entree1);
  Serial.print(tension1);
  delay(20);
  tension2 = analogRead(entree2);
  Serial.print(tension2);*/

  tension[0] = compte;
  
  for (i = 1; i <= 6; i++) {
    tension[i] = analogRead(entree[i]);
  }
  
  for (i=0; i<=6; i++) {
    Serial.print(tension[i]);
    Serial.print(", ");
  }
  Serial.println();
  
  compte++;
  digitalWrite(13, HIGH);
  delay(1000);
  digitalWrite(13, LOW);
  delay(29000);
}
