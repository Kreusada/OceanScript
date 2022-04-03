<#
.Synopsis
Makefile script in PowerShell.
.Description
Commands for reformatting and style checking/diffing.
#>

[CmdletBinding()]
param (
    [Parameter(Mandatory=$false)]
    [ArgumentCompleter({
        param (
            $commandName,
            $parameterName,
            $wordToComplete,
            $commandAst,
            $fakeBoundParameters
        )
        $script:availableCommands = @("reformat", "stylecheck", "stylediff", "activateenv")
        return $script:availableCommands | Where-Object { $_ -like "$wordToComplete*" }
    })]
    [String]
    $command,
    [switch]
    $help = $false
)

function reformat() {
    & $script:venvPython -m black $PSScriptRoot
}

function stylecheck() {
    & $script:venvPython -m black --check $PSScriptRoot
    Exit $LASTEXITCODE
}

function stylediff() {
    & $script:venvPython -m black --check --diff $PSScriptRoot
    Exit $LASTEXITCODE
}

function activateenv() {
    & $PSScriptRoot\.venv\Scripts\Activate.ps1
}

$script:availableCommands = @("reformat", "stylecheck", "stylediff", "activateenv")

if (Test-Path -LiteralPath "$PSScriptRoot\.venv" -PathType Container) {
    $script:venvPython = "$PSScriptRoot\.venv\Scripts\python.exe"
} else {
    $script:venvPython = "python"
}

if ($help -or !$command) {
    Get-Help $MyInvocation.InvocationName
    exit
}

switch ($command) {
    {$script:availableCommands -contains $_} {
        & $command
        break
    }
    default {
        Write-Host (
            """$command"" is not a valid command.",
            "To see available commands, type: ""$($MyInvocation.InvocationName) -help"""
        )
        break
    }
}
