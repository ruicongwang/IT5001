/** A berserker */
public class Berserker extends Fighter {
    // static constants
    public static final int COST = 200;
    private static final String BERSERKER_NAME = "Berserker";
    private static final String BERSERK_STRING = "Berserk mode! Attack double!";
    private static final int BERSERK_MULTIPLIER = 2;
    private static final double BERSERK_THRESHOLD = 0.5;

    // constructor
    Berserker() {
        super(BERSERKER_NAME);
    }
    
    @Override
    public int damage() {
        if (currentHp <= maxHp * BERSERK_THRESHOLD) { // berserk mode
            System.out.println(BERSERK_STRING);
            return BERSERK_MULTIPLIER * strength;
        } else {
            return strength;
        }
    }
}
