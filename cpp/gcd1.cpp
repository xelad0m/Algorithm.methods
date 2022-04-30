#include <cassert>
#include <cstdint>
#include <iostream>

template <class Int>
Int gcd(Int a, Int b) {
  assert(a > 0 && b > 0);
  // optimize this function

  Int current_gcd = 1;
  for (Int d = 2; d <= a && d <= b; d++) {
    if (a % d == 0 && b % d == 0) {
      current_gcd = d;
    }
  }
  return current_gcd;
}

int main(void) {
  std::int64_t a, b;
  std::cin >> a >> b;
  std::cout << gcd(a, b) << std::endl;
  return 0;
}
