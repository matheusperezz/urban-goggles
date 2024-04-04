//
// Created by mathe on 4/3/2024.
//

#include <iostream>
#include "problems.h"

using namespace std;

int minhaFuncao() {
  return 42;
}

int problem331() {
  int prisionerA, prisionerB;
  cin >> prisionerA >> prisionerB;

  if (prisionerA == prisionerB and prisionerA == 1) {
    cout << "Resultado para o Prisioneiro A: sentença leve (1 ano)" << endl;
    cout << "Resultado para o Prisioneiro B: sentença leve (1 ano)" << endl;
  } else if (prisionerA > prisionerB) {
    cout << "Resultado para o Prisioneiro A: sentença pesada (10 anos)" << endl;
    cout << "Resultado para o Prisioneiro B: livre" << endl;
  } else if (prisionerB > prisionerA) {
    cout << "Resultado para o Prisioneiro A: livre" << endl;
    cout << "Resultado para o Prisioneiro B: sentença pesada (10 anos)" << endl;
  } else {
    cout << "Resultado para o Prisioneiro A: sentença moderada (5 ano)" << endl;
    cout << "Resultado para o Prisioneiro B: sentença moderada (5 ano)" << endl;
  }

  return 0;
}

int problem264() {
  double total = 0;
  int n;
  cin >> n;
  for (int i = 0; i < n; i++){
    int quant; double value;
    cin >> quant >> value;
    total += quant * value;
  }

  printf("%.2f", total);
  return 0;
}