#include <bits\stdc++.h>
using namespace std;

int fact(int n) {
    int ans = 1;
    for (int i = 1; i <= n; i++) {
        ans *= i;
    }
    return ans;
}

int comb(int n, int k) {
    return fact(n) / (fact(k) * fact(n - k));
}

int v(int n) {
    int r = 0;
    int r_2 = pow(2, r);
    while (n % r_2 == 0) {
        r++;
        r_2 = pow(2, r);
    }
    return r - 1;
}

int S(int n) {
    int S = 0;
    for (int k = 1; k <= n; k++) {
        cout << "k = " << k << ", n = " << n << endl;
        S += pow(-2, k) * comb(2*k, k);
    }
    cout << "S = " << S << endl;
    return S;
}

int u(int n) {
    return v(3*S(n) + 4);
}

int main() {
    // cout << "hello";
    // int ans = S(20);
    // cout << ans;
    cout << comb(34, 17);
}