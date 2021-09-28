param(
    [Parameter (Mandatory=$true)] [string] $Path,
    [string] $Include,
    [string] $Exclude,
    [Parameter (Mandatory=$true)] [string] $Pattern,
    [switch] $Recurse
)

if ($Recurse) {
    if ($Include -and $Exclude) {
        Get-ChildItem -Path $Path -Include $Include -Exclude $Exclude -Recurse | Select-String -List -Pattern $Pattern
    } elseif ($Include) {
        Get-ChildItem -Path $Path -Include $Include -Recurse | Select-String -List -Pattern $Pattern
    } elseif ($Exclude) {
        Get-ChildItem -Path $Path -Exclude $Exclude -Recurse | Select-String -List -Pattern $Pattern
    } else {
        Get-ChildItem -Path $Path -Recurse | Select-String -List -Pattern $Pattern
    }
} else {
    if ($Include -and $Exclude) {
        Get-ChildItem -Path $Path -Include $Include -Exclude $Exclude | Select-String -List -Pattern $Pattern
    } elseif ($Include) {
        Get-ChildItem -Path $Path -Include $Include | Select-String -List -Pattern $Pattern
    } elseif ($Exclude) {
        Get-ChildItem -Path $Path -Exclude $Exclude | Select-String -List -Pattern $Pattern
    } else {
        Get-ChildItem -Path $Path | Select-String -List -Pattern $Pattern
    }
}

