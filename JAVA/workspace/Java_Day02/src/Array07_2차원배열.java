import java.util.Arrays;

public class Array07_2차원배열 {
	public static void main(String[] args) {
		int[][] arr1; // 권장
		int[] arr2[];
		int arr3[][];
		
		// 생성
		int[][] arr4 = new int[5][5];
		
		int[][] arr5 = new int[5][]; // 행의 길이만 넣었다.
		System.out.println(arr5[1]);
	}
}
