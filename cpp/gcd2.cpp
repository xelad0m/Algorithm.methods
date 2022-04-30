#include <cassert>
#include <cstdint>
#include <iostream>

template <class Int>
Int gcd(Int a, Int b) {
  assert(a > 0 && b > 0);
  // optimize this function

  Int current_gcd = 1;
  for (Int d = 1; d * d <= a && d <= b; d++) {
    if (a % d == 0) {
      if (b % d == 0) {
        current_gcd = d;
      }
      Int big_d = a / d;
      if (b % big_d == 0) {
        return big_d;
      }
    }
  }
  return current_gcd;
}

int main(void) {
  std::int64_t a, b;
  std::cin >> a >> b;
  // const int RUN_COUNT = 1000000;
  // for (int i = 0; i < RUN_COUNT; i++) {
  //  gcd(a, b);
  //}
  std::cout << gcd(a, b) << std::endl;
  return 0;
}
