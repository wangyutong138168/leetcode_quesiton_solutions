for (int i = 0; i < 1; i++) {
    Animal a = new Dog("Rex");
    a.makeSound();
    if (a instanceof Dog d) d.wag();
}