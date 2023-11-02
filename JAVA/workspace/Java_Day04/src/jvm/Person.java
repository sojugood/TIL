package jvm;

public class Person {
	// 클래스 변수(인스턴스 생성 없이 접근 가능)
	// 모든 인스턴스가 공유한다.
	static int pCount; // 사람의 수를 세는 변수 선언
	
	// 인스턴스 변수
	// 인스턴스 마다 메모리를 할당한다.(힙 영역에 생성)
	String name;
	String hobby;
	int age;
	
	// static 영역에서는 non-static 영역을 직접 접근이 불가능
	// non-static 영역에서는 static 영역에 대한 접근이 가능
	
	// static : 클래스 로딩 시 클래스 영역에 할당(미리 올라가 있음)
	// non-static : 인스턴스 생성 시 인스턴스 당 메모리가 별도로 힙 영역에 할당
	
	
	// non-static 영역
	public void count() {
		System.out.println(pCount);
	}
	
//	// static 영역 : non-static 영역에 접근 불가
//	public static void info() {
//		System.out.println(name);
//	}
}
