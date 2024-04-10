class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int low = 0, high = 0, size = nums.size();
        multiset<int> currentWindow;
        vector<int> result;
        while(high < size){
            if(high - low + 1 < k){
                currentWindow.insert(nums[high]);
                high++;  
            }
            else{
                currentWindow.insert(nums[high]);
                auto maxNum = currentWindow.rbegin();
                result.push_back(*maxNum);
                currentWindow.erase(currentWindow.find(nums[low]));
                low++;
                high++;
            }
        }
        return result;
    }
};