ExampleTestpackage com.example;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;

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
    public void testSquare() {
        // Assert.assertEquals
        assertEquals(4.0, mathUtils.square(2.0), 0.0001);

        // Assert.assertTrue
        assertTrue(mathUtils.square(3.0) == 9.0);

        // Assert.assertFalse
        assertFalse(mathUtils.square(4.0) == 10.0);

        // Assert.assertNull
        assertNull(null);

        // Assert.assertNotNull
        assertNotNull(mathUtils);
    }
} 