#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <lawrap/blas.h>

using namespace std;

//void read_file(cost std::string &filename, double* matrix) {
	
//}

int main()
{	std::vector<double> mat(49);
        std::vector<double>mat_s(49);
        std::vector<double>mat_ds(49);
        std::vector<double> D(49);
        std::vector<double>D_new(49);
//        for (int i = 0; i < 49; i++);
        std::ifstream stream1("C.data");
        std::ifstream stream2("S.data");
        std::ifstream stream3("D.data");
        
        if(!stream1)
            {
                        cout << "While opening a file an error is encountered" << endl;

            }
            else
            {
            for (int i = 0; i <49; i++)

                   {

                        stream1 >> mat[i];
                        stream2 >> mat_s[i];
                        stream3 >> D_new[i];
                         
                   }
            }
        {
            for (int k = 0; k <49; k++)
            cout << mat[k] << endl;
         }
        LAWrap :: gemm('T','N',7,7,5,2,(double* )mat.data(),7,(double* )mat.data(),7,0.0,(double* )D.data(),7);
        LAWrap :: gemm('N','N',7,7,7,1,(double*)D.data(),7,(double*)mat_s.data(),7,0.0,(double*)mat_ds.data(),7);
 {
            for (int m = 0; m <49; m++)
            cout << D[m] << endl;
         }
            double trace=0;
            for (int k = 0; k < 49; k+=8)
           {  
              trace += mat_ds[k];
//              cout << trace << " "<< mat_ds[k]<< " "<< k <<endl;
            }
           cout << trace << endl;           
           return 0 ; 
}
