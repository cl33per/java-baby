$CSVfile = Read-Host "Enter the Path of CSV file (Eg. C:\Teams.csv)"
$output = @()
$i = 0
$AllGroups = Get-AzADGroup
Foreach($group in $AllGroups){
    $AllGroupMember = Get-AzADGroupMember -GroupObjectId $group.Id
        Foreach($member in $AllGroupMember){
            $userObj = New-Object PSObject
            $userObj | Add-Member NoteProperty -Name "Group Name" -Value $group.DisplayName
            $userObj | Add-Member NoteProperty -Name "Group Description" -Value $group.Description
            $userObj | Add-Member NoteProperty -Name "Group MailNickname" -Value $group.MailNickname
            $userObj | Add-Member NoteProperty -Name "Group SecurityEnabled" -Value $group.SecurityEnabled
            $userObj | Add-Member NoteProperty -Name "Group Username" -Value $member.DisplayName
            $output += $userObj
        }
    $i++
    Write-Progress -activity "Scanning Groups...." -status "Scanned: $i of $($AllGroups.Count)" -percentComplete (($i / $AllGroups.Count)  * 100)
    # Write-Output $output
    $output | Export-csv -Path $CSVfile -NoTypeInformation -Encoding UTF8
}
