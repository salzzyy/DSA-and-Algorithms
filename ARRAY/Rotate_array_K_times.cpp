// leetcode url - https://leetcode.com/problems/rotate-array/description/


//not a inplace-solution

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void solve(vector<int>&arr, int k, vector<int>&ans, int n){
    //1 2 3 4 5 6 7     k =3
    //5 6 7 1 2 3 4

    k = k % n;   // suppose k = 7, k %n = 7 %6 = 1 

    for( int i =0 ; i < n ; i ++){
        ans[(i+k) %n] = arr[i];
    }


}

int main(){
    //taking inputs of array
    
    int n ;
    cin>>n;
    vector<int>arr(n, 0);
    for( int i =0; i <n; i++){
        cin>>arr[i];
    }
    int k;
    cin>>k;
    vector<int> ans(n, 0);
    solve(arr, k, ans, n);
    for(int i : ans) cout<< i <<" ";
}
