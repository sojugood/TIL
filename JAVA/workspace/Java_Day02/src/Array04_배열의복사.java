import java.util.Arrays;

public class Array04_배열의복사 {
	public static void main(String[] args) {
		int[] nums = { 42, 5, 3, 7, 23, 15 };
		// 배열 복사

		// 전통적인 복사방식
		int[] tmp = new int[nums.length * 2];
		for (int i = 0; i < nums.length; i++) {
			tmp[i] = nums[i];
		}
		System.out.println(Arrays.toString(tmp));

		// Arrays.copyOf(원본배열, 복사할 배열의 크기)
		int[] tmp2 = Arrays.copyOf(nums, nums.length * 2);
		System.out.println(Arrays.toString(tmp2));

		// System.arraycopy(원본배열, 원본배열시작점, 복사배열, 복사배열시작점, 복사할크기)
		int[] tmp3 = new int[nums.length * 2];
		System.arraycopy(nums, 0, tmp3, 0, nums.length);
		System.out.println(Arrays.toString(tmp3));
	}
}
