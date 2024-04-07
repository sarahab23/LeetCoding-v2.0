class Solution {
public:
    int numOfSubarrays(vector<int>& arr, int k, int threshold) {
        int size = arr.size(), i = 0, result = 0, windowSum = 0;
       for(i = 0; i < size; i++){
            windowSum += arr[i];
            if(i >= k - 1){
                if(windowSum/k >= threshold) result++;
                windowSum -= arr[i - k + 1];
            }
        }
        return result;
    }
};