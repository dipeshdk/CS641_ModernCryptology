#include<bits/stdc++.h>
using namespace std;

int IP[] = {
  58,50,42, 34,26,18,10,2,
  60,52,44,36,28,20,12,4,
  62,54, 46, 38, 30, 22, 14,6,
  64, 56, 48, 40,32,24, 16, 8,
  57, 49, 41, 33,25,17, 9,1,
  59, 51,43,35,27,19,11,3,
  61,53,45,37,29,21,13, 5,
  63,55, 47,39,31,23,15,7
};

string strToBin(const string& s){
    string bin = "";
    for(int i = 0; i < s.size(); i++){
        int a = (unsigned int)(s[i] - 'f');
        for(int j = i*4; j < i*4 + 4; j++){
            char x =  '0' + ((a >> (3-(j-(i*4)))) & 01);
            bin.push_back(x);
        }
    }
    return bin;
}

string strxor(const string& s1, const string& s2){
    string s = "";
    for(int i = 0; i < s1.size(); i++){
        if(s1[i] == s2[i])
            s.push_back('0');
        else
            s.push_back('1');
    }
    return s;
}

int main(){
    string s1 = "mgmphkljiulfqptu";
    string s2 = "mgmppkmjiulfuptu";
    string b1 = strToBin(s1);
    string b2 = strToBin(s2);
    string sxor = strxor(b1,b2);
    string ans = "";
    for(int i = 0; i < sxor.size(); i++){
        ans.push_back(sxor[IP[i]-1]);
    }
    cout << ans << endl;
}