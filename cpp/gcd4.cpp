#include <cassert>
#include <cstdint>
#include <utility>    // swap
#include <iostream>

template <class Int>
Int gcd(Int a, Int b) {
  assert(a > 0 && b > 0);

  // алгоритм Эквклида
  while (b > 0) {   //  а = 0 проверять теперь не обязательно
    // можно не проверять больше меньше, а делить одно на другое
    a %= b;
    std::swap(a, b);  // меняем местами
  }
  return a;
}

int main(void) {
  std::int64_t a, b;
  std::cin >> a >> b;
  const int RUN_COUNT = 1000000;  // тест 1 млн раз
  for (int i = 0; i < RUN_COUNT; i++) {
    gcd(a, b);
  }
  std::cout << gcd(a, b) << std::endl;
  return 0;
}
