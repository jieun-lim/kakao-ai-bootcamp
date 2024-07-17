
## load_dataset() 로 로컬 파일 읽기 
Hugging Face의 datasets 라이브러리에서 제공하는 함수로, 다양한 형식의 데이터셋을 로드하는 데 사용됩니다. 이 함수는 로컬 파일이나 온라인 데이터셋을 로드할 수 있으며, 데이터셋을 쉽게 전처리하고 토큰화하는 데 유용합니다.

```
data = load_dataset(path, data_files= {})
```

## 주요 파라미터
- path: 데이터셋 파일의 형식입니다. 예를 들어, 'text', 'json', 'csv' 등이 있습니다.
- data_files: 로컬 파일을 지정하는 경우 사용됩니다. 훈련, 검증, 테스트 데이터셋을 각각 지정할 수 있습니다. 예를 들어, {'train': 'train.txt', 'validation': 'validation.txt'}.
여기서 학습데이터의 경로를 지정해줍니다. 
- split: 로드할 데이터셋의 분할을 지정합니다. 예를 들어, 'train', 'test', 'validation' 등의 분할을 선택할 수 있습니다.
- cache_dir: 데이터셋을 캐시할 디렉토리를 지정합니다.
- features: 데이터셋의 특징을 지정하는 데 사용됩니다. 데이터셋의 각 필드의 데이터 타입을 지정할 수 있습니다.
- download_config: 데이터셋 다운로드 설정을 지정하는 데 사용됩니다.
- revision: 데이터셋의 특정 버전을 로드하는 데 사용됩니다.


## 예제 

```
from datasets import load_dataset

# data 디렉토리 내의 모든 텍스트 파일을 로드
data_files = {
    "train": "data/train.txt",
    "validation": "data/validation.txt"
}


```