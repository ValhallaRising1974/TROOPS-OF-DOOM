
// TroopSimulation.java

public class TroopSimulation {
    public static void main(String[] args) {
        System.out.println("=== Standard Troops ===");

        GhostS4 ghost = new GhostS4();
        System.out.println(ghost.quantity + "x " + ghost.name + " attack: " + ghost.attack() + " (" + ghost.specialTrait() + ")");

        SqueletonS4 skeleton = new SqueletonS4();
        System.out.println(skeleton.quantity + "x " + skeleton.name + " attack: " + skeleton.attack());

        System.out.println("\n=== Support Troops ===");

        CrabS2 crab = new CrabS2();
        System.out.println(crab.quantity + "x " + crab.name + " absorb damage (100): " + crab.absorb(100));

        SnailS2 snail = new SnailS2();
        System.out.println(snail.quantity + "x " + snail.name + " healing ability: " + snail.heal());

        System.out.println("\n=== Superminions (Endgame) ===");

        AracnoSS aracno = new AracnoSS();
        System.out.println(aracno.name + " special move: " + aracno.charge());

        ZoombieSS zoombie = new ZoombieSS();
        System.out.println(zoombie.name + " ultimate slam: " + zoombie.smash());
    }
}
