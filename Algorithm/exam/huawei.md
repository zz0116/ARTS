考虑了很久java代码怎么放在这里，是用ide直接在这个文件夹建工程还是只有一个文件贴代码，区别就在于是要方便还是这里只承载记录的作用。暂时就用md文件这么放，后面要建工程再说了。

这是昨天上午做的华为OD招聘的题目，OD招聘是变相的社招。华为使用牛客网进行机试，一个小时，一道题，题目很简单，记录如下。

```java
import java.util.HashSet;
import java.util.Scanner;

/**
 * 华为笔试，输入两行各四个非负整数，数字之间空格分离，
 * 判断两行的相同数字，
 * 数字相同而且位置相同的，以及数字相同位置不同的，
 * 两行的数字各自没有重复的，
 * 相同数字和位置的计为x个，相同数字不同位置记为y个，
 * 输出xAyB。
 * 如下，输入1 2 3 4,1 2 5 3，输出2A1B。
 * 1 2 3 4
 * 1 2 5 3
 * 2A1B
 *
 * @author 张远卓
 * @date 2019/11/2
 */
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        // 两行为两个数组
        String[] array1 = in.nextLine().split(" ");
        String[] array2 = in.nextLine().split(" ");
        int length = 4;
        int a = 0;
        HashSet<String> bSet = new HashSet<String>();
        for (int i = 0; i < length; i++) {
            String s1 = array1[i];
            String s2 = array2[i];
            // 先判断完全一样的，A的情况
            if (s1.equals(s2)) {
                a++;
            } else {
                // 再判断顺序不一样但有交集的情况
                bSet.add(s1);
                bSet.add(s2);
            }
        }
        int b = length * 2 - a * 2 - bSet.size();
        System.out.println(a + "A" + b + "B");
    }
}
```