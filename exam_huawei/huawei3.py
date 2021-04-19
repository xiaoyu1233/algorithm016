# include<iostream>
# include<queue>
# include<vector>
# include<algorithm>

using
namespace
std
int
main()
{
    int
E, N;
cin >> E >> N;
vector < vector < int >> task;
for (int i = 0; i < N; i++)
{
    int
id, p, b, t;
cin >> id >> p >> b >> t;
if (b + t) <= E
task.push_back({id, p, b, t});

}
sort(task.begin(), task.end(), []
(const
vector))



#include<iostream>
#include<queue>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
    int E,N;
    cin>>E>>N;
    vector<vector<int>> task;
    for(int i=0; i < N; i++)
    {
        int id, p, b, t;
        cin>>id>>p>>b>>t;
        if(b+t<=E)
            task.push_back({id, p, b, t});
    }
    sort(task.begin(),task.end(), [](const vector<int>&a, const vector<int>&b){ return a[2] < b[2];});
    vector<int> dp(task.size(), 0);
    vector<int> next(task.size(), -1);
    dp[0] = task[0][1];
    int max_profit = task[0][1];
    int max_index = 0;
    for(int i=1; i<task.size();i++)
    {
        dp[i] = task[i][1];
        next[i] = -1;
        for(int j=0; j< i; j++)
        {
            if(task[j][2] + task[j][3] < task[i][2])
            {
                if(dp[i] < dp[j] + task[i][1])
                {
                    dp[i] = dp[j] + task[i][1];
                    next[i] = j;
                }
            }
        }
        if(max_profit < dp[i])
            max_index = i;
    }
    max_profit = dp[max_index];
    vector<vector<int>> ans;
    while(max_index>=0)
    {

        ans.push_back(task[max_index]);
        max_index = next[max_index];
    }
    cout<<max_profit<<endl<<ans.size()<<endl;
    for(int i=ans.size()-1; i>=0;i--)
        cout<<ans[i][0]<<endl;
    return 0;

}