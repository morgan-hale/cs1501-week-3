//Evelyn Tse
//eyt7ph 

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int a = digits.size() - 1;
        int z = digits[a];
        if(z != 9){
            z++;
            digits[a] = z;
        } else {
            while(z == 9){
                digits[a] = 0;
                a--;
                z = digits[a];
            }
        }
        return digits;
    }
};
