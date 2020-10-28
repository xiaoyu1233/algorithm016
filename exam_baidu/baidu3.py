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
