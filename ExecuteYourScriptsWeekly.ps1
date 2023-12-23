param(
    [string]$ScriptsPath = ""##Replace with the directory where your .py scripts live.
)


# Set the execution policy to allow script execution
Set-ExecutionPolicy RemoteSigned -Scope Process -Force

# Ensure the path ends with a backslash
$ScriptsPath = $ScriptsPath.TrimEnd('\') + '\'

# Define the Python script file names
$script1 = "API2CSV.py"
$script2 = "CSV2Database.py"
$script3 = "CSV2Visualizations.py"

# Execute each Python script in order
& python "$($ScriptsPath)$script1"
if ($?) { 
    Write-Host "API2CSV.py executed successfully."
} else {
    Write-Host "Error executing API2CSV.py."
    exit
}

& python "$($ScriptsPath)$script2"
if ($?) { 
    Write-Host "CSV2Database.py executed successfully."
} else {
    Write-Host "Error executing CSV2Database.py."
    exit
}

& python "$($ScriptsPath)$script3"
if ($?) { 
    Write-Host "CSV2Visualizations.py executed successfully."
} else {
    Write-Host "Error executing ThirdScript.py."
    exit
}

# Revert the execution policy to its original state
Set-ExecutionPolicy $currentPolicy -Scope Process -Force

Write-Host "All scripts executed successfully."
