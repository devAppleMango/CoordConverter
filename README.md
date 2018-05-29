# CoordConverter
파이썬 좌표 변환 프로그램

```python
LatLong_to_TM(latitude, longtitude) # 경위도 -> TM
TM_to_LatLong(X, Y) # TM -> 경위도
```
options 
* `origin`: `midOrigin`(중부원점, default), `westOrigin`(서부원점), `eastOrigin`(동부원점), `eastSeaOrigin`(동해원점)
* `ellipsoid`: `grs80`(default), `bessel`

참고 자료 [1/1.000수치지형도 좌표변환 표준작업지침](http://www.ngii.go.kr/kor/board/view.do?rbsIdx=31&idx=251)
