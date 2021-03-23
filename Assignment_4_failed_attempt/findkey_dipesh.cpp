#include<iostream>
#include<fstream>
#include<vector>
#include<bits/stdc++.h>

#define BYTE unsigned char

using namespace std;
#define INT unsigned int

INT INV_P[] = {
	9, 17, 23, 31,
	13, 28, 2, 18,
	24, 16, 30, 6,
	26, 20, 10, 1,
	8, 14, 25, 3,
	4, 29, 11, 19,
	32, 12, 22, 7,
	5, 27, 15, 21,
};

INT E[] = {
  32, 1, 2, 3, 4, 5,
  4, 5,6, 7, 8, 9,
  8, 9, 10, 11, 12, 13,
  12, 13, 14, 15, 16, 17, 
  16, 17, 18, 19, 20, 21, 
  20, 21, 22, 23, 24, 25, 
  24, 25, 26, 27, 28, 29,
  28, 29, 30, 31, 32, 1
};

INT S[8][64]=
{
  14, 4, 13, 1, 2, 15, 11, 8, 3 , 10, 6, 12, 5, 9, 0, 7,
  0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
  4, 1 , 14, 8, 13, 6, 2, 11, 15, 12, 9, 7,3, 10, 5, 0,
  15, 12, 8,2,4, 9, 1,7 , 5, 11, 3, 14, 10, 0, 6, 13 ,
  
  15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0,5, 10,
  3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
  0, 14, 7, 11, 10, 4, 13, 1, 5, 8,12, 6, 9, 3, 2, 15,
  13, 8, 10, 1, 3, 15, 4, 2,11,6, 7, 12, 0,5, 14, 9,
  
  10, 0, 9,14,6,3,15,5, 1, 13, 12, 7, 11, 4,2,8,
  13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
  13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12,5, 10, 14, 7,
  1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12,
  
  7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
  13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
  10, 6, 9, 0, 12, 11, 7, 13, 15, 1 , 3, 14, 5, 2, 8, 4, 
  3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14,
  
  2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9, 
  14, 11,2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6, 
  4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14, 
  11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3, 
  
  12, 1, 10, 15, 9, 2, 6,8, 0, 13, 3, 4, 14, 7, 5, 11, 
  10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8, 
  9, 14, 15, 5, 2,8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6, 
  4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13, 
  
  4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
  13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
  1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2, 
  6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12,
  
  13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12,7, 
  1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2, 
  7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8, 
  2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11 };

INT RFP[] = {
  8,40,16,48,24,56,32,64,
  7, 39,15,47,23,55,31,63,
  6,38,14,46,22,54,30,62,
  5,37,13,45, 21,53,29,61,
  4,36,12,44,20,52,28,60,
  3, 35, 11,43,19,51,27,59,
  2, 34, 10, 42,18, 50,26,58,
  1,33,9,41, 17, 49, 25,57,
};

INT RFP_INV[] = {
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7,
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8
};

vector< vector<string> > take_input(string filename, const int& pairs ){
    ifstream fin;
    fin.open(filename);
    string line;
    vector< vector<string> > cipherPairs(pairs, vector<string> (2, ""));
    if(!fin) return cipherPairs;
    for(int i = 0 ; i < pairs ; i++){
        getline(fin, line);
        cipherPairs[i][0] = line;
        getline(fin, line);
        cipherPairs[i][1] = line;
    }
    fin.close();
    return cipherPairs;
}

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

int binToDec(string& Exp, int s, int e){
    int x = 0;
    for (int i = s; i < e; i++){
        if(Exp[i] == '1')
            x = (x << 1)+1;
        else
            x = (x << 1)+0;    
    }
    return x;
}

vector<int> genF(const vector<int>& preS, int j){
    int k = 6*j;
    int t = preS[k];
    t = (t<<1) | preS[k+5];
    t = (t<<1) | preS[k+1];
    t = (t<<1) | preS[k+2];
    t = (t<<1) | preS[k+3];
    t = (t<<1) | preS[k+4];
    /* fetch t th entry fron jth sbox */
    t = S[j][t];
    /* generate 4-bit block from s-box entry */
    vector<int> f (4,0);
    f[0] = ((t >> 3) & 1);
    f[1] = ((t >> 2) & 1);
    f[2] = ((t >> 1) & 1);
    f[3] = (t &1);
    return f;
}

