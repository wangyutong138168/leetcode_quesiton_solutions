abstract class Asset {
    abstract void info(); 
    void status() { System.out.println("Active"); } 
}

class Gold extends Asset {
    @Override
    void info() { System.out.println("Gold: 99% Pure"); } 
}