public class Array05_최대최소값찾기 {
	public static void main(String[] args) {
		int[] nums = { 42, 5, 3, 7, 23, 15 };

		// 최대값과 최소값을 찾는 방법

		// 조건문과 반복문 활용

		int min = Integer.MAX_VALUE;
		int max = Integer.MIN_VALUE;

		for (int num : nums) {
			min = Math.min(min, num);
			max = Math.max(max, num);
		}
		System.out.println(min + " " + max);
	}
}