int main(){
    string input_filename = "merge_output_1.txt";
    int pairs = 3000;

    vector< vector<string> > cipherPairs = take_input(input_filename, pairs);

    unordered_map<int,int> umap;

    for(int h = 0; h < pairs; h++){
        string out1 = cipherPairs[h][0];
        string out2 = cipherPairs[h][1];
        // Function to convert the Ciphertext to binary
        string oo1 = strToBin(out1);
        string oo2 = strToBin(out2);
        // Function to apply inverse permutation RFP to ciphertext
        string o1 = "";
        string o2 = "";
        for(int i = 0; i < 64; i++){
            o1.push_back(oo1[RFP_INV[i]-1]);
            o2.push_back(oo2[RFP_INV[i]-1]);
        }
        
        // Expansion
        string Exp1 = "", Exp2="";
        for(int i =0 ;i < 48;i++){
            Exp1.push_back(o1[E[i]-1]);
            Exp2.push_back(o2[E[i]-1]);
        }
        string Exp = strxor(Exp1,Exp2);

        // Function to XOR o1 and o2 and store in o
        string o = strxor(o1,o2);
        string C = "00000100000000000000000000000000";
        string F = "";
        for(int i = 0; i < 32; i++){
            if(C[i] == o[i+32]) F.push_back('0');
            else F.push_back('1');
        }

        // Inverse Permute F to get output of S box in Round 6
        string FP = "";
        for(int i = 0; i < 32; i++){
            FP.push_back(F[INV_P[i]-1]);
        }
        // Expand right half of 5th round
        
        // for(int j = 0; j < 48; j++){
        //     Exp1.push_back(o1[E[j]]);
        //     Exp2.push_back(o2[E[j]]);
        //     Exp.push_back(o[E[j]]);
        // }
        vector<int> preS1(48), preS2(48);
        int num = 5;
        set<int> pkeys[5];
        for(int j = 0; j < 8; j++){
            if((j == 0) || (j == 2) || (j == 3)) continue;
            num--;
            int x = binToDec(Exp, j*6, j*6+6); // XOR of input to Sj
            int x1 = binToDec(Exp1, j*6, j*6 + 6);
            int x2 = binToDec(Exp2, j*6, j*6 + 6);
            int s_out = binToDec(FP, j*4, j*4 + 4);
            for(int i = 0; i < 64; i++){
                int k= 6*j;
                int y = x1^i;
                int z = x2^i;
                for(int a = 0; a < 6; a++){
                    preS1[a+k] = (y >> (5-a)) & 01;
                    preS2[a+k] = (z >> (5-a)) & 01;
                }
                vector<int> f1 = genF(preS1, j);
                vector<int> f2 = genF(preS2, j);
                INT w = 0;
                for(int i = 0; i < 4; i++){
                    w = w + ((f1[i]^f2[i]) << (3-i));
                }
                if(s_out == w) pkeys[4-num].insert(i);
            }
        }

        for(auto itr1: pkeys[0]) for(auto itr2: pkeys[1])
            for(auto itr3: pkeys[2]) for(auto itr4: pkeys[3])
                for(auto itr5: pkeys[4]){
                    int key = itr1 << 24;
                    key+= (itr2<<18);
                    key+= (itr3<<12);
                    key+= (itr4<<6);
                    key+= (itr5);
                    // cout << itr1 << " " << itr2 << " " << itr3 << " " << itr4 << " " << itr5 << endl;
                    // cout << key << endl;
                    if(umap.find(key) == umap.end()) umap[key] = 1;
                    else umap[key]++;
                }
    }

    // 2, 5, 6, 7, 8
    INT k2, k5, k6, k7, k8;
    int max_key = 0;
    int mx = 0;

    for(auto itr1: umap){
        if(itr1.second > 1){
            cout << "key =  "<< itr1.first <<  " num = " << itr1.second << endl;;
        }
        if(mx < itr1.second){
            max_key = itr1.first;
            mx = itr1.second;
        }
    }

    k2 = (max_key >> (4*6)) & 0x3F;
    k5 = (max_key >> (3*6)) & 0x3F;
    k6 = (max_key >> (2*6)) & 0x3F;
    k7 = (max_key >> (1*6)) & 0x3F;
    k8 = (max_key >> (0*6)) & 0x3F;

    printf("k2 = %u, k5 = %u, k6 = %u, k7 = %u, k8 = %u\n", k2, k5, k6, k7, k8);

}