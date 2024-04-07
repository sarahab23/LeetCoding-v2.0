class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        int size = fruits.size(), low = 0, high = 0, result = INT_MIN;
        unordered_map<int,int> pluckedFruits;
        while(high < size){
          if(pluckedFruits[fruits[high]] > 0) pluckedFruits[fruits[high]]++;
            else pluckedFruits[fruits[high]] = 1;
            while(pluckedFruits.size() > 2){
                if(--pluckedFruits[fruits[low]] == 0) pluckedFruits.erase(fruits[low]);
                low++;
                    }
            result = max(result,high - low + 1);
            high++;
            }
        return result;
    }
};