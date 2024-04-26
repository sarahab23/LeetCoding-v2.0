// Using ASCII, easier to read, code and understand solution
class Solution {
public:
    bool isPalindrome(string s) {
        string newString = "";
        for(char c:s){
            if((c >= '0' && c <= '9') || (c >= 'a' && c <= 'z'))
                newString += c;
            else if(c >= 'A' && c <= 'Z')
                newString += c - 'A' + 'a';
        }
        int size = newString.size();
        bool result = true;
        if(size < 2) return result;
        int i = 0, j = size - 1;
        while(j > i){
            if(newString[i++] != newString[j--]){
                result = false;
                break;
            }
        }
        return result;
    }
};
