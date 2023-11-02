
public class Array01_생성 {
	public static void main(String[] args) {
		// 1차원 배열을 선언하는 방법
		int[] score1; // 이 방식을 권장
		int score2[];

		// 배열을 생성하는 방법
		// 1. 자료형[] 이름 = new 자료형[길이]; 값은 자료형의 초기값으로 초기화
		int[] score3 = new int[5]; // int형의 기본값은 0이다.

		// 2. 자료형[] 이름 = new 자료형[]{1, 2, 3, 4};
		int[] score4 = new int[] { 1, 2, 3, 4 };

		// 3. 자료형[] 이름 = {1, 2, 3, 4}; // 선언과 동시에 초기화
		int[] score5 = { 1, 2, 3, 4 }; // 이 방법은 약간의 제약사항이 있다.

		score3 = new int[6];
		score3 = new int[] { 1, 2, 3, 4, 5 };
//		score3 = {1, 2, 3, 4, 5}; // 이건 안된다.
		
		int[] score6 = new int[5];
		
		score6[0] = 10;
		score6[1] = 20;
//		score6[5] = 60; // 인덱스 범위 초과
	}
}
