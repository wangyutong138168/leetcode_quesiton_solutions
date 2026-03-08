abstract class Asset {
    abstract int price(); 
}

class Gold extends Asset {
    int price() { return 1000; } 
}

public class Main {
    public static void main(String[] args) {
        Asset a = new Gold(); 
        System.out.println(a.price());
    }
}