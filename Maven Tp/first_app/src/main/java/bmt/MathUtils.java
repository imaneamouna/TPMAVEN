 package bmt;

public class MathUtils {
 /**
     * This method adds two integers and returns the result.
     * @param a The first integer to be added
     * @param b The second integer to be added
     * @return The multiple of a and b
     */
    public double square(double x) {
        return x * x;
    }
    public static void main(String[] args) {
        MathUtils mm = new MathUtils();
        System.out.println("Square of 5 is: " + mm.square(5)); // Outputs
    }
}

