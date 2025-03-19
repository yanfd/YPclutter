def hanoi(n, start, mid, end):
	if n>0:
		hanoi(n-1, start, end, mid)
		print(f"{n} 从{start} 到了{end}")
		hanoi(n-1, mid, start, end)


hanoi(3,"A","B","C")

