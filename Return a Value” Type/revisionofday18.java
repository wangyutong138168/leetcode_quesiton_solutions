class Animal { void talk() { System.out.println("..."); } }
class Cat extends Animal { void talk() { System.out.println("Meow"); } }
Animal myPet = new Cat(); 
myPet.talk();      