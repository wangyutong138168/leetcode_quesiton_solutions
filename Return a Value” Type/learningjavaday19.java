interface Skill{void doWork(); }
abstract class Parent {abstract void info();}

class Child extends Parent implements Skill{
    public void dowork() {} void info() {}
}