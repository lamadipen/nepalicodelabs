package demo;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class DemoTddTest {

    private DemoTdd demoTdd = new DemoTdd();

    @Test
    void isFirstParamGreaterThanSecondParamSuccessTest() {
        boolean firstParamGreaterThanSecondParam = demoTdd.isFirstParamGreaterThanSecondParam(5, 1);

        Assertions.assertTrue(firstParamGreaterThanSecondParam);
    }

    @Test
    void isFirstParamGreaterThanSecondParamFailTest() {
        boolean firstParamGreaterThanSecondParam = demoTdd.isFirstParamGreaterThanSecondParam(1,5);

        Assertions.assertFalse(firstParamGreaterThanSecondParam);
    }
}