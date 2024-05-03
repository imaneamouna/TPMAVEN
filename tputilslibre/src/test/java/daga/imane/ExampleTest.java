package daga.imane;

import org.junit.Test;
import static org.junit.Assert.*;
import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;

public class ExampleTest {

    @BeforeClass
    public static void setUpBeforeClass() {
        System.out.println("BeforeClass: Executed once before all tests");
    }

    @Before
    public void setUp() {
        System.out.println("Before: Executed before each test");
    }

    @Test
    public void test1() throws InterruptedException {
        System.out.println("Test 1: Testing @Test annotation");
        Thread.sleep(500); // Simulate some work
    }

    @Test(timeout = 1000)
    public void test2() {
        System.out.println("Test 2: Testing @Test(timeout=1000) annotation");
    }

    @After
    public void tearDown() {
        System.out.println("After: Executed after each test");
    }

    @AfterClass
    public static void tearDownAfterClass() {
        System.out.println("AfterClass: Executed once after all tests");
    }

    @Test
    public void testSolveQuadraticEquation() {
        // Test when a = 1, b = -3, c = 2
        double[] roots = MyClass.solveQuadraticEquation(1, -3, 2);
        assertArrayEquals(new double[]{2.0, 1.0}, roots, 0.0001);

        // Test when a = 1, b = -2, c = 1
        roots = MyClass.solveQuadraticEquation(1, -2, 1);
        assertArrayEquals(new double[]{1.0}, roots, 0.0001);

        // Test when a = 1, b = 2, c = 3
        roots = MyClass.solveQuadraticEquation(1, 2, 3);
        assertArrayEquals(new double[0], roots, 0.0001);
    }

    @Test
    public void testAssertMethods() {
        // Test assertEquals
        assertEquals(4.0, MyClass.square(2.0), 0.0001);

        // Test assertTrue
        assertTrue(MyClass.square(3.0) == 9.0);

        // Test assertFalse
        assertFalse(MyClass.square(4.0) == 10.0);

        // Test assertNull
        assertNull(null);

        // Test assertNotNull
        assertNotNull(new MyClass());
    }
}
