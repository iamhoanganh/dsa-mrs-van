#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> bubble_sort(vector<int> arr)
{
    int n = arr.size();
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (arr[j] < arr[j + 1])
            {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
    return arr;
}

int binary_search(vector<int> arr, int x)
{
    int left = 0;
    int right = arr.size() - 1;
    while (left <= right)
    {
        int mid = (left + right) / 2;
        if (arr[mid] == x)
        {
            return mid;
        }
        else if (arr[mid] > x)
        {
            left = mid + 1;
        }
        else
        {
            right = mid - 1;
        }
    }
    return -1;
}

int main()
{
    int n;
    cin >> n;

    vector<int> arr(n);
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    int m;
    cin >> m;

    vector<int> queries(m);
    for (int i = 0; i < m; i++)
    {
        cin >> queries[i];
    }

    // Sắp xếp mảng theo thứ tự giảm dần
    vector<int> sorted_arr = bubble_sort(arr);

    // In ra mảng đã sắp xếp
    for (int i = 0; i < n; i++)
    {
        cout << sorted_arr[i] << " ";
    }
    cout << endl;

    // Tìm vị trí của các phần tử trong mảng đã sắp xếp
    for (int i = 0; i < m; i++)
    {
        int index = binary_search(sorted_arr, queries[i]);
        cout << (index != -1 ? to_string(index) : "-1") << endl;
    }

    return 0;
}
