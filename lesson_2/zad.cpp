#include<iostream>
#include<string>
#include<fstream>
#include<vector>

#define pb push_back

using namespace std;


struct arr{
    string name, surename;
    int year;
    float accuracy;
};


bool check_candidate(string name, string surename, int year, float accuracy){
    int name_size = name.size();
    int sname_size = surename.size();
    return (name_size > 3 && sname_size >= 3 && surename.substr( sname_size - 3, 3 ) == "ski");
}


string anonymization(string x){
    int n = x.size()-4;
    string new_x="";
    new_x += x[0];
    while(n--)new_x += '*';
    new_x += x[x.size()-3];
    new_x += x[x.size()-2];
    new_x += x[x.size()-1];
    return new_x;
}


int main(){
    vector<arr>output;

    string filename;
    cin>>filename;
    ifstream in(filename + ".txt", ios::in);

    if(in.fail()){
        cout<<"File does not exist"<<endl;
        return 1;
    }


    arr curr_max; curr_max.accuracy=-1.0;


    string name, surename;
    int year;
    float accuracy;

    while(in>>name>>surename>>year>>accuracy){

        if ( check_candidate(name, surename, year, accuracy)  && accuracy > curr_max.accuracy){
            curr_max.name = anonymization(name);
            curr_max.surename = anonymization(surename);
            curr_max.year = year;
            curr_max.accuracy = accuracy;
            output.clear();
            output.pb(curr_max);
        }
        else if ( check_candidate(name, surename, year, accuracy)  && accuracy == curr_max.accuracy){
            curr_max.name = anonymization(name);
            curr_max.surename = anonymization(surename);
            curr_max.year = year;
            curr_max.accuracy = accuracy;
            output.pb(curr_max);
        }
    }
    in.close();

    ofstream out(filename + ".max", ios::out);

    if(output.empty()){
        out<<endl;
        return 0;
    }
    for(int i=0; i<output.size(); i++){
        out<<output[i].name<<" "<<output[i].surename<<" "<<output[i].year<<endl;
    }
    out.close();

    return 0;
}
