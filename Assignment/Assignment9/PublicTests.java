import it5001.collections.immutable.ImmutableList;

import java.util.Arrays;
import java.util.function.Supplier;

public class PublicTests {
    public static void main(String[] args) {
        int attainedScore = 0, maxScore = 0;
        ComputedTestSet[] results = new ComputedTestSet[] {
            test(PublicTests::public_test1),
            test(PublicTests::public_test2),
            test(PublicTests::public_test3),
            test(PublicTests::public_test4),
            test(PublicTests::public_test5),
            test(PublicTests::public_test6)
        };

        // compute the results
        for (var i : results) {
            System.out.println(i);
            System.out.println();
            attainedScore += i.attainedScore;
            maxScore += i.maxScore;
        }
        System.out.printf("Total attained score: %d/%d\nTEST COMPLETE\n", attainedScore, maxScore);
    }


    private static UncomputedTestSet public_test1() {
        BinarySearchTree<String> bst = new BinarySearchTree<>("M");
        bst.addAll(Arrays.asList("DKFEAL".split("")));
        return new UncomputedTestSet(
            "Public Test 1",
            "A BST containing \"A\" should say so",
            "BinarySearchTree<String> bst = new BinarySearchTree<>(\"M\");\n" + 
                "bst.addAll(Arrays.asList(\"DKFEAL\".split(\"\")));\n" + 
                "bst.contains(\"A\")", 
            true,
            () -> bst.contains("A"),
            15);
    }

    private static UncomputedTestSet public_test2() {
        BinarySearchTree<Integer> bst = new BinarySearchTree<>(6);
        bst.addAll(Arrays.asList(new Integer[]{1, 7, 8, 3, 4, 10}));
        return new UncomputedTestSet(
            "Public Test 2",
            "A BST that doesn't contain 2 should say so",
            "BinarySearchTree<Integer> bst = new BinarySearchTree<>(6);\n" + 
                "bst.addAll(Arrays.asList(new Integer[]{1, 7, 8, 3, 4, 10}));\n" + 
                "bst.contains(2)", 
            false,
            () -> bst.contains(2),
            15);
    }

    private static UncomputedTestSet public_test3() {
        BinarySearchTree<Integer> bst = new BinarySearchTree<>(6);
        bst.addAll(Arrays.asList(new Integer[]{3, 1, 7, 8, 4, 10}));
        return new UncomputedTestSet(
            "Public Test 3",
            "inorder should work for a BST with unique elements",
            "BinarySearchTree<Integer> bst = new BinarySearchTree<>(6);\n" + 
                "bst.addAll(Arrays.asList(new Integer[]{3, 1, 7, 8, 4, 10}));\n" + 
                "bst.inorder()", 
            ImmutableList.of(1, 3, 4, 6, 7, 8, 10),
            () -> bst.inorder(),
            20);
    }

    private static UncomputedTestSet public_test4() {
        BinarySearchTree<Integer> bst = new BinarySearchTree<>(6);
        bst.addAll(Arrays.asList(new Integer[]{3, 1, 7, 6, 8, 3, 4, 10}));
        return new UncomputedTestSet(
            "Public Test 4",
            "inorder should work for a BST with duplicate elements",
            "BinarySearchTree<Integer> bst = new BinarySearchTree<>(6);\n" + 
                "bst.addAll(Arrays.asList(new Integer[]{3, 1, 7, 6, 8, 3, 4, 10}));\n" + 
                "bst.inorder()", 
            ImmutableList.of(1, 3, 3, 4, 6, 6, 7, 8, 10),
            () -> bst.inorder(),
            20);
    }

    private static UncomputedTestSet public_test5() {
        return new UncomputedTestSet(
            "Public Test 5",
            "sort should work for a sequence with unique elements",
            "BinarySearchTree.sorted(Arrays.asList(new Integer[]{3, 6, 4, 1, 5, 2}))", 
            ImmutableList.of(1, 2, 3, 4, 5, 6),
            () -> BinarySearchTree.sorted(Arrays.asList(new Integer[]{ 3, 6, 4, 1, 5, 2})),
            15);
    }

    private static UncomputedTestSet public_test6() {
        return new UncomputedTestSet(
            "Public Test 6",
            "sort should work for a sequence with duplicate elements",
            "BinarySearchTree.sorted(Arrays.asList(new Integer[]{6, 3, 6, 2, 4, 1, 5, 2}))", 
            ImmutableList.of(1, 2, 2, 3, 4, 5, 6, 6),
            () -> BinarySearchTree.sorted(Arrays.asList(new Integer[]{ 6, 3, 6, 2, 4, 1, 5, 2})),
            15);
    }

    private static ComputedTestSet test(Supplier<UncomputedTestSet> f) {
        UncomputedTestSet u = f.get();
        try {
            Object output = u.compute();
            return new ComputedTestSet(u.name, u.description, u.expression, u.expected, output, u.score);
        } catch (Exception e) {
            return new ComputedTestSet(u.name, u.description, u.expression, u.expected, e.getMessage(), u.score);
        }
    }

    private static class UncomputedTestSet {
        String name;
        String description;
        String expression;
        Object expected;
        int score;
        Supplier<?> output;
        UncomputedTestSet(String name, String description, String expression, Object expected, Supplier<?> outputSupplier, int score) {
            this.name = name;
            this.description = description;
            this.expression = expression;
            this.expected = expected;
            this.output = outputSupplier;
            this.score = score;
        }
        Object compute() { return output.get(); }
    }
    private static class ComputedTestSet {
        String name;
        String description;
        String expression;
        Object expected;
        Object output;
        int maxScore;
        int attainedScore;
        ComputedTestSet(String name, String description, String expression, Object expected, Object output, int maxScore) {
            this.name = name;
            this.description = description;
            this.expression = expression;
            this.expected = expected;
            this.output = output;
            this.maxScore = maxScore;
            if (expected.equals(output))
                this.attainedScore = maxScore;
            else
                this.attainedScore = 0;
        }
        @Override
        public String toString() {
            return String.format("===== %s =====\n%s\n\nTest:\n%s\n\nExpected: %s\nOutput:   %s\nAttained score: %d/%d\n===================", name, description, expression, expected, output, attainedScore, maxScore);
        }
    }
}
