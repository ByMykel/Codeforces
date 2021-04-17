//https://codeforces.com/problemset/problem/1471/B

#include <bits/stdc++.h>
using namespace std;

int main() { 
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) {
        long long n, x;
        cin >> n >> x;
        vector<pair<long long, long long>> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i].first;
            a[i].second = 1;
        }
        for (int i = 0; i < a.size(); i++) {
            if (a[i].first % x == 0) {
                a.push_back({a[i].first / x, a[i].second * x});
            } else {
                break;
            }
        }
        long long ans = 0;
        for (int i = 0; i < a.size(); i++) {
            ans += a[i].second * a[i].first;
        }
        cout << ans << '\n';
    }
}
