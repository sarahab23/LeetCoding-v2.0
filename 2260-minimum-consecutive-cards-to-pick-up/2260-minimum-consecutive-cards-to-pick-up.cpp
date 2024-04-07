class Solution {
public:
    int minimumCardPickup(vector<int>& cards) {
        int result = INT_MAX, i, size = cards.size();
        unordered_map<int,int> cardsPicked;
        for(i = 0; i < size; i++){
            if(cardsPicked.find(cards[i]) != cardsPicked.end()){
                result = min(result, i - cardsPicked[cards[i]] + 1);
       }
            cardsPicked[cards[i]] = i;
            }
        return (result == INT_MAX ? -1 : result);
    }
};