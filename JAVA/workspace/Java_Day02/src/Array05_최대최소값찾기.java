public class Array05_�ִ��ּҰ�ã�� {
	public static void main(String[] args) {
		int[] nums = { 42, 5, 3, 7, 23, 15 };

		// �ִ밪�� �ּҰ��� ã�� ���

		// ���ǹ��� �ݺ��� Ȱ��

		int min = Integer.MAX_VALUE;
		int max = Integer.MIN_VALUE;

		for (int num : nums) {
			min = Math.min(min, num);
			max = Math.max(max, num);
		}
		System.out.println(min + " " + max);
	}
}
