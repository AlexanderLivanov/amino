#include <iostream>
#include <fstream>
#include <string>

using std::string;
using std::cout;

int main(){

    std::ifstream file("amino.txt");
    std::string amino;
    unsigned long long int res = 1;

    if(file.is_open()){
        while (std::getline(file, amino)) {
            for(int i = 0; i <= amino.size(); i++){
                if(amino[i] == 'a') { res *= 4; } 
                if(amino[i] == 'r') { res *= 6; }
                if(amino[i] == 'n') { res *= 2; }
                if(amino[i] == 'd') { res *= 2; }
                if(amino[i] == 'c') { res *= 2; }
                if(amino[i] == 'q') { res *= 2; } 
                if(amino[i] == 'e') { res *= 2; } // or 4?
                if(amino[i] == 'g') { res *= 4; }
                if(amino[i] == 'h') { res *= 2; }
                if(amino[i] == 'i') { res *= 3; }
                if(amino[i] == 'l') { res *= 6; } 
                if(amino[i] == 'k') { res *= 2; }
                if(amino[i] == 'm') { res *= 1; }
                if(amino[i] == 'f') { res *= 2; }
                if(amino[i] == 'p') { res *= 4; }
                if(amino[i] == 's') { res *= 6; } 
                if(amino[i] == 't') { res *= 4; }
                if(amino[i] == 'w') { res *= 4; } // wait what??
                if(amino[i] == 'y') { res *= 2; }
                if(amino[i] == 'v') { res *= 4; }
                cout << res << " ";
            }
        }
    }
    
}