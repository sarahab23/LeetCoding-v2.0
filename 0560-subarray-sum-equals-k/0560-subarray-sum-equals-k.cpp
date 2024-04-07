class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int size = nums.size(), prefSum = 0, result = 0;
        unordered_map<int,int> prefSumCount;
        prefSumCount[0] = 1;
       for(int i = 0; i < size; i++){
            prefSum += nums[i];
            result = result + prefSumCount[prefSum - k]; 
            prefSumCount[prefSum]++;
        }
        return result;
    }
};