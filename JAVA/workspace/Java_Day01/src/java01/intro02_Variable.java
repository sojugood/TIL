package java01;

public class intro02_Variable {
	public static void main(String[] args) {
		// ���� ���� : �ڷ��� ���� �̸�
		int age;
		// ���� �Ҵ� : �����̸� = ��
		age = 100;
		// ���� �ʱ�ȭ
		// ����� ���ÿ� �Ҵ��� �ϸ� �ʱ�ȭ��� �Ѵ�.
		int money = 10000;
		
		System.out.println(age);
		System.out.println(money);
		
		// ������(�Ϲ���) ������ �� ��ȯ
		// ������ ���� ������ ���� ���� ������ ���� �����ϴ� ��
		byte a = 50;
		int j = a;
		System.out.println(j);
		
		// ����� ������ �� ��ȯ
		// �� ��ȯ ������ ��� : (Ÿ��)��;
		// ������ ���� ������ ���� ���� ������ ���� �����ϴ� ��
		long i = 10000000;
		int b = (int)i;
		System.out.println(b);
	}
}
