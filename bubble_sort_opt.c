void swap(int x, int y, int A[])
    {
        int temp = A[x];
        A[x] = A[y];
        A[y] = temp;
        return;
    }

int bubble_sort_opt(int A[], int n)
{
    for (int pass = 1; pass <= n - 1; ++pass)
    {
        int flag = 0; // flag denotes are there any swaps done in pass
        for (int i = 0; i <= n - 2; ++i)
        {
            if (A[i] > A[i + 1])
            {
                swap(i, i + 1, A);
                flag = 1; // After swap, set flag to 1
            }
        }
        if (flag == 0)
            break; // No swaps indicates we can terminate loop
    }
}