
public class Main {
	public static void main(String[] args) {
		Class01 person = new Class01();
		person.name = "ȫ�浿";
		person.age = 25;
		person.hobby = "����";
		person.info();
		
		Class01 person2 = new Class01();
		// ������ �� ��ȯ ����
		person2.study((byte)10);
		// �޼��� �����ε� �Ͽ��� ���� �߻� X
		person2.study(10L);
	}
}
