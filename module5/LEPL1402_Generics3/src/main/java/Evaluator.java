import java.util.HashMap;
import java.util.function.BiFunction;
import java.util.function.Function;

public class Evaluator {

    public BiFunction<Boolean, Boolean, Boolean> xor_gate() {
        // TODO BY STUDENT
        return (a,b) -> a^b;
    }

    public BiFunction<Boolean, Boolean, Boolean> or_gate() {
        // TODO BY STUDENT
        return (a,b) -> a || b;
    }

    public BiFunction<Boolean, Boolean, Boolean> and_gate() {
        // TODO BY STUDENT
        return (a,b) -> a && b;
    }

    public Function<Boolean, Boolean> not_gate() {
        // TODO BY STUDENT
        return (a) -> !a;
    }

    // Should return a map containing the computation's results (use HashMap)
    // You're asked to store the results under the following keys: "SUM" & "carry_out"
    // TODO WARNING : ONLY USE the previously defined methods to compute the result
    // (INGInious will prevent you from cheating by directly invoking logical operators)
    public HashMap<String, Boolean> evaluate_circuit(Boolean a, Boolean b, Boolean carry_in) {
        // TODO BY STUDENT
        HashMap<String, Boolean> result = new HashMap<>();
        boolean resultXOR = xor_gate().apply(a, b);
        result.put("SUM", xor_gate().apply(resultXOR, carry_in));
        result.put("carry_out", or_gate().apply(and_gate().apply(resultXOR, carry_in), and_gate().apply(a, b)));
        return result;
    }
}