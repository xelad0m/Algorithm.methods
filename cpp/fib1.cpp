#include <cassert>
#include <iostream>
#include <unordered_map>

// падает на n=500000 примерно
class Fibonacci final {
 public:
  static int get(int n) {
    assert(n >= 0);
    if (n == 0 || n == 1) {
      return n;
    } 
    
    static std::unordered_map<int, int> cache;
    auto &result = cache[n];
    if (result == 0) {
      result = get(n - 2) + get(n - 1);
    }
    return result;
  }
};

int main(void) {
  int n;
  std::cin >> n;
  std::cout << Fibonacci::get(n) << std::endl;
  return 0;
}
