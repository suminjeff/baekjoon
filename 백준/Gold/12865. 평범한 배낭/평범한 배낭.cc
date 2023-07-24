#include <iostream>
using namespace std;

int obj[100][2]; // obj[i][0] : 'i'th obj's weight
				 // obj[i][1] : 'i'th obj's value
int M[100][100001]; // M[i][j]: i'th obj in, max j weight, total value

int max(int n, int m) {
	return (n > m ? n : m);
}



int dp_Values(int N, int K) {
	for (int n = 1; n < N; n++) {
		for (int k = 1; k <= K; k++) {
			if (obj[n][0] > k) {
				M[n][k] = M[n - 1][k];
			}
			else
				M[n][k] = max(M[n - 1][k - obj[n][0]] + obj[n][1], M[n - 1][k]);
		}
	}
	

	return M[N - 1][K];
}


int main() {
	int N, K;
	cin >> N >> K;
	for (int i = 0; i < N; i++) {
		cin>>obj[i][0]>>obj[i][1];
	}
	for (int n = 0; n < N; n++) {
		M[n][0] = 0;
	}
	for (int k = 0; k <= K; k++) {
		if (obj[0][0] > k)
			M[0][k] = 0;
		else
			M[0][k] = obj[0][1];
	}

	cout << dp_Values(N, K)<<endl;
}
