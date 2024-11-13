#include <iostream>
#include <vector>
using namespace std;

int main() {
  int N, P, temp;
  vector<int> nums;

  for (int i = 0; i < N; i++) {
      cin >> temp;
      cout << "temp: " << temp << endl;
      nums.push_back(temp);
  }

  for (int j = 0; j < N; j++){
      if (nums[j] >= P/2) {
          cout << j << " ";
      }
  }
  cout << endl;

  return 0;
}
