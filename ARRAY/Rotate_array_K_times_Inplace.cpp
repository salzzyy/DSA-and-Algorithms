// leetcode url - https://leetcode.com/problems/rotate-array/description/
//inplace solution

#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

void rotate(vector<int>& arr, int i , int j){

    //inplace solution -> first rotate the whole array, then rotate till k, ,then roatate after k->n
    while( i < j){
        int b = arr[j];
        arr[j]=arr[i];
        arr[i]= b;
        
        i++;
        j--;

    }
}

int main(){
    int n ;
    cin>>n;
    vector<int>arr(n);
    for(int i=0 ; i <n; i ++){
        cin>> arr[i];
    }
    int k;  
    cin>>k;
    int i = 0;
    int j = n;
    rotate(arr,i=0, j=n-1);
    rotate(arr, i =0, j =k-1);
    rotate(arr, i = k, j = n-1);
    
    for( int i : arr) cout<<i <<" ";
}
