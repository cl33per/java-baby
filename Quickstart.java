// class QuickStart {
//   public static void main(String[] args) {
//     int myInt = 9;
//     double myDouble = myInt; // Automatic casting: int to double

//     System.out.println(myInt);      // Outputs 9
//     System.out.println(myDouble);   // Outputs 9.0
//   }
// }

class Lamp {
  boolean isOn;

  void turnOn() {
    isOn = true;
  }

  void turnOff() {
   isOn = false;
  }
  void displayLightStatus(){
      System.out.println("Light on? " + isOn);
  }
}

class QuickStart {
public static void main(String[] args) {
   Lamp l1 = new Lamp(); // create l1 object of Lamp class
   Lamp l2 = new Lamp(); // create l2 object of Lamp class
   l1.turnOn();
   l2.turnOff();

   l1.displayLightStatus();
   l2.displayLightStatus();
  }
}