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
		
		// a는 6이고 비트 반전하면 -7
		System.out.println(~a); // -7
		
		System.out.println(!false); // true
		
		// 산술연산자
		System.out.println();
		System.out.println("산술연산자");
		
		int x = 10;
		int y = 6;
		
		System.out.println(x + y); // 16
		System.out.println(x - y); // 4
		System.out.println(x * y); // 60
		System.out.println(x / y); // 1
		System.out.println(x % y); // 4
		
		// 비교연산자
		System.out.println();
		System.out.println("비교연산자");
		
		int c = 10;
		
		System.out.println(c > 10); // false
		System.out.println(c != 10); // false
		System.out.println(c >= 10); // true
		System.out.println(c == 10); // true
		System.out.println(c != 10); // false
		
		// 문자열은 어떻게 비교?
		String d = "Hi";
		String e = "Hi";
		String f = new String("Hi");
		
		System.out.println(d == e); // true
		System.out.println(e == f); // false
		System.out.println(e.equals(f)); // true
		
		// 논리연산자
		System.out.println();
		System.out.println("논리연산자");
		
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
