# Pipenvをインストールして実行する場合

## 前提条件
 * Pipenv がインストール済み

## モジュールのインストール
```
pipenv install
```

## 実行確認

### 仮想環境の起動
```
pipenv shell
```

### pytest を実行する場合(仮想環境起動後)
```
pytest
```

### watch-test を実行する場合(仮想環境起動後)
```
pytest-watch
```

# Dockerを使って実行する場合

## 前提条件
 * Docker がインストール済み
 * Docker Compose がインストール済み

## 実行確認

### コンテナの起動 & コンテナへの接続
```
docker-compose up -d --build
docker-compose exec python3 bash
```

### pytestを 実行する場合(コンテナに接続後)
```
pytest
```

### watch-testを実行する場合(コンテナに接続後)
```
pytest-watch
```

# 次は？

src/tutorial_test.py に pytestでテストを書く最低限の文法を説明します。
詳しく調べたい場合は次を参照

https://docs.pytest.org/
