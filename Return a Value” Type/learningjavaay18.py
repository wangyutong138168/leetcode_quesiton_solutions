class Animal { void speak() { System.out.println("..."); } }
class Dog extends Animal { void speak() { System.out.println("Bark"); } }
Animal myDog = new Dog(); 
myDog.speak();            