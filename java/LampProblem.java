
class Lamp {
    boolean isOn;

    void turnOn() {
        isOn = true;
    }

    void turnOff() {
        isOn = false;
    }

    void displayLightStatus() {
        System.out.println("Light on? " + isOn);
    }
}

class LampProblem {
    public static void main(String[] args) {
        Lamp l1 = new Lamp(); // create l1 object of Lamp class
        Lamp l2 = new Lamp(); // create l2 object of Lamp class
        l1.turnOn();
        l2.turnOff();

        l1.displayLightStatus();
        l2.displayLightStatus();
    }
}