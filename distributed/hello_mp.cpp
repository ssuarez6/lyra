/*
 * This program shows how many processors and threads are available at this machine
 * This program is an example about how to use parallel programming
 * openmp is included in gcc compiler so you dont have to install anythin
 * for compiling: g++ -o hello_mp hello_mp.cpp -fopenmp
 */

#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <omp.h>

using namespace std;

int main( int args, char *argv[]){
  int id;
  double wtime;
  cout << "\n" << " Number of processors available  = "
       << omp_get_num_procs() << "\n" << "Max number of threads = " 
       << omp_get_max_threads() << "\n";
  wtime = omp_get_wtime();
#pragma omp parallel				\
  private (id)
  {
  id = omp_get_thread_num();
  cout << "This is process" << id << "\n";
  }

  wtime = omp_get_wtime() - wtime;
 cout << "\n" << "Elapsed wall clock time = " << wtime << "\n";
 
 return 0;
}
