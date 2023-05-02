#!/bin/bash

# 画像ファイルの拡張子
EXTENSION="png"

# 変換後のディレクトリ
OUTPUT_DIR="default-textures"

# 変換前のファイルのリスト
FILES=$(ls *)

# 変換前のファイルを1つずつRGBA変換して変換後のディレクトリに保存
for FILE in $FILES; do
    # ファイル名と拡張子に分割
    FILENAME="${FILE%.*}"
    FILEEXT="${FILE##*.}"

    # RGBA変換して保存
    convert $FILE -alpha set -background none "$OUTPUT_DIR/$FILENAME-rgba.$FILEEXT"
done

# for f in ./default-textures/*; do
#     # ファイル一つ毎の処理
#     echo "file: $f"
#     convert $f -strip $f
# done