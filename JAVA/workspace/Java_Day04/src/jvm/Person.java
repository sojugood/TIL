package jvm;

public class Person {
	// Ŭ���� ����(�ν��Ͻ� ���� ���� ���� ����)
	// ��� �ν��Ͻ��� �����Ѵ�.
	static int pCount; // ����� ���� ���� ���� ����
	
	// �ν��Ͻ� ����
	// �ν��Ͻ� ���� �޸𸮸� �Ҵ��Ѵ�.(�� ������ ����)
	String name;
	String hobby;
	int age;
	
	// static ���������� non-static ������ ���� ������ �Ұ���
	// non-static ���������� static ������ ���� ������ ����
	
	// static : Ŭ���� �ε� �� Ŭ���� ������ �Ҵ�(�̸� �ö� ����)
	// non-static : �ν��Ͻ� ���� �� �ν��Ͻ� �� �޸𸮰� ������ �� ������ �Ҵ�
	
	
	// non-static ����
	public void count() {
		System.out.println(pCount);
	}
	
//	// static ���� : non-static ������ ���� �Ұ�
//	public static void info() {
//		System.out.println(name);
//	}
}
