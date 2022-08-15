package twelve.functionalprogramming;

import java.util.List;

public class FunctionalProgrammingExamples {
    public static void main(String[] args) {
        List<String> list = List.of("Apple", "Banana", "Cat");
        List<Integer> listNumbs = List.of(1,2,3,4,5, 7, 9);
//        printBasic(list);
        printWFP(list);
        printListFP(listNumbs);
//        printWFilter(list);
        printWFilterFP(list);
        printListFilterFP(listNumbs);
    }

    private static void printBasic(List<String> list) {
        for (String str : list) {
            System.out.println(str);
        }
    }

    private static void printWFP(List<String> list) {
        // stream of values
        list.stream().forEach(element -> System.out.println("element - " + element));
//        list.stream().forEach(System.out::println);
//        list.forEach(System.out::println);
    }

    private static void printListFP(List<Integer> list) {
        list.stream().forEach(number -> System.out.println("Number - " + number));
    }

    private static void printListFilterFP(List<Integer> list) {
        list.stream()
                .filter(element -> element % 2 != 0)
                .forEach(number -> System.out.println("Number - " + number));
    }

    private static void printWFilter(List<String> list) {
        for (String filter : list) {
            if(filter.endsWith("at")) {
                System.out.println(filter);
            }
        }
    }

    private static void printWFilterFP(List<String> list) {
        list.stream()
                .filter(element -> element.endsWith("at"))
                .forEach(element -> System.out.println("element - " + element));
    }
}
