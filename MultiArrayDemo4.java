package day06;

import java.util.Arrays;

public class MultiArrayDemo4 {

	public static void main(String[] args) {
		int[][] mm = {
				{100, 90},
				{85, 75, 65},
				{70, 60}
			};
		
		// 用 Java 8 Stream 來印出每一個元素
		Arrays.stream(mm) // {{100, 90},{85, 75, 65},{70, 60}}
			  .flatMapToInt(m -> Arrays.stream(m)) // {100, 90}  {85, 75, 65}  {70, 60}
			  .forEach(x -> System.out.println(x));

	}

}
