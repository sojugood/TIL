package java01;

public class intro03_Operator {
	public static void main(String[] args) {
		int a = 5;
		System.out.println(a++); // 5
		System.out.println(++a); // 7
		System.out.println(--a); // 6
		System.out.println(a); // 6
		System.out.println(a--); // 6
		System.out.println(a++); // 5
		
		System.out.println(-a); // -6
		
		// a�� 6�̰� ��Ʈ �����ϸ� -7
		System.out.println(~a); // -7
		
		System.out.println(!false); // true
		
		// ���������
		System.out.println();
		System.out.println("���������");
		
		int x = 10;
		int y = 6;
		
		System.out.println(x + y); // 16
		System.out.println(x - y); // 4
		System.out.println(x * y); // 60
		System.out.println(x / y); // 1
		System.out.println(x % y); // 4
		
		// �񱳿�����
		System.out.println();
		System.out.println("�񱳿�����");
		
		int c = 10;
		
		System.out.println(c > 10); // false
		System.out.println(c != 10); // false
		System.out.println(c >= 10); // true
		System.out.println(c == 10); // true
		System.out.println(c != 10); // false
		
		// ���ڿ��� ��� ��?
		String d = "Hi";
		String e = "Hi";
		String f = new String("Hi");
		
		System.out.println(d == e); // true
		System.out.println(e == f); // false
		System.out.println(e.equals(f)); // true
		
		// ��������
		System.out.println();
		System.out.println("��������");
		
		int aa = 10;
		int bb = 20;
		
		System.out.println(aa > 5 && bb > 5); // true
		System.out.println(aa > 5 && bb < 5); // false
		System.out.println(aa < 5 && bb > 5); // false
		System.out.println(aa < 5 && bb < 5); // false
		
		System.out.println(aa > 5 || bb > 5); // true
		System.out.println(aa > 5 || bb < 5); // true
		System.out.println(aa < 5 || bb > 5); // true
		System.out.println(aa < 5 || bb < 5); // false
		
		System.out.println(!(aa < 5 && bb < 5)); // true
		
	}
}
