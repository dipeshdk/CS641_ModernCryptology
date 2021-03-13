#include<iostream>
#include<fstream>

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

int main(){
    ifstream fin;
    fin.open("final_outputs_2.txt");
    string line;
    string cipherPairs[320][2];
    if(!fin) return 0;
    for(int i = 0 ; i < 320 ; i++){
        getline(fin, line);
        cipherPairs[i][0] = line;
        getline(fin, line);
        cipherPairs[i][1] = line;
    }
    fin.close();

    int keyf[8][64];

    for(int i = 0; i < 8; i++){
        for(int j = 0; j < 64; j++){
            keyf[i][j] = 0;
        }
    }

    for(int h = 0; h < 320; h++){
        char out1[17]; // Ciphertext
        char out2[17]; // 2nd ciphertext
        for(int i = 0; i < 16; i++){
            out1[i] = cipherPairs[h][0][i];
            out2[i] = cipherPairs[h][1][i];
        }
        char o1[64], o2[64], o[64], oo1[64], oo2[64]; // Binary of ciphertext

        // Function to convert the Ciphertext to binary
        for(int i = 0; i < 16; i++){
            INT a = (unsigned int)(out1[i] - 'f');
            INT b = (unsigned int)(out2[i] - 'f');
            for(int j = i*4; j < i*4 + 4; j++){
                oo1[j] = '0' + ((a >> (3-(j-(i*4)))) & 01);
                oo2[j] = '0' + ((b >> (3-(j-(i*4)))) & 01);
            }
        }

        // Function to apply inverse permutation RIP to ciphertext
        for(int i = 0; i < 64; i++){
            o1[RFP[i]-1] = oo1[i];
            o2[RFP[i]-1] = oo2[i];
        }

        // Function to XOR o1 and o2 and store in o
        for(int i = 0; i < 64; i++){
            if(o1[i] == o2[i]){
                o[i] = '0';
            }
            else{
                o[i] = '1';
            }
        }

        char F[33];
        
        char C[33] = "00000000000000000000010000000000";
        for(int i = 0; i < 32; i++){
            if(C[i] == o[i+32]){ // Is there a final swap in fiestel?
                F[i] = '0';
            }
            else{
                F[i] = '1';
            }
        }

        // Inverse Permute F to get output of S box in Round 6
        char FP[33];
        for(int i = 0; i < 32; i++){
            FP[i] = F[INV_P[i]-1];
        }

        // Expand right half of 5th round
        char Exp1[49], Exp2[49], Exp[49];
        for(int j = 0; j < 48; j++){
            Exp1[j] = o1[E[j]];
            Exp2[j] = o2[E[j]];
            Exp[j] = o[E[j]];
        }

        // Exp[i] XOR K[i] = input to S box which outputs FP
        // Contruct set X_i

        // Make a set to keep counter of key validities, blocks S1, 2, 4, 5, 6

        printf("here %d\n", h);

        register INT t, k;
        BYTE preS1[48], preS2[48];

        /* Map 8 6-bit blocks into 8 4-bit bolcks using S-boxes */
        for(int j = 0; j < 8; j++){
            if((j == 2) || (j == 6) || (j == 7)) continue;
            INT x = 0; // XOR of input to Sj
            INT x1 = 0, x2 = 0;
            INT s_out = 0;
            for(int i = j*6; i < j*6 + 6; i++){
                if(Exp[i] == '1'){
                    x = (x << 1)+1;
                }
                else{
                    x = (x << 1)+0;
                }
                if(Exp1[i] == '1'){
                    x1 = (x1 << 1)+1;
                }
                else{
                    x1 = (x1 << 1)+0;
                }
                if(Exp2[i] == '1'){
                    x2 = (x2 << 1)+1;
                }
                else{
                    x2 = (x2 << 1)+0;
                }
            }
            for(int i = j*4; i < j*4 + 4; i++){
                if(FP[i] == '1'){
                    s_out = (s_out << 1)+1;
                }
                else{
                    s_out = (s_out << 1)+0;
                }
            }
            
            // printf("here 2\n");

            for(INT i = 0; i < 64; i++){
                k= 6*j;
                INT y = x^i; // i is Beta, y is Beta'
                for(int a = 0; a < 6; a++){
                    preS1[a+k] = (i >> (5-a)) & 01;
                    preS2[a+k] = (y >> (5-a)) & 01;
                }

                // printf("here 4\n");
                
                BYTE f1[4];
                
                t = preS1[k];
                t = (t<<1) | preS1[k+5];
                t = (t<<1) | preS1[k+1];
                t = (t<<1) | preS1[k+2];
                t = (t<<1) | preS1[k+3];
                t = (t<<1) | preS1[k+4];
                /* fetch t th entry fron jth sbox */
                t = S[j][t];
                /* generate 4-bit block from s-box entry */
                k= 4*j;
                f1[0] = (t>>3)&1;
                f1[1] = (t >> 2) & 1;
                f1[2] = (t >> 1) & 1;
                f1[3] = t &1;
                
                // printf("here 3\n");

                BYTE f2[4];
                k= 6*j;
                t = preS2[k];
                t = (t<<1) | preS2[k+5];
                t = (t<<1) | preS2[k+1];
                t = (t<<1) | preS2[k+2];
                t = (t<<1) | preS2[k+3];
                t = (t<<1) | preS2[k+4];
                /* fetch t th entry fron jth sbox */
                t = S[j][t];
                /* generate 4-bit block from s-box entry */
                k= 4*j;
                f2[0] = (t>>3)&1;
                f2[1] = (t >> 2) & 1;
                f2[2] = (t >> 1) & 1;
                f2[3] = t &1;

                INT w = 0;
                for(int i = 0; i < 4; i++){
                    w = w + ((f1[i]^f2[i]) << (3-i));
                }
                if(s_out == w){
                    // This valid pair
                    keyf[j][i^x1]++;
                }
            }
            /* Compute index t into jth s box */
        }
    }

    // 1, 2, 4, 5, 6
    INT k1, k2, k4, k5, k6;

    for(int i = 0; i < 8; i++){
        if((i == 2) || (i == 6) || (i == 7)) continue;
        INT k_max = 0;
        int num = 0;
        for(int j = 0; j < 64; j++){
            if(keyf[i][j] > num){
                num = keyf[i][j];
                k_max = (unsigned int)j;
            }
            printf("%d(%d) ", j, keyf[i][j]);
        }
        printf("\n");
        if(i == 0) k1 = k_max;
        if(i == 1) k2 = k_max;
        if(i == 3) k4 = k_max;
        if(i == 4) k5 = k_max;
        if(i == 5) k6 = k_max;
    }

    printf("k1 = %u, k2 = %u, k4 = %u, k5 = %u, k6 = %u\n", k1, k2, k4, k5, k6);

}