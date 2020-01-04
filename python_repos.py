import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# 执行API调用并存储相应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code", r.status_code)

# 将API相应存储在一个变量中
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])# 指出一共有多少个python仓库

# 搜索有关仓库的信息
repo_dicts = response_dict['items'] # items是一个由字典组成的列表，每一个字典存储了关于这个仓库的各种信息

names, stars = [], []
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	stars.append(repo_dict['stargazers_count'])

# 可视化
my_style = LS('#333366', base_style = LCS)
chart = pygal.Bar(style = my_style, x_label_rotation = 45, show_legend = False)
chart.title = 'Most-Starrde Python project on GitHub'
chart.x_labels = names # 设置横坐标的名称

chart.add('', stars) # 加入标签
chart.render_to_file('python_repos.svg')

# 研究第一个仓库(研究第一个字典)
# repo_dict = repo_dicts[0]

# print('\nSelected information about first repository:')
# for repo_dict in repo_dicts:
# 	print('name', repo_dict['name'])
# 	print('Owner:', repo_dict['owner']['login'])
# 	print('Stars', repo_dict['stargazers_count'])
# 	print('Repository:', repo_dict['html_url'])
# 	print('Created:', repo_dict['created_at'])
# 	print('Update:', repo_dict['updated_at'])
# 	print('Description:', repo_dict['description'])

# # print("\nKeys:", len(repo_dict))
# # for key in sorted(repo_dict.keys()):
# # 	print(key)

# # 处理结果
# print(response_dict.keys())
