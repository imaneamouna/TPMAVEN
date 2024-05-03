package bmt;

import static org.junit.Assert.*;
import org.junit.Test;

public class CalculationTest {

    @Test
    public void testAdd() {
        assertEquals(5, Calculation.add(2, 3));
    }

    @Test
    public void testSubtract() {
        assertEquals(1, Calculation.subtract(3, 2));
    }

    @Test
    public void testMultiply() {
        assertEquals(6, Calculation.multiply(2, 3));
    }

    @Test
    public void testDivide() {
        assertEquals(2.0, Calculation.divide(6, 3), 0.0001);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testDivideByZero() {
        Calculation.divide(6, 0);
    }
}
