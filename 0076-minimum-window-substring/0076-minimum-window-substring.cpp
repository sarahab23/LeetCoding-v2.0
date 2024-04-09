class Solution {
public:
    string minWindow(string s, string t) {
        int low = 0, high = 0, head = -1, sizeOfWindow = INT_MAX, counter = t.size();
        int n = t.size(), m = s.size();
        vector<int> letterCount(128,0);
        for(char c : t) letterCount[c]++;
        while(high < m){
            if(letterCount[s[high++]]-- > 0) counter--;
            while(counter == 0){
                if(high - low < sizeOfWindow){
                    sizeOfWindow = high - low;
                    head = low;
                }
                if(letterCount[s[low++]]++ == 0) counter++;
            }
        }
        return (head == -1? "" : s.substr(head,sizeOfWindow));
    }
};