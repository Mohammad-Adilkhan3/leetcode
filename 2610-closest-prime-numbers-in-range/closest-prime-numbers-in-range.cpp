class Solution {
public:
    vector<int> closestPrimes(int left, int right) {
        auto isPrime = [](int n) {
            if (n < 2) return false;
            for (int i = 2; i <= sqrt(n); i++) {
                if (n % i == 0) return false;
            }
            return true;
        };
        vector<int> primes;
        for (int i = left; i <= right; i++) {
            if (isPrime(i)) {
                primes.push_back(i);
            }
        }
        vector<int> res = {-1, -1};
        if (primes.size() < 2) return res;
        int diff = INT_MAX;
        for (size_t i = 0; i < primes.size() - 1; i++) {
            if (primes[i + 1] - primes[i] < diff) {
                diff = primes[i + 1] - primes[i];
                res[0] = primes[i];
                res[1] = primes[i + 1];
            }
        }
        return res;
    }
};