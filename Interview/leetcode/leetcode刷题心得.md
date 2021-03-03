# [点击去B站：Leetcode力扣必备算法知识和练习题|手画图解版](https://b23.tv/bIQs1w)
[代码详见 ./ leetcodeTry.java](leetcodeTry.java)
## 双指针
1. 普通指针：两个指针向一个方向移动
2. 对撞指针：两个指针从两边来。例如[881](https://leetcode-cn.com/problems/boats-to-save-people/)。先调用Arrays.sort(people)对数组进行排序，再对撞。
3. 快慢指针：一个每次走一步，一个每次走两步。例如[141](https://leetcode-cn.com/problems/linked-list-cycle/submissions/)。注意判空时应当先判断head再判断head.next。fast同理

## 二分查找法
- 二分查找一定要有序
题目：
1. [704.二分](https://leetcode-cn.com/problems/binary-search/)
2. [35.搜索插入位置](https://leetcode-cn.com/problems/search-insert-position/)<br>注意中间的浮标（pos）应当表达成 $pos = head + \frac{tail-head}{2}$, 来避免直接写成 $pos = \frac{head + tail}{2}$ 可能出现超int的情况；<br>可以用`递归`，也可以用`while(head < tail)`循环
3. [162.寻找峰值](https://leetcode-cn.com/problems/find-peak-element/)<br>关键要抓住：**若nums[m] < nums[m+1], 则峰值在m右侧;若nums[m] > nums[m+1]，则峰值在m+1左侧**
4. [74.二维矩阵搜索](https://leetcode-cn.com/problems/search-a-2d-matrix/)<br>二维矩阵升序排列，直接将二维矩阵二分查找，令`left = 0, right = m * n - 1, xPos = ((left + right) / n), yPos = ((left + right) % n)`作为初始,开始二分

## 小技巧：滑动窗口
- 目的：减少循环中的计算量

举例：<br>给定数组s[n], 计算其中连续三个数之和的最大值
1. 暴力法
2. 滑动窗口法<br>窗口1 = s[0] + s[1] + s[2]<br>窗口2 = 窗口1 - s[0] + s[3]


例题：
1. [209.长度最小的子数组](https://leetcode-cn.com/problems/minimum-size-subarray-sum/) 
    - 对于非定长的数组，灵活分析决定是否能够采用滑动窗口
    - 两种方法：<br>1. 固定window长度，依次遍历，有合适就返回；再改变window长度进行下一次遍历;<br>2. 对一个窗口不断增长直到和超过target，然后逐个减去window的前面数字直导小于target，开始下一次
2. [1456.定长子串中元音的最大数目](https://leetcode-cn.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)<br>典型窗口
3. [1004.最大连续的1个数III](https://leetcode-cn.com/problems/max-consecutive-ones-iii/solution/hua-dong-chuang-kou-de-liang-chong-jie-j-8ses/)一个指向窗口左边（记作L），一个指向窗口右边（记作R），不断右移R直到[L, R]内的0个数大于K，然后右移L直到0个数等于K，判断是否更新答案

## 递归
自己调用自己<br>注意时间复杂度较高<br>例题：
1. 斐波拉契数列
2. [206.翻转链表](https://leetcode-cn.com/problems/reverse-linked-list)
3. [344.反转字符串](https://leetcode-cn.com/problems/reverse-string)
## 分治法
将大卫提分解为小问题，当然这里也用到了递归的思想<br>例题：
1. 归并排序
2. [169.多数数字](https://leetcode-cn.com/problems/majority-element)这里有下面几种方法：
   - 摩尔投票法：不同的数字相互抵消，最后剩下的就是最多的（前提：最多的数字大于数字总数的一般）
   - 排序：排序后选择 $nums[\dfrac{n}{2}]$, 一定为所求
   - 哈希表：统计，排序
   - 因为超过$\lfloor \dfrac{n}{2} \rfloor$ 的数组下标被众数占据了，这样我们随机挑选一个下标对应的元素并验证，有很大的概率能找到众数。因此，由于一个给定的下标对应的数字很有可能是众数，我们随机挑选一个下标，检查它是否是众数，如果是就返回，否则继续随机挑选。
3. [53.最大子序和](https://leetcode-cn.com/problems/maximum-subarray/)
   - 动态规划：比较一段数组的和和下一个数，选取较大的，同时更新
   - 分治。没看懂？？？？

4. [215.数组中的第K个最大元素](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/)<br>两种方法
   - 快速排序
   - 堆排序：建立一个大根堆，做 k−1 次删除操作后堆顶元素就是我们要找的答案
## 回溯法
1. [78.子集](https://leetcode-cn.com/problems/subsets/)<br>[具体题解](https://leetcode-cn.com/problems/subsets/solution/er-jin-zhi-wei-zhu-ge-mei-ju-dfssan-chong-si-lu-9c/)
   - 集合中的每个元素都可以选或者不选，用二进制和位运算来表示
      ```
      class Solution {
         List<Integer> t = new ArrayList<Integer>();
         List<List<Integer>> ans = new ArrayList<List<Integer>>();

         public List<List<Integer>> subsets(int[] nums) {
            int n = nums.length;
            for (int mask = 0; mask < (1 << n); ++mask) {
                  t.clear();
                  for (int i = 0; i < n; ++i) {
                     if ((mask & (1 << i)) != 0) {
                        t.add(nums[i]);
                     }
                  }
                  ans.add(new ArrayList<Integer>(t));
               }
               return ans;
            }
         }   
      ```
   - 逐个枚举，空集的幂集只有空集，每增加一个元素，让之前幂集中的每个集合，追加这个元素，就是新增的子集。
      ```
      //循环枚举
      public static List<List<Integer>> enumerate(int[] nums) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        res.add(new ArrayList<Integer>());
        for (Integer n : nums) {
            int size = res.size();
            for (int i = 0; i < size; i++) {
                List<Integer> newSub = new ArrayList<Integer>(res.get(i));
                newSub.add(n);
                res.add(newSub);
            }
         }
         return res;
      }

      //递归枚举
      public static void recursion(int[] nums, int i, List<List<Integer>> res) {
         if (i >= nums.length) return;
         int size = res.size();
         for (int j = 0; j < size; j++) {
               List<Integer> newSub = new ArrayList<Integer>(res.get(j));
               newSub.add(nums[i]);
               res.add(newSub);
         }
         recursion(nums, i + 1, res);
      }
      ```
   
   - 
2. []()<br>

3. []()<br>

4. []()<br>
## 深度优先

## 广度优先

## 并查集
### 并查集优化

## 贪心

## 记忆化搜索

## 动态规划
