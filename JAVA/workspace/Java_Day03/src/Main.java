
public class Main {
	public static void main(String[] args) {
		Class01 person = new Class01();
		person.name = "홍길동";
		person.age = 25;
		person.hobby = "골프";
		person.info();
		
		Class01 person2 = new Class01();
		// 묵시적 형 변환 가능
		person2.study((byte)10);
		// 메서드 오버로딩 하여서 문제 발생 X
		person2.study(10L);
	}
}
