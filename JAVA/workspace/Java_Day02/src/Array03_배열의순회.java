import java.util.Arrays;

public class Array03_배열의순회 {
	public static void main(String[] args) {
		int[] nums = { 42, 5, 3, 7, 23, 15 };

		// 반복문을 통해 순회
//		for (int i = 0; i < nums.length; i++) {
//			System.out.println(nums[i]);
//		}

		// for-each
		// 가독성이 향상된 for문
//		for (자료형 변수명 : 반복할 수 있는 것) {
//			
//		}
//		for (int n : nums) {
//			System.out.println(n);
//		}

		// 읽기(조회)만 가능, 수정 불가
//		for (int x : nums) {
////			x = x * 2;
//			x *= 2;
//		}
//		
//		for (int x : nums) {
//			System.out.println(x);
//		}
//		
		for (int i = 0; i < nums.length; i++) {
			nums[i] *= 2;
		}

		for (int x : nums) {
			System.out.println(x);
		}

		// 배열안의 값이 궁금할 때 사용하면 바로 볼 수 있음
		System.out.println(Arrays.toString(nums));
	}
}
