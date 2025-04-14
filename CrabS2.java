
// CrabS2.java

public class CrabS2 {
    public String name = "Rune Crab";
    public String type = "Tank";
    public int hp = 500;
    public int quantity = 2;

    public int absorb(int damage) {
        return Math.max(0, damage - 50);
    }
}
