/*This script implements various sorting algortithms which includes Inserstion sort, Merge sort, Quick sort, Bubble sort
and Selection sort. There is a separate class which generate an array of integers for all the sorting algorithmn. The 
array will be same for all the algorithms. The size of array can be determined by user as per there conveniece.

Author: Naerayan Jat
Date: 6 February 2024
 */

// Importing random module.
import java.util.Random;


public class SortingAlgorithms{
    public static void main(String[] args) {
        InputGenerator.input();
        long startTime = System.currentTimeMillis();
        InsertionSort.sort();
        QuickSort.sort();
        MergeSort.sort();
        BubbleSort.sort();
        SelectionSort.sort();
        long endTime = System.currentTimeMillis();
        System.out.println("\nTotal time taken: " + (endTime  - startTime));
    }
}

// Implementing Insertion sort algorithm.
class InsertionSort{
    static int[] numbers = InputGenerator.numbers;
    public static void sort(){
        for (int i = 1; i < numbers.length; i++){
            for (int j = i; j > 0; j--){
                if (numbers[j] < numbers[j-1]){
                    swap(j, j-1, numbers);
                }else{
                    break;
                }
            }
        }
        System.out.print("\nThis is output of Insertion sort: ");
        for (int i: numbers){
            System.out.print(i + " ");
        }
    }

    static void swap(int i1, int i2, int[] numbers){
        int temp = numbers[i1];
        numbers[i1] = numbers[i2];
        numbers[i2] = temp;
    }
}


// Implementing quick sort algorithm.
class QuickSort{
    static int[] numbers = InputGenerator.numbers;
    static void quick(int start, int end){
        if (start < end){
            int j = partition(start, end);
            quick(start, j - 1);
            quick(j+1, end);
        }
    }

    static int partition(int start, int end){
        int pivot = start;
        int rear = end;
        while (pivot < rear){
            if (numbers[pivot] >= numbers[pivot + 1]){
                InsertionSort.swap(pivot, pivot+1, numbers);
                pivot++;
            }else{
                InsertionSort.swap(pivot+1, rear, numbers);
                rear--;
            }
        }
        return pivot;
    }

    static void sort(){
        quick(0, numbers.length - 1);
        System.out.print("\nThis is output of Qwick sort: ");
        for (int i: numbers){
            System.out.print(i + " ");
        }
    }
}


// Implementing Merge sort algorithm.
class MergeSort{
    static int[] numbers = InputGenerator.numbers;
    static void mergeSort(int[] arr, int l, int r) {
        if (l < r) {
            int m = (l + r) / 2;
            mergeSort(arr, l, m);
            mergeSort(arr, m + 1, r);
            merge(arr, l, m, r);
        }
    }

    static void merge(int[] arr, int p, int q, int r) {
        int n1 = q - p + 1;         // calculating length of left array.
        int n2 = r - q;             // calculating the length of right array.

        int L[] = new int[n1];
        int R[] = new int[n2];
        // Putting elements from arr to left and right array.
        for (int i = 0; i < n1; i++)
            L[i] = arr[p + i];
        for (int j = 0; j < n2; j++)
            R[j] = arr[q + 1 + j];

        int i, j, k;
        i = 0;
        j = 0;
        k = p;   // Pointer to keep track which index we need to put number.

        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
            } else {
            arr[k] = R[j];
            j++;
            }
            k++;
        }
        // Putting numbers from left array to array. 
        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }
        // Putting numbers from right array to array. 
        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }

    static void sort(){
        mergeSort(numbers, 0, numbers.length - 1);
        System.out.print("\nThis is output of Merge sort: ");
        for (int i: numbers){
            System.out.print(i + " ");
        }
    }
}


/* Online Java Compiler and Editor */
class BubbleSort{ 
    static int[] numbers = InputGenerator.numbers;
    static void bubble()    // function to implement bubble sort  
    {   int[] a = numbers;
        int n = a.length;  
        int i, j, temp; 
        for (i = 0; i < n; i++)  
        {  
            for (j = i + 1; j < n; j++)  
            {  
                if (a[j] < a[i])  
                {  
                    temp = a[i];  
                    a[i] = a[j];  
                    a[j] = temp;  
                }  
            }  
        }  
    }

    static void sort(){
        bubble();
        System.out.print("\nThis is output of Bubble sort: ");
        for (int i: numbers){
            System.out.print(i + " ");
        }
    }
}


class SelectionSort{
    static int[] numbers = InputGenerator.numbers;

    static void selection(){
        int size = numbers.length;
        for (int i = 0; i < size - 1; i++){
            int minIndex = i;
            int j = i + 1;
            while(j < size){
                if (numbers[minIndex] > numbers[j]){
                    minIndex = j;
                }
                j++;
            }
            if(minIndex != i){InsertionSort.swap(minIndex, j, numbers);}
        }
    }
    static void sort(){
        selection();
        System.out.print("\nThis is output of Selection sort: ");
        for (int i: numbers){
            System.out.print(i + " ");
        }
    }
}

class InputGenerator{
    static int size = 10;
    static int[] numbers = new int[size];
    public static void input(){
        Random r = new Random();
        r.setSeed(size);
        int i = 0;
        while (i < size ) {
            numbers[i] =  r.nextInt(5694);
            i++;
        }
        System.out.print("Numbers before sorting: ");
        for(int j: numbers){
            System.out.print(j + " ");
        }
        System.out.println();
    }
}
