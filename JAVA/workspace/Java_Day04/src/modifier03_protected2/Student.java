package modifier03_protected2;

import modifier03_protected.Person;

public class Student extends Person {
	public static void main(String[] args) {
		Student s = new Student();
		// ����� ����
		// �ٸ���Ű�������� protected Ư���� ������ ����	
		s.age = 10;
		s.name = "Kim";
	}
}
