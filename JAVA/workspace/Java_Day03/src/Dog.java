
public class Dog {
	String name;
	
	// 기본 생성자(매개변수 X)
	// 클래스명과 동일하게 작성, 매개변수 X, 반환타입 X
	public Dog() {
		this("기본");
		System.out.println("기본생성자");
		// 기본(default) 생성자 : 클래스 내에 생성자가 하나도 정의되어 있지 않을 경우
		// JVM이 자동으로 제공하는 생성자
	}
	

//	public Dog(String n) {
//		name = n;
//	}
	
	public Dog(String name) {
		this.name = name;
	}
}
