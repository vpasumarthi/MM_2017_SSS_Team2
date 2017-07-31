#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <math.h>

//#include <pybind11/pybind11.h>
//#include<pybind11/stl.h>
#include<iostream>
#include<string>
//#include<pybind11/numpy.h>

//anamespace py = pybind11;

//void print_arg (const std::string & s)
//{
 //std::cout << "string argument: " << s << std::endl;

//}


int main() {
  std::vector<std::vector<double>> allData;
  std::vector<double> x;
  std::vector<double> y;
  std::vector<double> z;
//  std::vector<double> rij;
//  std::vector<double> rij2;
   
  std::ifstream fin("coordinates.txt");
  std::string line;
  while (std::getline(fin, line)) {      // for each line
    std::vector<double> lineData;           // create a new row
    double val;
    std::istringstream lineStream(line); 
    while (lineStream >> val) {          // for each value in line
      lineData.push_back(val);           // add to the current row
    }
    allData.push_back(lineData);         // add row to allData
  } 



for (int j = 1; j < 2; j++)

{

   for (int i = 2; i < 20; i++)
{
    x.push_back(allData[i][j]);
 
 }
}
for (int j = 2; j < 3; j++)

{ 

   for (int i = 2; i < 20; i++)
{
    y.push_back(allData[i][j]);
 
   } 
}
for (int j = 3; j < 4; j++)

{

   for (int i = 2; i < 20; i++)
  {
    z.push_back(allData[i][j]);
 
}     


}
for (int l = 0; l < 18; l++)
{
 for (int m = l+1; m < 18; m++)
   {
       double box =10.0;
       double rij2 = ((x[l] - x[m])*(x[l]-x[m]) + (y[l] - y[m])*(y[l]-y[m])+(z[l] - z[m])*(z[l]-z[m]));
       double rij = sqrt(rij2);
       int ratio = rij/box;
       rij = box * ratio;
      double sig_by_r6 = (1/rij)^6;
      double sig_by_r12 = (1/rij)^12;
      double potential_energy = 4.0 *(sig_by_r12-sig_by_r6);
    }
}
for (int n = 0; n <rij2.size(); n++)
     {
      std :: cout<<rij2[n]<<'\n';
      }
     return 0;
}
