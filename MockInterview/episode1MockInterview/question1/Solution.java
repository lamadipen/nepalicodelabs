 /**
 
 Question 1: 

 Given an array of integers greater than zero, find if there is a way to
  split the array in two (without reordering any elements) such that the
  numbers before the split add up to the numbers after the split. If so,
  print the two resulting arrays.

  [2, 3, 4, 6, 1,  5, 9,]
  l                  r  
 
 In [1]: can_partition([5, 2, 3]) 
 Output [1]: ([5], [2, 3]) 
 Return [1]: True 
  
 In [2]: can_partition([2, 3, 2, 1, 1, 1, 2, 1, 1]) 
 Output [2]([2, 3, 2], [1, 1, 1, 2, 1, 1]) 
 Return [2]: True 
  
 In [3]: can_partition([1, 1, 3]) 
 Return [3]: False 
  
 In [4]: can_partition([1, 1, 3, 1]) 
 Return [4]: False
 **/

import java.io.*;
import java.util.*;

class Solution {
  public static void main(String[] args) {

  }

  public boolean canSplit(int[] arr) {
    int left = 0;
    int right = arr.length - 1;

    int leftSum = arr[0];
    int rightSum = arr[right];
    int[] leftArray = new int[arr.length];
    int[] rightArray = new int[arr.length];

    while (left < right) {
      if (leftSum < rightSum && left != 0) {
        leftSum += arr[left];
        leftArray[left] = arr[left];
        left++;
      } else if (rightSum < leftSum && right != arr.length - 1) {
        rightSum += arr[right]
        rightArray[right] = arr[right];
        right--;
      } else {
        printResultArray(leftArray, rightArray);
        return true;
      }
    }
    return false;
    //here print if the there is no result
  }

  public void printResultArray(int[] leftArr, int[] rightArr) {}

}