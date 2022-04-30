#include <cassert>
#include <cstdint>
#include <iostream>

template <class Int>
Int gcd(Int a, Int b) {
  assert(a > 0 && b > 0);

  // алгоритм Эквклида
  while (a > 0 && b > 0) {
    if (a > b) {
      a %= b;
    } else {
      b %= a;
    }
  }
  return a == 0 ? b : a;
}

int main(void) {
  std::int64_t a, b;
  std::cin >> a >> b;
  const int RUN_COUNT = 1000000;
  for (int i = 0; i < RUN_COUNT; i++) {
    gcd(a, b);
  }
  std::cout << gcd(a, b) << std::endl;
  return 0;
}
