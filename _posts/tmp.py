import os
teams = {
	"Gungnir": ["许臻佳", "周子寒", "金之涵"],
	"Laevateinn": ["范裕达", "杨卓林", "丁尧尧"],
	"Metis": ["龙思杉", "谢雨桐", "蔡静怡"],
	"Mjolnir": ["胥拿云", "谭博文", "王洋鲲"],
	"New Meta": ["李文昊", "秋闻达", "高宇"],
	"Reshiram": ["方博慧", "杨嘉成", "罗中瑭"],
	"Spear of Longinus": ["苏雨峰", "刘予希", "张凯羿"]
}

s = "---\nname: %s\ncategory: acmicpc_team\nleader: %s\nmember: %s、%s\nfeature: acmicpc/2016-2017/%s.jpg\n---\n"

def trans(s):
	return '_'.join(s.split(' '))

for team_name, member in teams.items():
	filename = "2016-07-01-acmicpc_team_%s.md" % trans(team_name)
	os.system("touch %s" % filename)
	with open(filename, "w") as fobj:
		fobj.write(s % (team_name, member[0], member[1], member[2], trans(team_name)))
