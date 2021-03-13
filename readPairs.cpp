#include<iostream>
#include<fstream>

using namespace std;

int main(){
    ifstream fin;
    fin.open("merge_output_1.txt");
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

    ofstream fout;
    fout.open("pair_output_1.txt");

    // the following code if for verification purpose only 
    for(int i = 0 ; i < 320; i++){
        fout << cipherPairs[i][0] << " " << cipherPairs[i][1] << endl;
    }
    fout.close();
    return 0;
}