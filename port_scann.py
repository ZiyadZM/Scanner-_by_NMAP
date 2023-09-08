import nmap
A = 75
B = 80
target = '127.0.0.1'
scanner = nmap.PortScanner()
for i in range(A, B+1):
    res = scanner.scan(target, str(i))
    res = res['scan'][target]['tcp'][i]['state']
    print(f'Port{i} is {res}.')
