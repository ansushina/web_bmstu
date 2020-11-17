### без балансировки 10000


```
ab -c 10 -n 10000 http://127.0.0.1/api/v1/genres/
This is ApacheBench, Version 2.3 <$Revision: 1807734 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 1000 requests
Completed 2000 requests
Completed 3000 requests
Completed 4000 requests
Completed 5000 requests
Completed 6000 requests
Completed 7000 requests
Completed 8000 requests
Completed 9000 requests
Completed 10000 requests
Finished 10000 requests


Server Software:        WSGIServer/0.2
Server Hostname:        127.0.0.1
Server Port:            80

Document Path:          /api/v1/genres/
Document Length:        768 bytes

Concurrency Level:      10
Time taken for tests:   72.449 seconds
Complete requests:      10000
Failed requests:        1
   (Connect: 0, Receive: 0, Length: 1, Exceptions: 0)
Non-2xx responses:      1
Total transferred:      10799278 bytes
HTML transferred:       7679414 bytes
Requests per second:    138.03 [#/sec] (mean)
Time per request:       72.449 [ms] (mean)
Time per request:       7.245 [ms] (mean, across all concurrent requests)
Transfer rate:          145.57 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       3
Processing:     0   72  13.6     71     145
Waiting:        0   72  13.5     71     143
Total:          0   72  13.6     71     146

Percentage of the requests served within a certain time (ms)
  50%     71
  66%     76
  75%     80
  80%     82
  90%     89
  95%     96
  98%    107
  99%    117
 100%    146 (longest request)

```


### с балансировкой 10000


```
ab -c 10 -n 10000 http://127.0.0.1/api/v1/genres/
This is ApacheBench, Version 2.3 <$Revision: 1807734 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 1000 requests
Completed 2000 requests
Completed 3000 requests
Completed 4000 requests
Completed 5000 requests
Completed 6000 requests
Completed 7000 requests
Completed 8000 requests
Completed 9000 requests
Completed 10000 requests
Finished 10000 requests


Server Software:        WSGIServer/0.2
Server Hostname:        127.0.0.1
Server Port:            80

Document Path:          /api/v1/genres/
Document Length:        768 bytes

Concurrency Level:      10
Time taken for tests:   44.095 seconds
Complete requests:      10000
Failed requests:        0
Total transferred:      10800000 bytes
HTML transferred:       7680000 bytes
Requests per second:    226.78 [#/sec] (mean)
Time per request:       44.095 [ms] (mean)
Time per request:       4.409 [ms] (mean, across all concurrent requests)
Transfer rate:          239.19 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.2      0      10
Processing:    10   44  27.0     39     152
Waiting:       10   44  27.0     39     152
Total:         10   44  27.0     39     152

Percentage of the requests served within a certain time (ms)
  50%     39
  66%     59
  75%     66
  80%     70
  90%     81
  95%     90
  98%    101
  99%    109
 100%    152 (longest request)

```
### без балансировки 10000
```
 ab -c 10 -n 100000 http://127.0.0.1/api/v1/genres/1/
This is ApacheBench, Version 2.3 <$Revision: 1807734 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 10000 requests
Completed 20000 requests
Completed 30000 requests
Completed 40000 requests
Completed 50000 requests
Completed 60000 requests
Completed 70000 requests
Completed 80000 requests
Completed 90000 requests
Completed 100000 requests
Finished 100000 requests


Server Software:        WSGIServer/0.2
Server Hostname:        127.0.0.1
Server Port:            80

Document Path:          /api/v1/genres/1/
Document Length:        28 bytes

Concurrency Level:      10
Time taken for tests:   326.246 seconds
Complete requests:      100000
Failed requests:        50253
   (Connect: 0, Receive: 0, Length: 50253, Exceptions: 0)
Non-2xx responses:      50253
Total transferred:      34854882 bytes
HTML transferred:       10539012 bytes
Requests per second:    306.52 [#/sec] (mean)
Time per request:       32.625 [ms] (mean)
Time per request:       3.262 [ms] (mean, across all concurrent requests)
Transfer rate:          104.33 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       8
Processing:     0   32  76.6      1    5063
Waiting:        0   32  76.6      1    5063
Total:          0   33  76.5      1    5063

Percentage of the requests served within a certain time (ms)
  50%      1
  66%     56
  75%     60
  80%     63
  90%     69
  95%     77
  98%     97
  99%    111
 100%   5063 (longest request)

```


### с балансировкой 100000

```
ab -c 10 -n 100000 http://127.0.0.1/api/v1/genres/1/
This is ApacheBench, Version 2.3 <$Revision: 1807734 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 10000 requests
Completed 20000 requests
Completed 30000 requests
Completed 40000 requests
Completed 50000 requests
Completed 60000 requests
Completed 70000 requests
Completed 80000 requests
Completed 90000 requests
Completed 100000 requests
Finished 100000 requests


Server Software:        WSGIServer/0.2
Server Hostname:        127.0.0.1
Server Port:            80

Document Path:          /api/v1/genres/1/
Document Length:        28 bytes

Concurrency Level:      10
Time taken for tests:   420.282 seconds
Complete requests:      100000
Failed requests:        0
Total transferred:      33900000 bytes
HTML transferred:       2800000 bytes
Requests per second:    237.94 [#/sec] (mean)
Time per request:       42.028 [ms] (mean)
Time per request:       4.203 [ms] (mean, across all concurrent requests)
Transfer rate:          78.77 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0      13
Processing:    11   42  25.1     37     265
Waiting:       11   42  25.1     37     265
Total:         11   42  25.1     37     266

Percentage of the requests served within a certain time (ms)
  50%     37
  66%     55
  75%     62
  80%     66
  90%     76
  95%     84
  98%     95
  99%    105
 100%    266 (longest request)
```