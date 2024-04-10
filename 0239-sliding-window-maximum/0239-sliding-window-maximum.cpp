class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int low = 0, high = 0, size = nums.size();
        multiset<int> currentWindow;
        vector<int> result;
        while(high < size){
            currentWindow.insert(nums[high]);  
            if(high - low + 1 >= k){
                result.push_back(*currentWindow.rbegin());
                currentWindow.erase(currentWindow.find(nums[low]));
                low++;
            }
            high++;
        }
        return result;
    }
};