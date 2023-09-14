#include <bits\stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> a, b;
    for (int i = 0; i < n; i++) {
        int inp;
        cin >> inp;
        a.push_back(inp);
    }
    b = a;
    int tmp = 0, ct = 0;
    for (int i = 1; i < n; i++) {
        if (a[i] > a[tmp]) {
            a[i]--;
            a[tmp]++;
            ct++;
            i = 1;
            tmp = 0;
        } else {
            tmp = i;
        }
    }

    tmp = 0;
    int ct2 = 0;

    for (int i = 1; i < n; i++) {
        if (b[i] > b[tmp]) {
            b[i]--;
            b[tmp]++;
            ct++;
            i = 1;
            tmp = 0;
        } else {
            tmp = i;
        }
    }

    cout << min(ct, ct2);
}