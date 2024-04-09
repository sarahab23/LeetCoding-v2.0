class Solution {
public:
    string minWindow(string s, string t) {
        int n = t.size(), m = s.size(), counter = 0, head = -1, resultSize = INT_MAX;
        int low = 0, high = 0;
        vector<int> letterCount(256,0);
        for(char c:t) letterCount[c]++;
        while(high < m){
            if(letterCount[s[high]] > 0) counter++;
            letterCount[s[high]]--;
            while(counter == n){
                if(high - low + 1 < resultSize){
                    resultSize = high - low + 1;
                    head = low;
                }
                if(letterCount[s[low]] == 0) counter--;
                letterCount[s[low]]++;
                low++;
            }
            high++;
        }
        return (head == -1? "" : s.substr(head,resultSize));
    }
};