package nine.inheritance;

public class ProjectInterface {

    interface Test {
        void method1();
        // if I add a second method, I will need to implement the method2() in both classes
        // how do I fix this compilation error.
        // void method2();

        // can have a default interface
        // useful: when I provide interface and another third party is providing the implementation details
        default void method2(){}
    }

    class Class1 implements Test {

        @Override
        public void method1() {

        }
    }

    class Class2 implements Test {

        @Override
        public void method1() {

        }
    }
}
