public class GoldAsset {
    private double price;

    public double getPrice() { 
        return price; 
    }

    public void setPrice(double p) { 
        if (p > 0) this.price = p;
    }
}