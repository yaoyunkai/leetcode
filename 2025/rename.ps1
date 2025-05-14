# 设置目标文件夹路径（默认为当前目录）
$directory = Get-Location

# 获取所有文件（不包括目录）
Get-ChildItem -Path $directory -File | ForEach-Object {
    $file = $_
    $baseName = $file.BaseName
    $extension = $file.Extension

    # 使用正则表达式匹配以数字开头、后跟一个点、且点后有内容的文件名
    if ($baseName -match '^(\d+)\.(.+)$') {
        # 提取数字部分并转换为整数
        $number = [int]$matches[1]
        # 提取点后的内容
        $rest = $matches[2]

        # 格式化为四位数（前导补零）
        $newBaseName = "{0:0000}.{1}" -f $number, $rest
        # 构建新文件名
        $newName = $newBaseName + $extension

        # 输出重命名信息（可选）
        Write-Host "Renaming '$($file.Name)' to '$newName'"

        # 执行重命名操作
        Rename-Item -Path $file.FullName -NewName $newName
    }
}