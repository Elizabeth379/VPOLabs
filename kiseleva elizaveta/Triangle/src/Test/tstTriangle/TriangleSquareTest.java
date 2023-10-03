package Test.tstTriangle;

import org.junit.Test;
import triangle.Triangle;

import static org.junit.Assert.assertEquals;

public class TriangleSquareTest {

    @Test
    public void testGetSquare() {
        Triangle triangle = new Triangle(3, 4, 5);

        double expectedSquare = 6.0;

        double actualSquare = triangle.getSquare();

        assertEquals(expectedSquare, actualSquare, 0.0001);
    }

    @Test
    public void testGetSquareWithZeros() {
        Triangle triangle = new Triangle(0, 0, 0);

        double expectedSquare = 0.0;

        double actualSquare = triangle.getSquare();

        assertEquals(expectedSquare, actualSquare, 0.0001);
    }

    @Test
    public void testGetSquareWithNegativeValues() {
        Triangle triangle = new Triangle(-3, 4, 5);

        double expectedSquare = 0.0; // Треугольник с отрицательным значением стороны не существует

        double actualSquare = triangle.getSquare();

        assertEquals(expectedSquare, actualSquare, 0.0001);
    }

    @Test
    public void testGetSquareWithInvalidTriangle() {
        Triangle triangle = new Triangle(1, 1, 3); // Треугольник с этими сторонами не существует

        double expectedSquare = 0.0;

        double actualSquare = triangle.getSquare();

        assertEquals(expectedSquare, actualSquare, 0.0001);
    }

    @Test
    public void testGetSquareWithLargeValues() {
        Triangle triangle = new Triangle(1000, 2000, 2500);

        double expectedSquare = 0.0; // Треугольник слишком большой, его площадь должна быть равна 0

        double actualSquare = triangle.getSquare();

        assertEquals(expectedSquare, actualSquare, 0.0001);
    }


}
