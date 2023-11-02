package java01;

public class intro02_Variable {
	public static void main(String[] args) {
		// 변수 선언 : 자료형 변수 이름
		int age;
		// 변수 할당 : 변수이름 = 값
		age = 100;
		// 변수 초기화
		// 선언과 동시에 할당을 하면 초기화라고 한다.
		int money = 10000;
		
		System.out.println(age);
		System.out.println(money);
		
		// 묵시적(암묵적) 데이터 형 변환
		// 범위가 넓은 데이터 형에 좁은 데이터 형을 대입하는 것
		byte a = 50;
		int j = a;
		System.out.println(j);
		
		// 명시적 데이터 형 변환
		// 형 변환 연산자 사용 : (타입)값;
		// 범위가 좁은 데이터 형에 넓은 데이터 형을 대입하는 것
		long i = 10000000;
		int b = (int)i;
		System.out.println(b);
	}
}
