// MyClass.java
package daga.imane;

public class MyClass {
    public static double[] solveQuadraticEquation(double a, double b, double c) {
        double discriminant = b * b - 4 * a * c;
        if (discriminant < 0) {
            return new double[0]; // No real roots
        } else if (discriminant == 0) {
            return new double[] { -b / (2 * a) }; // One real root
        } else {
            double sqrtDiscriminant = Math.sqrt(discriminant);
            return new double[] { (-b + sqrtDiscriminant) / (2 * a), (-b - sqrtDiscriminant) / (2 * a) }; // Two real roots
        }
    }
    public static double square(double x) {
        return x * x;
    }
}
