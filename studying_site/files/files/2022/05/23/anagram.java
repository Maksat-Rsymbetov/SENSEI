import java.util.*;
public class Main {
	public static void main(String[] args) {
		System.out.println((int)'a');
		System.out.println((int)'z');
	}

	public static int anagram(String s){
		int l = s.length();
		boolean even = (l % 2 == 0);
		Hashtable<Character, Integer> set1 = new Hashtable<>();
		Hashtable<Character, Integer> set2 = new Hashtable<>();
		for(int i = 0; i < l / 2; i++){
			char c1 = s.charAt(i);
			char c2 = even? s.charAt(i + l / 2) : s.charAt(i + 1 + l / 2);
			if(set1.contains(c1)) set1.put(c1, set1.get(c1) + 1);
			else set1.put(c1, 1);

			if(set2.contains(c2)) set2.put(c2, set2.get(c2) + 1);
			else set2.put(c2, 1);
		}
		int ans = 0;
		for(char c: set1.keySet()){
			if(set2.containsKey(c)) ans += Math.abs(set1.get(c) - set2.get(c));
			else ans += set1.get(c);
		}
		return ans;
	}

	public static int gemstones(List<String> arr){
		Hashtable<Character, Integer> table = new Hashtable<>();
		ArrayList<HashSet<Character>> chars = new ArrayList<>();
		for(String s: arr){
			HashSet<Character> set = new HashSet<>();
			for(int i = 0; i < s.length(); i++){
				set.add(s.charAt(i));
			}
			chars.add(set);
		}

		for(HashSet<Character> set: chars){
			for(char c: set){
				if(table.containsKey(c)) table.put(c, table.get(c) + 1);
				else table.put(c, 1);
			}
		}
		int size = arr.size();
		int ans = 0;
		for(char c: table.keySet()){
			if(table.get(c) == size) ans++;
		}
		return ans;
	}

	public static int gemstones(List<String> arr){
		Hashtable<Character, Integer> table = new Hashtable<>();
		ArrayList<HashSet<Character>> chars = new ArrayList<>();
		for(String s: arr){
			HashSet<Character> set = new HashSet<>();
			for(int i = 0; i < s.length(); i++){
				set.add(s.charAt(i));
			}
			chars.add(set);
		}

		for(HashSet<Character> set: chars){
			for(char c: set){
				if(table.containsKey(c)) table.put(c, table.get(c) + 1);
				else table.put(c, 1);
			}
		}
		int size = arr.size();
		int ans = 0;
		for(char c: table.keySet()){
			if(table.get(c) == size) ans++;
		}
		return ans;
	}

	public static String funnyString(String s) {
		ArrayList<Integer> list1 = new ArrayList<>();
		ArrayList<Integer> list2 = new ArrayList<>();

		for(int i = 0; i < s.length() - 1; i++){
			int a = (int)s.charAt(i), b = (int)s.charAt(i + 1);
			list1.add(Math.abs(a - b));
		}
		for(int i = s.length() - 1; i >= 0; i--){
			int a = (int)s.charAt(i), b = (int)s.charAt(i + 1);
			list2.add(Math.abs(a - b));
		}
		return (list1.equals(list2))? "Funny" : "Not Funny";
	}
}


