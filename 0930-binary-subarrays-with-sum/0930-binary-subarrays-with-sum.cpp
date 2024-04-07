class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        int result = 0, size = nums.size(), prefSum = 0;
        unordered_map<int,int> prefSumCount;
        prefSumCount[0] = 1;
        for(int i = 0; i < size; i++){
            prefSum += nums[i];
            result += prefSumCount[prefSum - goal];
            prefSumCount[prefSum]++;
        }
        return result;
    }
};