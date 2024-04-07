class Solution {
public:
    vector<int> getAverages(vector<int>& nums, int k) {
        int size = nums.size(), i, windowSize = 2*k + 1;
        vector<int> result(size, -1);
        if(size < windowSize) return result;
        vector<long long int> prefixSum(size + 1, 0);
        for(i = 0; i < size; i++) prefixSum[i+1] = prefixSum[i] + nums[i];
        for(i = k; i + k < size; i++) result[i] = floor((prefixSum[i + k + 1] - prefixSum[i - k])/windowSize);
        return result;
    }
};