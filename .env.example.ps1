$Env:API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
$Env:AUTHDOMAIN = "xxx...xxx.firebaseapp.com"
$Env:DBUTL="https://xxx...xxx.firebaseio.com"
$Env:SBUCKET="xxx...xxx.appspot.com"

# Uncomment the following if you'd like the environment variables
# to be permanently set on your user account for this machine.

<#

[Environment]::SetEnvironmentVariable("API_KEY", $Env:API_KEY, "User")
[Environment]::SetEnvironmentVariable("AUTHDOMAIN", $Env:AUTHDOMAIN, "User")
[Environment]::SetEnvironmentVariable("DBUTL", $Env:DBUTL, "User")
[Environment]::SetEnvironmentVariable("SBUCKET", $Env:SBUCKET, "User")

#>
