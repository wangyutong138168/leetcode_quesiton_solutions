class Asset {
    void info() { System.out.println("General Asset"); }
}

class Gold extends Asset {
    @Override
    void info() { System.out.println("Gold Bar: 99.9% Pure"); }
}

public class Main {
    public static void main(String[] args) {
       
        Asset myAsset = new Gold(); 
        
        myAsset.info();
    }
}