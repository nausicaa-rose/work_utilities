param(
    [Parameter (Mandatory=$true)] [string] $Path,
    [string] $OutPath
)

if (!($PSBoundParameters.ContainsKey("OutPath"))) {
    $OutPath = $Path
}

Get-ChildItem -Path ${Path}\*.zip | ForEach-Object {
    Expand-Archive -Path $_ -DestinationPath $OutPath
}