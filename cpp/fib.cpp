#include <cassert>
#include <iostream>


// наивный алгоритм
class Fibonacci final {
 public:
  static int get(int n) {
    assert(n >= 0);
    if (n == 0 || n == 1) {
      return n;
    } 
    return get(n - 2) + get(n - 1);
  }
};

int main(void) {
  int n;
  std::cin >> n;
  std::cout << Fibonacci::get(n) << std::endl;
  return 0;
}
