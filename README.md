# jhta_matjip

2조 세미프로젝트
* **강태욱** -*짱짱 조장님* - [GitHub] (https://github.com/rafinkang)
* **김민수** - [GitHub] (https://github.com/kimsubbae113)
* **김기욱** - [GitHub] (https://github.com/tarsonia1)
* **서민정** - [GitHub] (https://github.com/MinjeongSuh88)


## Python Google 스타일 가이드
* 글로벌
```
GLOBAL_CONSTANT_NAME
```

* CamelCase
```
ClassName
ExceptionName
```
* snake_case
```
module_name
package_name
method_name
function_name
global_var_name
instance_var_name
function_parameter_name
local_var_name
```
* mixCase
```
안씀
```

## 중앙hta 지도 중심 좌표
```
c=14136711.5110454,4519281.4097483,20,0,0,0,dh
```

## build
```
pip install auto-py-to-exe

pyinstaller --noconfirm --onefile --windowed --hidden-import "pkg_resources.py2_warn" --paths "E:/jhta_matjip/jhta_matjip"  "E:/jhta_matjip/jhta_matjip/main.py"
cd out
```