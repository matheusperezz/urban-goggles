import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Problems {
  public void problem_56() {
    Scanner reader = new Scanner(System.in);
    int size, target;
    int total = 0;
    size = reader.nextInt();
    target = reader.nextInt();
    List<Integer> nums = new ArrayList<>();

    for (int i = 0; i < size; i++){
      nums.add(reader.nextInt());
    }

    // Solution
    for (Integer n : nums){
      if (n == target){
        total++;
      }
    }

    System.out.println(total);
  }
}
