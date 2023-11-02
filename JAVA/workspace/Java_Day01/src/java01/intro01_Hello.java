package java01;

public class intro01_Hello {
	// crtl + space : 자동완성
	public static void main(String[] args) {
		// sysout
		System.out.println("Hello SSAFY!!");
		
		// println은 줄바꿈(new Line) 포함
		System.out.print("Hello SSAFY!!");
		System.out.println("Hello SSAFY!!");
		
		// print("\n")하면 줄바꿈
		System.out.print("Hello SSAFY!!");
		System.out.print("\n");
		System.out.print("Hello SSAFY!!\n");
		System.out.println("Hello SSAFY!!");
		
		// printf
		System.out.printf("%s\n", "Hello World!!");
		System.out.printf("%c\n", 'W');
		// 4칸을 확보한 뒤 오른쪽부터
		System.out.printf("%4d\n", 10);
		// 4칸을 확보한 뒤 왼쪽부터
		System.out.printf("%-4d\n", 10);
		// 4칸을 확보한 뒤 오른쪽부터(빈칸은 0으로)
		System.out.printf("%04d\n", 10);
		// 실수
		System.out.printf("%f\n", 10.1);
		// 실수(소수점 둘째자리까지)(셋째자리에서 반올림)
		System.out.printf("%.2f\n", 10.105);

	}
}
