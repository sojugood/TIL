import java.util.Arrays;

public class Array06_빈도수구하기 {
	public static void main(String[] args) {
		int[] nums = { 3, 7, 2, 5, 7, 7, 9, 2, 8, 1, 1, 5, 3 };
		
		int[] count = new int[10];
		
		for (int i = 0; i < nums.length; i++) {
			count[nums[i]]++;
		}
		
		System.out.println(Arrays.toString(count));
	}
}
