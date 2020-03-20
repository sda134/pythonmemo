::コマンドを非表示
@echo off

:: module名（ファイルフルパス）を指定して、引数付きで実行
python %~dp0\basic\basic.py hogehoge


echo ""

:: パッケージとして実行
python -m structured

::pause