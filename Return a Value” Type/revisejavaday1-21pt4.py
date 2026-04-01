class A { String x = "A"; void show(){ System.out.println("A"); } }
class B extends A { String x = "B"; void show(){ System.out.println("B"); } }
A obj = new B();
System.out.println(obj.x); obj.show();